# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu
    

##############################################################################
screen definition_say(who, what, side_image=None, two_window=False):
#This screen is used to create a custom screen for use with definitions
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has viewport
            draggable True
            mousewheel True
            scrollbars "vertical"
            ymaximum 800 xfill True yfill True
            yinitial 1.0

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

init python:
    shuffle_items = range(20)
   
    def shuffle_menu():
        global shuffle_items
        shuffle_items = range(20)
        shuffle_items.sort(key=lambda x:renpy.random.random())
        return
       
    def unshuffle_menu():
        global shuffle_items
        shuffle_items = range(20)
        return
        
screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for index in shuffle_items:
                if index < len(items):
                    $caption, action, chosen = items[index]
                    if action: 
                   
                        button:
                            action action
                            style "menu_choice_button"                       

                            text caption style "menu_choice"
                   
                    else:
                        text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        if persistent.lang == "francais":
            textbutton _("Commencer") action Start()
            textbutton _("Sauvegardes") action ShowMenu("load")
            textbutton _("Préférences") action ShowMenu("preferences")
            textbutton _("Langage") action Jump("language_chooser")
            textbutton _("Aide") action Help()
            textbutton _("Crédits") action Start("bil_credits")
            textbutton _("Quitter") action Quit(confirm=False)
        else:
            textbutton _("Start Game") action Start()
            textbutton _("Load Save") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Language") action Jump("language_chooser")
            textbutton _("Help") action Help()
            textbutton _("Credits") action Start("bil_credits")
            textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox
        
        if persistent.lang == "francais":
            textbutton _("Retour") action Return()
            textbutton _("Préférences") action ShowMenu("preferences")
            textbutton _("Sauvegarder") action ShowMenu("save")
            textbutton _("Sauvegardes") action ShowMenu("load")
            textbutton _("Menu principal") action MainMenu()
            textbutton _("Aide") action Help()
            textbutton _("Quitter") action Quit()
        else:
            textbutton _("Return") action Return()
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("Save Game") action ShowMenu("save")
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Main Menu") action MainMenu()
            textbutton _("Help") action Help()
            textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        if persistent.lang == "francais":
            hbox:
                style_group "file_picker_nav"

                textbutton _("Précédent"):
                    action FilePagePrevious()

                textbutton _("Auto"):
                    action FilePage("auto")

                textbutton _("Rapide"):
                    action FilePage("quick")

                for i in range(1, 9):
                    textbutton str(i):
                        action FilePage(i)

                textbutton _("Suivant"):
                    action FilePageNext()
        else:
            hbox:
                style_group "file_picker_nav"

                textbutton _("Previous"):
                    action FilePagePrevious()

                textbutton _("Auto"):
                    action FilePage("auto")

                textbutton _("Quick"):
                    action FilePage("quick")

                for i in range(1, 9):
                    textbutton str(i):
                        action FilePage(i)

                textbutton _("Next"):
                    action FilePageNext()
        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    
                    if persistent.lang == "francais":
                        $ file_time = FileTime(i, empty=_("Vide."))
                    else:
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                   
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox
                if persistent.lang == "francais":
                    label _("Affichage")
                    textbutton _("Fenêtre") action Preference("display", "window")
                    textbutton _("Plein écran") action Preference("display", "fullscreen")
                else:
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox
                if persistent.lang == "francais":
                    label _("Transitions")
                    textbutton _("Toutes") action Preference("transitions", "all")
                    textbutton _("Aucunes") action Preference("transitions", "none")
                else:
                    label _("Transitions")
                    textbutton _("All") action Preference("transitions", "all")
                    textbutton _("None") action Preference("transitions", "none")
                
            frame:
                style_group "pref"
                has vbox
                if persistent.lang == "francais":
                    label _("Vitesse du texte")
                else:
                    label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                if persistent.lang == "francais":
                    label _("Sauter")
                    textbutton _("Texte déjà vu") action Preference("skip", "seen")
                    textbutton _("Tout le texte") action Preference("skip", "all")
                else:
                    label _("Skip")
                    textbutton _("Seen Messages") action Preference("skip", "seen")
                    textbutton _("All Messages") action Preference("skip", "all")
                    
            frame:
                style_group "pref"
                has vbox
    
                if persistent.lang == "francais":
                    textbutton _("Débuter Sauter") action Skip()
                else:
                    textbutton _("Begin Skipping") action Skip()
                    
            frame:
                style_group "pref"
                has vbox

                if persistent.lang == "francais":
                    label _("Après les choix")
                    textbutton _("Arrêter de sauter") action Preference("after choices", "stop")
                    textbutton _("Continuer à sauter") action Preference("after choices", "skip")
                else:
                    label _("After Choices")
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                if persistent.lang == "francais":
                    label _("Avancement automatique")
                else:
                    label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                #if config.has_voice:
                    #textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox
                if persistent.lang == "francais":
                    label _("Volume — Musique")
                else:
                    label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                if persistent.lang == "francais":
                    label _("Volume — Sons")
                else:
                    label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            #if config.has_voice:
                #frame:
                    #style_group "pref"
                    #has vbox

                    #label _("Voice Volume")
                    #bar value Preference("voice volume")

                    #textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    #if config.sample_voice:
                        #textbutton _("Test"):
                            #action Play("voice", config.sample_voice)
                            #style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        if persistent.lang == "francais":
            if message == layout.MAIN_MENU:
                label _("Retourner au menu principal?\nCela fera perdre la progression en cours."):
                    xalign 0.5
            elif message == layout.DELETE_SAVE:
                label _("Êtes-vous sûr de vouloir supprimer cette sauvegarde?"):
                    xalign 0.5
            elif message == layout.OVERWRITE_SAVE:
                label _("Êtes-vous sûr de vouloir écraser cette sauvegarde?"):
                    xalign 0.5
            elif message == layout.LOADING:
                label _("Le chargement fera perdre la progression en cours.\nÊtes-vous sûr de vouloir faire cela?"):
                    xalign 0.5
            elif message == layout.QUIT:
                label _("Êtes-vous sûr de vouloir quitter?"):
                    xalign 0.5
            elif message == layout.END_REPLAY:
                label _("Êtes-vous sûr de vouloir arrêter le visionnement?"):
                    xalign 0.5
            else:
                label _("Voulez-vous procéder?"):
                    xalign 0.5
        else:
            label _(message):
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            if persistent.lang == "francais":
                textbutton _("Oui") action yes_action
                textbutton _("Non") action no_action
            else:
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        if persistent.lang == "francais":
            textbutton _("Retour") action Rollback()
            textbutton _("Sauver") action ShowMenu('save')
            textbutton _("R.Sauver") action QuickSave()
            textbutton _("R.Charger") action QuickLoad()
            textbutton _("Sauter") action Skip()
            textbutton _("R.Sauter") action Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Préfs") action ShowMenu('preferences')
        else:
            textbutton _("Back") action Rollback()
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Skip") action Skip()
            textbutton _("F.Skip") action Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        
        
        idle_color "#830000"
        hover_color "#ff6666"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
        
        #idle_color "#cc0"
        #hover_color "#830000"
        #selected_idle_color "#cc08"
        #selected_hover_color "#8888"
        #insensitive_color "#4448"
        
        #idle_color "#8888"
        #hover_color "#ff6666"
        #selected_idle_color "#cc08"
        #selected_hover_color "#cc0"
        #insensitive_color "#4448"



