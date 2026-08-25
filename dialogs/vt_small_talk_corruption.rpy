label vt_small_talk_corruption:
    "You bring up some topics that might push her boundaries."

    if selected_girl.corruption < 15:
        "[selected_girl] looks uncomfortable with the direction of the conversation."

        if selected_girl.discipline > 70:
            $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"discipline": (250, 750)})
        elif selected_girl.fear > 60:
            $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"fear": (250, 750)})
        elif selected_girl.affection > 40:
            $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"affection": (-750, -250)})
        elif selected_girl.intellect > 70:
            $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"intellect": (250, 750)})
        elif selected_girl.naturism > 60:
            $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (-750, -250)})
        else:
            $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
            selected_girl.character "[_line]"

        $ selected_girl.apply_impacts({"affection": (-750, -250), "fear": (250, 750)})
    else:
        if selected_girl.corruption < 30:
            "[selected_girl] looks a little surprised but curious to hear more."

            if selected_girl.discipline > 50 and selected_girl.affection > 20:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750), "affection": (250, 750)})
            elif selected_girl.intellect > 60:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750)})
            elif selected_girl.fear > 40:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (250, 750)})
            elif selected_girl.naturism > 50:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
        elif selected_girl.corruption < 45:
            "[selected_girl] looks intrigued, wanting to hear more."

            if selected_girl.discipline > 40 and selected_girl.corruption > 35:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750)})
            elif selected_girl.affection > 40 and selected_girl.fear < 30:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750), "fear": (-750, -250)})
            elif selected_girl.intellect > 60:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750)})
            elif selected_girl.naturism > 60:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
        elif selected_girl.corruption < 60:
            "[selected_girl] looks intrigued, her curiosity clearly piqued."

            if selected_girl.discipline > 30 and selected_girl.affection > 50:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750), "affection": (250, 750)})
            elif selected_girl.fear > 30 and selected_girl.corruption > 50:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (250, 750)})
            elif selected_girl.intellect > 50 and selected_girl.corruption > 50:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750)})
            elif selected_girl.naturism > 50 and selected_girl.affection > 40:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750), "affection": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
        elif selected_girl.corruption < 75:
            "[selected_girl] looks completely captivated by the conversation."

            if selected_girl.discipline > 20 and selected_girl.corruption > 65:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.fear < 20 and selected_girl.affection > 60:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (250, 750), "affection": (250, 750)})
            elif selected_girl.intellect > 60 and selected_girl.discipline < 30:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750), "discipline": (-750, -250)})
            elif selected_girl.naturism > 70:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
            
        else:
            "[selected_girl] looks at you with a mischievous, knowing smile."

            if selected_girl.discipline < 20 and selected_girl.corruption > 80:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.fear < 10 and selected_girl.affection > 70:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (250, 750), "affection": (250, 750)})
            elif selected_girl.intellect > 60 and selected_girl.corruption > 85:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            elif selected_girl.naturism > 70 and selected_girl.discipline < 20:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750), "discipline": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "corruption_smalltalk", player)
                selected_girl.character "[_line]"
        # Diminishing returns at highest corruption levels
        $ selected_girl.apply_impacts({"corruption": (250, 750), "fear": (-750, -250), "discipline": (-600, -300)})

    return
