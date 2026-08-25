# Climax pull-out coercion. Redirect target for creampie_pussy (01_vt_mod_items.rpy): a bare, not-on-BC,
# low-baby-desire girl interjects to make you pull out. Push (stop_bc_breed willingness) or respect her.
# Outcomes: eager=finish inside + permanent creampie flag; conditional=this session only; else=pull out.

init python:

    # Tunable impacts (revisit during playtest).
    VT_PULLOUT_IMPACTS = {
        "yes_perm":    {"corruption": (500, 1000), "baby_desire": (200, 500)},
        "yes_session": {"corruption": (200, 500)},
        "no_soft":     {"affection": (-250, -100)},
        "no_hard":     {"affection": (-500, -250), "fear": (200, 500)},
        "respect":     {"affection": (100, 300)},
    }

    # Her interjection when you go to finish inside.
    VT_PULLOUT_INTERJECT = {
        "crude":    ["Wait -- pull out! I'm not on the pill, don't you dare cum in me!"],
        "explicit": ["Nngh -- pull out! I'm not on anything, you can't finish inside!"],
        "direct":   ["Wait -- pull out. I'm not on birth control, don't cum in me."],
        "neutral":  ["W-wait, pull out! I'm not on anything right now!"],
        "shy":      ["N-no, pull out! P-please, I'm not on the pill...!"],
        "demure":   ["Wait -- you mustn't finish inside. I'm not protected...!"],
    }

    # Player's push lines.
    VT_PULLOUT_PUSH = [
        "I'm too close to stop... let me finish inside you, just this once.",
        "I want to cum in you so bad... let me fill you up.",
    ]

    # Her answer, keyed by outcome then register.
    VT_PULLOUT_LINES = {
        "yes_perm": {
            "crude":    ["Fuck it -- do it. Fill me up, and keep cumming in me from now on."],
            "explicit": ["God... yes, finish inside me. Don't pull out -- not now, not ever."],
            "direct":   ["...Okay. Finish inside. And keep doing it -- I want it."],
            "neutral":  ["...Do it. Cum inside me. I don't want you to pull out anymore."],
            "shy":      ["I... o-okay. Finish inside... I want to feel it. Every time."],
            "demure":   ["...Very well. Finish inside me. Don't hold back -- not anymore."],
        },
        "yes_session": {
            "crude":    ["...Fuck it, just this once. Cum in me. But you pull out next time."],
            "explicit": ["Ohh -- okay, this once. Finish inside... but only this time."],
            "direct":   ["...Fine, just this time. Cum in me -- but we go back to pulling out after."],
            "neutral":  ["...Okay, just this once. Finish inside. But pull out next time."],
            "shy":      ["I-I... just this once, okay? O-only because you're so close..."],
            "demure":   ["This once, then. Finish inside -- but do not presume it again."],
        },
        "no": {
            "crude":    ["No! Pull out -- pull out now!"],
            "explicit": ["No -- not inside! Pull out, I mean it!"],
            "direct":   ["No. Pull out. I'm not risking it."],
            "neutral":  ["No -- pull out! Please!"],
            "shy":      ["N-no, please pull out! I-I can't...!"],
            "demure":   ["No -- withdraw. I will not be finished inside."],
        },
    }

    # Her line when you pull out (respect choice).
    VT_PULLOUT_RESPECT = {
        "crude":    ["Good -- yeah, all over me. Thanks for not risking it."],
        "explicit": ["Mmm -- yes, pull out, cover me. Thank you for being careful."],
        "direct":   ["Thank you. Pulling out -- that's the right call."],
        "neutral":  ["Thank you for pulling out. I feel safer with you."],
        "shy":      ["Th-thank you for pulling out... I was scared for a second."],
        "demure":   ["Thank you for withdrawing. That was considerate of you."],
    }

    def vt_accepts_creampie(girl):
        """Permanent 'you may finish inside me' concession (sidecar flag)."""
        try:
            return bool(vt_girl_bucket(girl).get("vt_accepts_vaginal_creampie", False))
        except Exception as e:
            renpy.log(f"VT MOD ERROR: vt_accepts_creampie failed for {getattr(girl, 'first_name', girl)}: {e!r}")
            return False

    def vt_set_accepts_creampie(girl, val=True):
        """Returns True if the permanent flag was actually persisted, False on failure -- callers
        that narrate a permanent concession should check this rather than assume the write landed."""
        try:
            vt_girl_bucket(girl)["vt_accepts_vaginal_creampie"] = bool(val)
            return True
        except Exception as e:
            renpy.log(f"VT MOD ERROR: vt_set_accepts_creampie failed for {getattr(girl, 'first_name', girl)}: {e!r} -- permanent flag NOT saved.")
            return False

    def vt_wants_pullout(girl):
        """True if she'll interject for a pull-out: raw (or a broken condom she's aware of), not wanting a
        condom now, not on BC, not pregnant, baby_desire band 'none', not already conceded."""
        if girl is None or not isinstance(girl, Girl):
            return False
        if not getattr(store, "is_during_sex_interaction", False):
            return False
        # Raw: no condom, or a broken one she's aware of.
        _raw = getattr(player, "condom_active", "raw") == "raw"
        _broke_known = getattr(player, "condom_broke", False) and getattr(girl, "aware_vaginal_condom", False)
        if not (_raw or _broke_known):
            return False
        # Wants a condom now -> the condom gate handles it, not this.
        if vt_condom_now(girl, "vaginal"):
            return False
        if getattr(girl, "birth_control", False):
            return False
        if getattr(girl, "pregnant", False):
            return False
        if vt_baby_desire_band(girl) != "none":
            return False
        if vt_accepts_creampie(girl):
            return False
        if girl.id in getattr(store, "vt_creampie_session", set()):
            return False
        return True

    def vt_try_creampie(girl, player=None):
        """Resolve a 'let me finish inside' push; store the result for the gate to show."""
        if player is None:
            player = getattr(store, "player", None)

        band = vt_willingness_band(girl, "stop_bc_breed", player)
        if band == "eager":
            if vt_set_accepts_creampie(girl, True):                # permanent
                outcome, line_key = "yes_perm", "yes_perm"
            else:
                # Persisting the permanent flag failed -- fall back to session-only rather than
                # promising a permanent concession that didn't actually save.
                outcome, line_key = "yes_session", "yes_session"
                store.vt_creampie_session.add(girl.id)
        elif band == "conditional":
            outcome, line_key = "yes_session", "yes_session"
            store.vt_creampie_session.add(girl.id)                 # this session only
        elif band == "hesitant":
            outcome, line_key = "no_soft", "no"
        else:
            outcome, line_key = "no_hard", "no"

        impacts = VT_PULLOUT_IMPACTS.get(outcome)
        if impacts:
            girl.apply_impacts(dict(impacts))

        line = vt_voice(girl, VT_PULLOUT_LINES[line_key], "Pull out!")
        store.vt_pullout_result = {"outcome": outcome, "line": line}

