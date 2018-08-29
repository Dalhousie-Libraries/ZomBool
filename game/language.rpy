#Contains scenes and a few options that make the language switching work. Screens.rpy and options.rpy contain a few extras

init -3 python:
    #Starts by checking whether or not a default language was assigned to this game.
    if persistent.lang is None:
        persistent.lang = "english"

    lang = persistent.lang

#If no language has ever been picked, the splashscreen forces a pick
label splashscreen:
    
    if not persistent.chose_lang:
        $persistent.chose_lang = True
        jump language_chooser
        
    scene black
    with Pause(1)
    if lang == "english":
        show text "WARNING: contains graphic depictions of blood and body parts.{vspace=20}Click to continue.{vspace=50}" with dissolve
    else:
        show text "ATTENTION: comprend des scènes où l'on peut voir du sang et des morceaux de corps.{vspace=20}Cliquez l'écran pour continuer." with dissolve
    $renpy.pause(1000)
    hide text with dissolve

    return

#If no language has ever been picked...pick a language.
label language_chooser:
    scene black
    
    $unshuffle_menu()
    menu:
        "English":
            $persistent.lang = "english"
        "Français":
            $persistent.lang = "francais"
        
    $renpy.utter_restart()
    return

#Refuses to load a save file in a different language.
label after_load:
    if lang == game_lang:
        return

    if lang == "english":
        "Can't load this file — the language of this save file is not the current selected language."
    elif lang == "francais":
        "Impossible de charger ce fichier — le fichier de sauvegarde a été enregistré dans une langue différente que celle présentement sélectionnée."

    $ renpy.full_restart()
    
    return

#Send to the right path depending on language
label language_path:
    $game_lang = lang
    
    #Send to the right path depending on language
    if lang == "english":
        jump en_start
    else:
        jump fr_debut
    return