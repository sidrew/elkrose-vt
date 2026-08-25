label vt_small_talk_fear:
    "You bring up some topics as thinly veiled threats trying to scare her."

    if selected_girl.fear < 15:
        "[selected_girl] looks confused and unbothered."

        if selected_girl.discipline > 70:
            $ _line = vt_say(selected_girl, "fear_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"discipline": (-750, -250)})
        elif selected_girl.corruption > 60:
            $ _line = vt_say(selected_girl, "fear_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"corruption": (-750, -250)})
        elif selected_girl.intellect > 70:
            $ _line = vt_say(selected_girl, "fear_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"intellect": (250, 750)})
        elif selected_girl.affection > 40:
            $ _line = vt_say(selected_girl, "fear_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"affection": (-750, -250)})
        elif selected_girl.naturism > 60:
            $ _line = vt_say(selected_girl, "fear_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"naturism": (-750, -250)})
        else:
            $ _line = vt_say(selected_girl, "fear_smalltalk", player)
            selected_girl.character "[_line]"
        
    else:
        if selected_girl.fear < 30:
            "[selected_girl] looks slightly nervous but tries to hide it."

            if selected_girl.discipline > 50:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 40:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.affection > 30:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (-750, -250)})
            elif selected_girl.intellect > 60:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
        elif selected_girl.fear < 45:
            "[selected_girl] looks uncomfortable, her composure starting to crack."

            if selected_girl.discipline > 40:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 50:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.affection > 40:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (-750, -250)})
            elif selected_girl.fear > 35 and selected_girl.intellect > 50:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250), "fear": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
        elif selected_girl.fear < 60:
            "[selected_girl] looks visibly worried and anxious."

            if selected_girl.discipline > 30:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 40:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.affection > 50:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (-750, -250)})
            elif selected_girl.intellect > 50:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
        elif selected_girl.fear < 75:
            "[selected_girl] looks frightened, her hands trembling slightly."

            if selected_girl.discipline > 20:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 50:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750)})
            elif selected_girl.affection > 60:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            elif selected_girl.intellect < 40:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
        else:
            "[selected_girl] looks terrified and on edge."

            if selected_girl.discipline > 10:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (-750, -250)})
            elif selected_girl.corruption > 60:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.affection > 70:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            elif selected_girl.naturism > 50:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "fear_smalltalk", player)
                selected_girl.character "[_line]"
            
        # At highest fear levels, discipline might start to crack
        $ selected_girl.apply_impacts({"fear": (250, 750), "discipline": (250, 750), "affection": (-750, -250)})

    return

label vt_small_talk_fear_lower:
    "You bring up some topics in an attempt to appear less intimidating."

    if selected_girl.fear > 85:
        "[selected_girl] looks terrified and on edge."

        if selected_girl.discipline > 50:
            $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"discipline": (-750, -250)})
        elif selected_girl.corruption > 60:
            $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"corruption": (-750, -250)})
        elif selected_girl.affection < 30:
            $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"affection": (-750, -250), "fear": (-750, -250)})
        elif selected_girl.intellect > 60:
            $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"intellect": (-750, -250)})
        elif selected_girl.fear > 90:
            $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
            selected_girl.character "[_line]"
            $ selected_girl.apply_impacts({"fear": (250, 750)})
        else:
            $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
            selected_girl.character "[_line]"

        $ selected_girl.apply_impacts({"fear": (-750, -250), "affection": (250, 750), "discipline": (-750, -250)}) 
    else:
        if selected_girl.fear > 70:
            "[selected_girl] looks slightly less nervous."

            if selected_girl.discipline > 40:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750)})
            elif selected_girl.corruption > 50:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.affection > 40:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            elif selected_girl.intellect > 50:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
            
        elif selected_girl.fear > 55:
            "[selected_girl] looks visibly less worried and anxious."

            if selected_girl.discipline > 30:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750)})
            elif selected_girl.corruption > 40:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750)})
            elif selected_girl.affection > 50:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            elif selected_girl.intellect < 50:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
            
        elif selected_girl.fear > 40:
            "[selected_girl] looks more relaxed around you."

            if selected_girl.discipline > 20:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750)})
            elif selected_girl.corruption > 30:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (250, 750)})
            elif selected_girl.affection > 60:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            elif selected_girl.intellect > 50:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
            
        elif selected_girl.fear > 25:
            "[selected_girl] looks considerably more comfortable in your presence."

            if selected_girl.discipline > 10:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750)})
            elif selected_girl.corruption > 20:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.affection > 70:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            elif selected_girl.naturism > 50:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"naturism": (250, 750)})
            else:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
            
        else:
            "[selected_girl] looks relaxed and comfortable around you."

            if selected_girl.discipline > 0:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"discipline": (250, 750)})
            elif selected_girl.corruption > 10:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"corruption": (-750, -250)})
            elif selected_girl.affection > 80:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"affection": (250, 750)})
            elif selected_girl.intellect > 50:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
                $ selected_girl.apply_impacts({"intellect": (-750, -250)})
            else:
                $ _line = vt_say(selected_girl, "fear_lower_smalltalk", player)
                selected_girl.character "[_line]"
            
        # At lowest fear levels, discipline decreases as she feels more secure
        $ selected_girl.apply_impacts({"fear": (-750, -250), "affection": (250, 750), "discipline": (-750, -250)})
       

    return
