label vt_small_talk_naturism:
    "You bring up some topics related to nature and natural living."

    if selected_girl.naturism < 15:
        "[selected_girl] looks uncomfortable and hesitant."

        if selected_girl.discipline > 70:
            $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (-750, -250)})
        elif selected_girl.corruption > 60:
            $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (-750, -250)})
        elif selected_girl.intellect > 70:
            $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (-750, -250)})
        elif selected_girl.fear > 60:
            $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (-750, -250)})
        elif selected_girl.affection > 40:
            $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (-750, -250)})
        else:
            $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
            selected_girl.character "[_line]"
        
        $ selected_girl.apply_impacts({"naturism": (250, 750), "discipline": (250, 750)})
    else:
        if selected_girl.naturism < 30:
            "[selected_girl] looks a little surprised but curious to hear more."

            if selected_girl.discipline > 50:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750)})
            elif selected_girl.corruption > 40:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750)})
            elif selected_girl.intellect > 60:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            elif selected_girl.fear > 40:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (250, 750)})
            elif selected_girl.affection > 30:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
            
        elif selected_girl.naturism < 45:
            "[selected_girl] looks intrigued, considering your words carefully."

            if selected_girl.discipline > 40:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 30:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.intellect > 50:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            elif selected_girl.fear > 30:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (250, 750)})
            elif selected_girl.affection > 40:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
            
        elif selected_girl.naturism < 60:
            "[selected_girl] looks intrigued and interested, leaning forward."

            if selected_girl.discipline > 30:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 20:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.intellect > 40:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            elif selected_girl.fear > 20:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (-750, -250)})
            elif selected_girl.affection > 50:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
            
        elif selected_girl.naturism < 75:
            "[selected_girl] looks completely at ease and engaged."

            if selected_girl.discipline > 20:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 10:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.intellect > 30:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            elif selected_girl.fear > 10:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (-750, -250)})
            elif selected_girl.affection > 60:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
            
        else:
            "[selected_girl] looks completely at ease, her movements natural and fluid."

            if selected_girl.discipline > 10:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 0:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.intellect > 20:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            elif selected_girl.fear > 0:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (-750, -250)})
            elif selected_girl.affection > 70:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "naturism_smalltalk", player)
                selected_girl.character "[_line]"
            
        # Diminishing returns at highest naturism levels
        $ selected_girl.apply_impacts({"naturism": (250, 750), "discipline": (-750, -250), "fear": (-750, -250), "corruption": (-750, -250)})

    return

