# Covert pill-slipping: a second, non-consensual path alongside the open give-medicine flow
# (vt_give_medicine, 05_vt_gift_flow_repoint.rpy). Reached as a follow-up to an existing/new
# coffee action at two locations: the coffee shop's "Buy her a coffee" (PATRONS only -- the
# working barista uses a separate, untouched database_coffee_shop_barista_options list, so this
# is patron-only for free, no extra check needed) and a wholly new "Offer to refill her coffee"
# action added to the teacher's lounge.
#
# Neither base-game file is edited directly (consistent with this mod's established
# additive-only approach -- see vt_repoint_menu_label / vt_repoint_gift_menu_label and the
# vt_academy_bathroom_sex precedent, all in the existing *_ren.py database-patch files): the
# coffee-shop hook repoints the existing "Buy her a coffee" menu entry to a small wrapper label
# that calls the real, unmodified base label and then offers the covert picker; the lounge action
# is purely appended as new database entries + a new label, exactly like vt_academy_bathroom_sex.
#
# Deliberately does NOT go through vt_ask_reachable/vt_willingness_band/vt_dock_gift_gate
# (04_vt_dock_coercion.rpy) -- those model a conversation she's a knowing, consenting party to.
# The entire point of slipping something into her coffee is that she never finds out, so applying
# is unconditional (mirroring what the mechanical layer -- apply_planb_pill/apply_emergency_pill
# -- already does on its own), gated only by pill ownership and, for the two DOCK items, whether
# it would be mechanically pointless.
#
# HARD RULE for every gating/narration decision below: never leak information the player doesn't
# already have. All of it is keyed on player_knows_pregnant (what the PLAYER knows), never on
# knows_pregnant (what SHE knows) or the raw pregnant flag -- a player who doesn't know she's
# pregnant must see identical menu state and narration whether she is or isn't, every time. This
# is why apply_emergency_pill takes a notify=False here: its built-in notify is keyed on HER
# awareness (correct for the open flow, where her own dialogue masks the secrecy), which would
# leak her pregnancy to the player here since she says and does nothing to mask it.

init python:

    def vt_covert_slip_options(girl):
        """Build the covert pill picker's menu list for `girl`. Returns [] if the player owns
        nothing eligible -- callers should skip the menu entirely in that case (this is a bonus
        add-on after a real action already chosen, not a dedicated menu entry, so there's no
        "nothing to offer" message)."""
        med_ids = ("fertility_pill", "prenatal_vitamins", "planb_pill", "emergency_pill")
        pill_counts = vt_player_pill_counts(player)
        gifts_db = database_shop_items["gifts"]

        # Shared with vt_give_medicine (05_vt_gift_flow_repoint.rpy) and vt_get_items_and_quantity
        # (00_vt_patcher.rpy) via vt_should_hide_fertiboost -- requires player_knows_pregnant, so
        # the no-leak rule holds.
        hide_ferti = vt_should_hide_fertiboost(girl)
        # SafeDOCK: pointless once pregnant -- same grey-out condition/wording as vt_give_medicine.
        safedock_pointless = getattr(girl, "pregnant", False) and getattr(girl, "player_knows_pregnant", False)
        # DryDOCK: pointless if not pregnant, or past the 14-real-day window -- but ONLY greyed
        # out when the player already knows enough to deduce that himself. If he doesn't know
        # she's pregnant at all, this stays enabled and behaves identically regardless of her true
        # state (never a tell).
        drydock_pointless = False
        if getattr(girl, "player_knows_pregnant", False):
            try:
                current_day = time_manager.total_days
            except NameError:
                current_day = 0
            within_window = getattr(girl, "pregnant", False) and (current_day - getattr(girl, "preg_start_day", 0)) <= 14
            drydock_pointless = not within_window

        options = []
        for pid in med_ids:
            cnt = pill_counts.get(pid, 0)
            if cnt <= 0:
                continue
            if pid == "fertility_pill" and hide_ferti:
                continue
            gift_obj = gifts_db.get(pid)
            if gift_obj is None:
                continue
            caption = f"{gift_obj.name} (Owned: {cnt})"
            if pid == "planb_pill" and safedock_pointless:
                options.append((f"{caption}|It would be pointless -- {girl.first_name} is already pregnant.", None))
            elif pid == "emergency_pill" and drydock_pointless:
                options.append((f"{caption}|It would be pointless -- there's nothing left for it to do.", None))
            else:
                options.append((caption, pid))
        return options