default vt_pullout_result = None

# Redirect target for creampie_pussy (01_vt_mod_items.rpy), called with the option_label kwargs.
# Resolves the pull-out, then plays the real creampie or the external cumshot.
label vt_pullout_climax_gate(action_name=None, additional_subtags=None, skip_descriptions=False, skip_responses=False):
    python:
        _pg_girl = selected_girl
        _pg_real = "generic_action_creampie_pussy"     # cum inside
        _pg_pullout = "generic_action_cumshot_pussy"   # pull out (external)

    # Not a pull-out girl -> finish inside as chosen.
    if not vt_wants_pullout(_pg_girl):
        $ renpy.call(_pg_real, action_name=action_name, additional_subtags=additional_subtags, skip_descriptions=skip_descriptions, skip_responses=skip_responses)
        return

    # She interjects.
    $ _pg_interject = vt_voice(_pg_girl, VT_PULLOUT_INTERJECT, "Wait -- pull out! I'm not on anything!")
    _pg_girl.character "[_pg_interject]"

    $ _pg_out = "respect"
    menu:
        "Push her to let you finish inside":
            $ _pg_pitch = renpy.random.choice(VT_PULLOUT_PUSH)
            player.character "[_pg_pitch]"
            $ vt_try_creampie(_pg_girl, player)
            python:
                _pg_res = vt_pullout_result or {}
                _pg_out = _pg_res.get("outcome", "no_hard")
                _pg_line = _pg_res.get("line", "")
            if _pg_line:
                _pg_girl.character "[_pg_line]"

        "Respect her -- pull out":
            $ _pg_rline = vt_voice(_pg_girl, VT_PULLOUT_RESPECT, "Thank you for pulling out.")
            _pg_girl.character "[_pg_rline]"
            $ _pg_girl.apply_impacts(dict(VT_PULLOUT_IMPACTS.get("respect", {})))

    if _pg_out in ("yes_perm", "yes_session"):
        # Finish inside.
        $ renpy.call(_pg_real, action_name=action_name, additional_subtags=additional_subtags, skip_descriptions=skip_descriptions, skip_responses=skip_responses)
    else:
        # Pull out -> external cumshot.
        $ renpy.call(_pg_pullout, action_name=action_name, additional_subtags=additional_subtags, skip_descriptions=skip_descriptions, skip_responses=skip_responses)
    return
