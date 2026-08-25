# Repoints every base-game "Give gift" menu entry (give_girl_gift / give_mother_gift) to a tiny
# 2-choice submenu below: "Gift Item" (the REAL, untouched base game/give_mother_gift label --
# zero duplication, so base-game gift updates are inherited automatically) vs "Give Medicine"
# (a small VT-owned picker for the mod's 4 pill items: FertiBOOST, PregnaVITA, SafeDOCK,
# DryDOCK).
#
# History: the first attempt hooked in at Gift.give_gift() (01_vt_mod_items.rpy), but the base
# game's "takes it with joy...I love it!" narration is hardcoded directly in label
# give_girl_gift and runs BEFORE give_gift() is ever called, so that produced contradictory
# back-to-back narration for SafeDOCK/DryDOCK. The second attempt fixed that by fully
# reimplementing label give_girl_gift/give_mother_gift as vt_ copies -- it worked, but meant
# permanently duplicating ~50 lines of base label body that would silently drift out of sync on
# any base-game gift-flow update. This version instead only intercepts the CHOICE of which flow
# to enter: "Gift Item" calls the real base label directly (nothing to keep in sync, ever), and
# only the 4 VT pills -- genuinely new content the base game knows nothing about -- get their own
# small, VT-owned flow.
#
# Repointed via the same data-repoint technique already used elsewhere in this mod (small-talk
# topics, the pre-exam event, the library scene -- see vt_repoint_menu_label in
# events/vt_location_dialogue_database_ren.py) rather than a base-label override
# (config.label_overrides), which this mod deliberately avoids for mod-manager eligibility.
#
# Scope: base game only. Other installed mods that add their own "Give gift" menu entries (found:
# _mods/sponsor_addons/fit_and_fast, _mods/ggypt_library_expansion) are left untouched -- not our
# data to edit; those specific menus still route straight to the base give_girl_gift/
# give_mother_gift (no "Give Medicine" option, but no double-dialogue bug either, since they never
# touch Gift.give_gift() for a not-giftable item -- the 4 pills are simply absent from their gift
# grids too, via is_giftable=False in 01_vt_mod_items.rpy).