# Called as a follow-up from an already-chosen action (buying/refilling her coffee) at the coffee
# shop and teacher's lounge -- not its own menu entry, so silently returns if there's nothing to
# offer or the player backs out.
label vt_covert_slip_pill(girl):
    $ _vc_options = vt_covert_slip_options(girl)

    if not _vc_options:
        return

    $ _vc_options.append(("Never mind.", "__vt_cancel__"))
    $ _vc_chosen = renpy.display_menu(_vc_options)

    if _vc_chosen in (None, "__vt_cancel__"):
        return

    $ time_manager.skip_time(minutes=2)

    if _vc_chosen == "planb_pill":
        $ girl.apply_planb_pill()

    elif _vc_chosen == "emergency_pill":
        # Only reachable within the 14-day window when she's known to be pregnant
        # (drydock_pointless greys it out past that); otherwise reachable regardless of her true
        # state. Either way the shared narration below stays identical and non-committal about
        # whether it worked -- the game's own pregnancy tracking, not this narration, is what
        # eventually shows the outcome (see the no-leak HARD RULE at the top of this file).
        $ girl.apply_emergency_pill(notify=False)

    elif _vc_chosen == "fertility_pill":
        if not girl.pregnant:
            $ girl.fertility_boost += 7

    elif _vc_chosen == "prenatal_vitamins":
        $ girl.prenatal_boost = getattr(girl, "prenatal_boost", 0) + 1

    # Shared across every branch -- deliberately identical wording regardless of pill or her
    # state, so nothing is inferable from the narration alone (see the no-leak HARD RULE above).
    # REVISIT: kept as one hoisted line for now. If this ever grows per-pill/per-branch flavor
    # text, re-derive each branch's wording from a no-leak-safe axis only (e.g. pill id, never
    # pregnant/knows_pregnant) so divergence can't become an inferable tell.
    "You stir it into her coffee, dissolving it into the dark liquid before she looks back."
    "[girl] picks up her coffee and takes a sip, none the wiser."

    $ vt_spend_pill_ammo(player, _vc_chosen)

    return

# Repoint target for the coffee shop's existing "Buy her a coffee" entry (database_coffee_shop_options
# -- patrons only; database_coffee_shop_barista_options, the working girl's own list, is untouched).
# Calls the real base label unmodified -- nothing to keep in sync on a future base-game update --
# then offers the covert picker as a follow-up. Same technique as vt_gift_menu
# (05_vt_gift_flow_repoint.rpy).
label vt_coffee_buy_with_covert_offer:
    call coffee_shop_discussion_buy_girl_coffee
    call vt_covert_slip_pill(selected_girl)
    return

# Wholly new lounge action (not a repoint -- there's no existing "refill coffee" action to wrap).
# A small, no-cost workplace favor (smaller reward than the shop's $25 "buy coffee" since it costs
# the player nothing) plus the same covert offer.
label vt_lounge_coffee_refill:
    $ time_manager.skip_time(minutes=5)

    player.character "Let me top off your coffee for you."

    selected_girl.character "Oh, thank you, [player]. That's sweet of you."

    $ selected_girl.apply_impacts({"affection": (250, 500)})

    call vt_covert_slip_pill(selected_girl)

    return

# Registration: repoint the coffee-shop entry, append the new lounge entry. Runs at init -1 --
# after database_coffee_shop_options/database_teacher_discussion_options/
# database_teaching_assistant_discussion_options exist (base game, init -4) and after
# vt_repoint_gift_menu_label is defined (05_vt_gift_flow_repoint.rpy, init -2).
init -1 python:

    if "database_coffee_shop_options" in globals() and "vt_repoint_gift_menu_label" in globals():
        vt_repoint_gift_menu_label(database_coffee_shop_options, "coffee_shop_discussion_buy_girl_coffee", "vt_coffee_buy_with_covert_offer")
    else:
        renpy.log("VT MOD ERROR: could not repoint coffee_shop_discussion_buy_girl_coffee for the covert offer -- database_coffee_shop_options or vt_repoint_gift_menu_label not found.")

    _VT_LOUNGE_REFILL_ENTRY = ("'vt_lounge_coffee_refill' not in actions_already_done", "Offer to refill her coffee", "vt_lounge_coffee_refill")
    for _vt_lounge_db_name in ("database_teacher_discussion_options", "database_teaching_assistant_discussion_options"):
        if _vt_lounge_db_name in globals():
            _vt_lounge_db = globals()[_vt_lounge_db_name]
            if not any(label == "vt_lounge_coffee_refill" for _cond, _text, label in _vt_lounge_db):
                _vt_lounge_db.append(_VT_LOUNGE_REFILL_ENTRY)
        else:
            renpy.log(f"VT MOD ERROR: {_vt_lounge_db_name} not found! Could not add vt_lounge_coffee_refill.")