##############################################################################
# Body Parts
#
# A screen that displays an image map of body parts in the prologue
# One of the body parts lets players continue on.
screen body_parts:
    
    if persistent.lang == "francais":
        imagemap:
            auto "bdParts_%s.jpg"
            hotspot (159, 26, 152, 98) alt "un pied avec une bague autour d'un orteil" action Return("fail")
            hotspot (42, 124, 241, 183) alt "un morceau de bras attaché à un poing" action Return("fail")
            hotspot (283, 137, 158, 328) alt "un morceau de jambe attaché à un pied pointé vers le mur" action Return("fail")
            hotspot (406, 9, 149, 182) alt "une main. Il ne semble pas avoir une bague autour d'aucun des doigts" action Return("fail")
            hotspot (577, 139, 180, 116) alt "une autre main. Avec beaucoup de sang! Pourquoi tellement de sang?" action Return("fail")
            hotspot (540, 276, 142, 281) alt "un morceau d'un bras différent" action Return("fail")
            hotspot (426, 461, 128, 107) alt "une main" action Return("fail")
            hotspot (18, 318, 260, 262) alt "un morceau de bras attaché à une main dans une position relaxe. Il y a une bague autour d'un des doigts." action Return("win")
    else:
        imagemap:
            auto "bdParts_%s.jpg"
            hotspot (159, 26, 152, 98) alt "a foot with a ring around a toe" action Return("fail")
            hotspot (42, 124, 241, 183) alt "part of an arm attached to a hand curled into a fist" action Return("fail")
            hotspot (283, 137, 158, 328) alt "part of a leg attached to a flexed foot" action Return("fail")
            hotspot (406, 9, 149, 182) alt "a hand. There does not seem to be a ring around any of the fingers." action Return("fail")
            hotspot (577, 139, 180, 116) alt "another hand. Why so much blood?" action Return("fail")
            hotspot (540, 276, 142, 281) alt "part of a different arm" action Return("fail")
            hotspot (426, 461, 128, 107) alt "a hand" action Return("fail")
            hotspot (18, 318, 260, 262) alt "part of an arm attached to a relaxing hand. There is a ring around one of the fingers." action Return("win")
    