init -2 python:

    def vt_repoint_gift_menu_label(options, old_label, new_label):
        """Like vt_repoint_menu_label, but ALSO rewrites the requirements string's literal
        old_label token, not just the trailing label element. Gift menu entries gate themselves
        with "'<label>' not in actions_already_done", and actions_already_done (or, during a home
        visit, actions_already_done_home_visit) is tracked by the label actually jumped to --
        confirmed in label_girl_office_discussion.rpy / label_mother_discussion.rpy: menu_choice
        is the chosen option_label, appended verbatim BEFORE the label runs. Repointing only the
        trailing label while leaving the self-referential condition on the old name would break
        the daily "already gave a gift today" gate: the old token would never be appended again,
        so the condition would always read True (unlimited gifts/day)."""
        for i, entry in enumerate(options):
            if entry[-1] == old_label:
                new_requirements = entry[0].replace(f"'{old_label}'", f"'{new_label}'")
                options[i] = (new_requirements,) + entry[1:-1] + (new_label,)
                return True
        return False

    # Every base-game list containing a "Give gift" -> give_girl_gift entry.
    # databases/locations/location_dialogue_database_ren.py:
    _VT_GIRL_GIFT_LISTS = [
        "database_teacher_discussion_options",
        "database_teaching_assistant_discussion_options",
        "database_secretary_discussion_options",
        "database_girl_office_discussion_options",
        "database_mother_office_discussion_options",
        "database_alumni_office_discussion_options",
        "database_alumni_mother_office_discussion_options",
        "database_student_bathroom_options",
        "database_alumni_bathroom_options",
        "database_student_cafeteria_options",
        "database_alumni_cafeteria_options",
        "database_nurse_discussion_options",
        "database_student_clinic_options",
        "database_alumni_clinic_options",
        "database_locker_room_options",
        "database_locker_room_shower_options",
        "database_alumni_locker_room_options",
        "database_bar_bartender_options",
        "database_bar_options",
        "database_beach_options",
        "database_park_options",
        "database_pier_options",
        "database_coffee_shop_barista_options",
        "database_coffee_shop_options",
        "database_clothing_store_clerk_options",
        "database_clothing_store_options",
        # locations/shoot_studio/shoot_studio_entries_ren.py:
        "database_shoot_assistant_discussion_options",
        "database_student_shoot_studio_options",
        "database_shoot_changing_room_options",
        # databases/home_visit/daughter_discussion_options_database_ren.py:
        "database_home_visit_daughter_discussion_options",
        "database_home_visit_daughter_discussion_alumni_options",
    ]

    # databases/home_visit/mother_discussion_options_database_ren.py:
    _VT_MOTHER_GIFT_LISTS = [
        "database_home_visit_mother_discussion_options",
        "database_home_visit_mother_discussion_alumni_options",
    ]

    _vt_girl_gift_repointed = 0
    for _vt_name in _VT_GIRL_GIFT_LISTS:
        if _vt_name in globals():
            if vt_repoint_gift_menu_label(globals()[_vt_name], "give_girl_gift", "vt_gift_menu"):
                _vt_girl_gift_repointed += 1
        else:
            renpy.log(f"VT MOD WARNING: gift-menu repoint target '{_vt_name}' not found -- base game may have changed.")

    _vt_mother_gift_repointed = 0
    for _vt_name in _VT_MOTHER_GIFT_LISTS:
        if _vt_name in globals():
            if vt_repoint_gift_menu_label(globals()[_vt_name], "give_mother_gift", "vt_mother_gift_menu"):
                _vt_mother_gift_repointed += 1
        else:
            renpy.log(f"VT MOD WARNING: gift-menu repoint target '{_vt_name}' not found -- base game may have changed.")

    renpy.log(
        f"VT MOD: Gift-menu repoint -- {_vt_girl_gift_repointed}/{len(_VT_GIRL_GIFT_LISTS)} give_girl_gift entries, "
        f"{_vt_mother_gift_repointed}/{len(_VT_MOTHER_GIFT_LISTS)} give_mother_gift entries."
    )

    def vt_clear_gift_action_today(is_mother_flow=False):
        """Undo the daily 'already gave a gift today' mark when the player backed out without
        actually giving anything. actions_already_done is tracked by the label actually jumped
        to (see vt_repoint_gift_menu_label's docstring above) -- since that's now vt_gift_menu /
        vt_mother_gift_menu, not give_girl_gift / give_mother_gift, the base label's own internal
        cancel-cleanup (label_give_girl_gift.rpy, still checking the OLD name) is a no-op
        post-repoint; this replaces it under the new name."""
        label_name = "vt_mother_gift_menu" if is_mother_flow else "vt_gift_menu"
        if is_during_home_visit:
            if label_name in actions_already_done_home_visit:
                actions_already_done_home_visit.remove(label_name)
        else:
            if label_name in actions_already_done.get(selected_girl.id, []):
                actions_already_done[selected_girl.id].remove(label_name)

# Shared implementation for both vt_gift_menu (girl) and vt_mother_gift_menu (mother) below --
# they differ only in which base label "Gift Item" calls and whether "Give Medicine" needs the
# selected_girl-swap. "Gift Item" calls the real base label unmodified. Cancelling out of it can't
# be told apart from a successful gift by inspecting selected_gift alone (the base label sets it
# to None either way), so elapsed game time is used as the signal instead: give_girl_gift/
# give_mother_gift only call time_manager.skip_time on an actual gift, never on cancel.
label vt_gift_menu_impl(base_label, is_mother_flow=False):
    menu:
        "Gift Item":
            $ _vt_pre_time = (time_manager.total_days, time_manager.hour, time_manager.minute)
            $ renpy.call(base_label)
            if (time_manager.total_days, time_manager.hour, time_manager.minute) == _vt_pre_time:
                $ vt_clear_gift_action_today(is_mother_flow=is_mother_flow)

        "Give Medicine":
            if is_mother_flow:
                $ temporary_girl = selected_girl
                $ selected_girl = selected_girl.mother

            call vt_give_medicine

            if is_mother_flow:
                $ selected_girl = temporary_girl
                $ temporary_girl = None

        "Never mind.":
            $ vt_clear_gift_action_today(is_mother_flow=is_mother_flow)
    return

