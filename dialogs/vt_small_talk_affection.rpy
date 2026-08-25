label vt_small_talk_affection:
    "You bring up some topics that might interest her."

    if selected_girl.affection < 15:
        "[selected_girl] seems guarded and keeps her distance."

        if selected_girl.fear > 60:
            $ _line = vt_say(selected_girl, "affection_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"fear": (250, 750)})
        elif selected_girl.discipline > 60:
            $ _line = vt_say(selected_girl, "affection_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"discipline": (250, 750)})
        elif selected_girl.corruption > 60:
            $ _line = vt_say(selected_girl, "affection_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"corruption": (250, 750)})
        elif selected_girl.intellect > 70:
            $ _line = vt_say(selected_girl, "affection_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"intellect": (250, 750)})
        elif selected_girl.naturism > 60:
            $ _line = vt_say(selected_girl, "affection_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (250, 750)})
        else:
            $ _line = vt_say(selected_girl, "affection_smalltalk", player)
            selected_girl.character "[_line]"
        
        $ selected_girl.apply_impacts({"affection": -500, "fear": (250, 750)})
    else:
        if selected_girl.affection < 30:
            "[selected_girl] seems to be warming up to you slightly."

            if selected_girl.intellect > 70 and selected_girl.discipline > 50:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750), "discipline": (250, 750)})
            elif selected_girl.naturism > 70:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750)})
            elif selected_girl.corruption > 40 and selected_girl.fear < 40:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "fear": (-750, -250)})
            elif selected_girl.fear > 50:
                $ selected_girl.apply_impacts({"fear": 250})
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
            else:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
            
            $ selected_girl.apply_impacts({"affection": (250, 750)})
        elif selected_girl.affection < 45:
            "[selected_girl] is becoming more engaged in the conversation."
            if selected_girl.discipline > 60 and selected_girl.corruption < 30:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "discipline": (-750, -250)})
            elif selected_girl.fear > 40 and selected_girl.affection > 35:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (-750, -250)})
            elif selected_girl.naturism > 50 and selected_girl.intellect < 60:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750), "intellect": (-750, -250)})
            elif selected_girl.corruption > 50 and selected_girl.discipline < 40:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "discipline": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                
            $ selected_girl.apply_impacts({"affection": (250, 750)})
        elif selected_girl.affection < 60:
            "[selected_girl] is leaning in, clearly interested in what you're saying."

            if selected_girl.fear > 40 and selected_girl.affection > 50:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (-750, -250)})
            elif selected_girl.discipline > 60 and selected_girl.corruption > 30:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "discipline": (-750, -250)})
            elif selected_girl.naturism > 60 and selected_girl.intellect > 60:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750), "intellect": (250, 750)})
            elif selected_girl.corruption > 60 and selected_girl.fear < 30:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "fear": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
            
            $ selected_girl.apply_impacts({"affection": (250, 750)})
        elif selected_girl.affection < 75:
            "[selected_girl] is completely focused on you, her eyes bright with interest."

            if selected_girl.corruption > 70:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750)})
            elif selected_girl.discipline > 70 and selected_girl.corruption < 40:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "discipline": (-750, -250)})
            elif selected_girl.fear > 50 and selected_girl.affection > 65:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (-750, -250)})
            elif selected_girl.naturism > 60 and selected_girl.discipline < 40:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750), "discipline": (250, 750)})
            elif selected_girl.intellect > 70 and selected_girl.corruption > 40:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "intellect": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
            
            $ selected_girl.apply_impacts({"affection": (250, 750)})
        else:
            "[selected_girl] looks at you with complete trust and affection."

            if selected_girl.discipline > 70 and selected_girl.corruption > 50:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750), "discipline": (-750, -250)})
            elif selected_girl.fear > 40 and selected_girl.affection > 80:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"fear": (-750, -250)})
            elif selected_girl.naturism > 70 and selected_girl.intellect > 70:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750), "intellect": (-750, -250)})
            elif selected_girl.corruption > 80:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750)})
            elif selected_girl.fear < 20 and selected_girl.discipline > 60:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750), "fear": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "affection_smalltalk", player)
                selected_girl.character "[_line]"
            
            # Diminishing returns at highest levels
            $ selected_girl.apply_impacts({"affection": (250, 750)})

    return