##############################################################################
# Unlock safe
#
# A screen that displays numbers that stand in for the alphabet
# Players try to unlock a code in chapter 1, see also pthJoint
screen unlock_safe:
   # tag menu
    imagemap:
        auto "safe_%s.jpg"
        hotspot (27, 34, 153, 124) alt "1" action Return("1")
        hotspot (186, 36, 154, 119) alt "2. A b c" action Return("2")
        hotspot (354, 35, 159, 125) alt "3. d e f"action Return("3")
        
        hotspot (20, 160, 160, 125) alt "4. g h i" action Return("4")
        hotspot (184, 157, 161, 138) alt "5. j k l" action Return("5")
        hotspot (351, 157, 167, 134) alt "6. m n o" action Return("6")
        
        hotspot (13, 288, 163, 128) alt "7. p q r s" action Return("7")
        hotspot (183, 291, 163, 128) alt "8. t u v" action Return("8")
        hotspot (354, 294, 167, 132) alt "9. w x y" action Return("9")
        
        hotspot (19, 419, 158, 134) alt "*" action Return("*")
        hotspot (183, 418, 167, 144) alt "0" action Return("0")
        hotspot (356, 429, 173, 132) alt "#" action Return("#")
    
    
    frame:
        style_group "mm"
        xalign .91
        yalign .20
        
        label _(safeWord)
        
    frame:
        style_group "mm"
        xalign .91
        yalign .85
        
        label _(myWordString)
    
    frame:
        style_group "mm"
        xalign .91
        yalign .80

        has vbox
        #Only show the buttons after 2 attempts
        #Once we start clicking on numbers, remove the buttons - they are not wanted at the moment
        if flagCount >=2 and len(mySafeString) <=0:
            if chMenu1 == False:
                textbutton _([safeButtonLists[safeIC][0]]):
                    action [SetVariable("chMenu1", True), SetVariable("mySafeString", safeButtonLists[safeIC][0]), Jump("fr_safe_check_list")]
            if chMenu2 == False:
                textbutton _([safeButtonLists[safeIC][1]]):
                    action [SetVariable("chMenu2", True), SetVariable("mySafeString", safeButtonLists[safeIC][1]), Jump("fr_safe_check_list")]
            if chMenu3 == False:
                textbutton _([safeButtonLists[safeIC][2]]):
                    action [SetVariable("chMenu3", True), SetVariable("mySafeString", safeButtonLists[safeIC][2]), Jump("fr_safe_check_list")]
            if chMenu4 == False:
                textbutton _([safeButtonLists[safeIC][3]]):
                    action [SetVariable("chMenu4", True), SetVariable("mySafeString", safeButtonLists[safeIC][3]), Jump("fr_safe_check_list")]
        label _(mySafeString)