label vt_gift_menu:
    call vt_gift_menu_impl("give_girl_gift")
    return

label vt_mother_gift_menu:
    call vt_gift_menu_impl("give_mother_gift", True)
    return

# Picker for the 4 VT pill items (sidecar "ammo" counts, not real inventory Gift objects -- see
# vt_player_pill_counts, 00_vt_patcher.rpy). SafeDOCK/DryDOCK skip straight to give_gift(), which
# routes them to vt_dock_gift_gate (04_vt_dock_coercion.rpy) for consent handling. FertiBOOST/
# PregnaVITA keep their existing vanilla accept-chance roll and reaction lines -- reproduced here
# (not called into label_give_girl_gift.rpy, which always shows the full gift-picker grid, not a
# single pre-chosen item) rather than duplicated wholesale; these two lines are the only base-game
# narration this file re-implements.
label vt_give_medicine:
    python:
        _vt_med_ids = ("fertility_pill", "prenatal_vitamins", "planb_pill", "emergency_pill")
        _vt_pill_counts = vt_player_pill_counts(player)
        _vt_gifts_db = database_shop_items["gifts"]
        # Shared with vt_get_items_and_quantity (00_vt_patcher.rpy) and vt_covert_slip_options
        # (06_vt_covert_pill.rpy) via vt_should_hide_fertiboost, so the condition can't drift.
        _vt_hide_ferti = vt_should_hide_fertiboost(selected_girl)
        _vt_med_options = []
        for _vt_pid in _vt_med_ids:
            _vt_cnt = _vt_pill_counts.get(_vt_pid, 0)
            if _vt_cnt <= 0:
                continue
            if _vt_pid == "fertility_pill" and _vt_hide_ferti:
                continue
            _vt_gift_obj = _vt_gifts_db.get(_vt_pid)
            if _vt_gift_obj is None:
                continue
            _vt_caption = f"{_vt_gift_obj.name} (Owned: {_vt_cnt})"
            if _vt_pid == "planb_pill" and getattr(selected_girl, "pregnant", False) and getattr(selected_girl, "player_knows_pregnant", False):
                # SafeDOCK only blocks FUTURE conception -- pointless on an existing pregnancy he
                # already knows about. Value None renders this entry disabled/muted with the
                # tooltip via the shared choice screen (game/screens.rpy) -- the same "Text|tooltip"
                # + None-value convention every "not currently available" base-game menu entry
                # already uses (e.g. every "Give gift|Given a gift today" tuple).
                _vt_med_options.append((f"{_vt_caption}|It would be pointless -- {selected_girl.first_name} is already pregnant.", None))
            else:
                _vt_med_options.append((_vt_caption, _vt_pid))

    if not _vt_med_options:
        "You don't have any medicine to offer [selected_girl] right now."
        return

    # A real sentinel, not None -- an item whose value is None renders DISABLED (see the SafeDOCK
    # case above), so "Never mind." would otherwise be unclickable.
    $ _vt_med_options.append(("Never mind.", "__vt_cancel__"))
    $ _vt_chosen_id = renpy.display_menu(_vt_med_options)

    if _vt_chosen_id in (None, "__vt_cancel__"):
        return

    $ time_manager.skip_time(minutes=5)

    player.character "Here [selected_girl], I got you something."

    $ selected_gift = database_shop_items["gifts"][_vt_chosen_id]

    if selected_gift.id in ("planb_pill", "emergency_pill"):
        $ selected_gift.give_gift(selected_girl)
    elif selected_girl.accept_gift(selected_gift):
        "[selected_girl] takes the [selected_gift] from your hands, her face filled with joy."

        selected_girl.character "Oh, thank you! I love it!"

        $ selected_gift.give_gift(selected_girl)
    else:
        $ selected_gift.apply_gift_impacts(selected_girl, accepted_gift=False)

        "[selected_girl] pushes back your outstretched hand."

        selected_girl.character "Umm... Thanks but no thanks, I cannot accept that."

    $ selected_gift = None

    return
