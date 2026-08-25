# Narrator dialog labels. Usage: renpy.call("vt_fetish_dialog", dialogtext=f"...")

label vt_fetish_dialog(dialogtext=dialogtext):

    "[dialogtext]"

    return

# Her spoken reaction (as selected_girl == the acted-on girl) for the penetration->oral (ATM) beat.
label vt_atm_reaction(line=""):

    selected_girl.character "[line]"

    return

label vt_condom_dialog(dialogtext=dialogtext):
    
    "[dialogtext]"

    return

label vt_broken_condom_dialog(dialogtext=dialogtext):
    
    "[dialogtext]"

    return

label vt_raw_dialog(dialogtext=dialogtext):
    
    "[dialogtext]"

    return