#Contains initial variables, including character setup
init -3 python:
    #Establish some random numbers to use in alternate menu choices
    if persistent.mySeed2 is None:
        persistent.mySeed2 = renpy.random.randint(0, 1)
    
    if persistent.mySeed2alt is None:
        persistent.mySeed2alt = renpy.random.randint(0,1)
        
    if persistent.mySeed3 is None:
        persistent.mySeed3 = renpy.random.randint(0,2)
        
    if persistent.mySeed3alt is None:
        persistent.mySeed3alt = renpy.random.randint(0,2)

init:
    # Declare images used for characters in this game
    image Eva pensive = "Eva_pensive.png"
    image Eva mwahaha = "Eva_mwaha.png"
    image Eva determ = "Eva_determin.png"
    image Eva satisfaction = "Eva_satisfaction.png"
    image Eva flashback = im.Grayscale("Eva_determin.png")
    image Eva factorscale = im.FactorScale("Eva_mwaha.png", 0.75, 0.75)
    
    image Librarian neutral = "Librarian_neutral.png"
    image Librarian intense = "Librarian_intense.png"
    image Librarian smiling = "Librarian_smiling.png"
    image Librarian factorscale = im.FactorScale("Librarian_smiling.png", 0.75, 0.75)
    
    image Creature neutral = "Creature.png"
    image Creature factorscale = im.FactorScale("Creature.png", 0.75, 0.75)
    
    image Reception obssessed = "Reception_obssessed.png"
    image Reception passion = "Reception_passion.png"
    image Reception stars = "Reception_stars.png"
    image Reception neutral = "Reception_neutral.png"
    image Reception happy = "Reception_happy.png"
    image Reception factorscale = im.FactorScale("Reception_stars.png", 0.75, 0.75)
    
    image Pharma afraid = "Pharma_afraid.png"
    image Pharma terrified = "Pharma_terrified.png"
    image Pharma relieved = "Pharma_relieved.png"
    image Pharma happy = "Pharma_happy.png"
    image Pharma factorscale = im.FactorScale("Pharma_terrified.png", 0.75, 0.75)
    
    image Proprio unhappy = "Proprio_unhappy.png"
    image Proprio drill = "Proprio_drill.png"
    image Proprio happy = "Proprio_happy.png"
    image Proprio satisfaction = "Proprio_satisfaction.png"
    image Proprio factorscale = im.FactorScale("Proprio_drill.png", 0.75, 0.75)
    
    image Employee afraid = "Employee_afraid.png"
    image Employee determination = "Employee_determination.png"
    image Employee neutral = "Employee_neutral.png"
    image Employee factorscale = im.FactorScale("Employee_determination.png", 0.75, 0.75)
    
    image Client intense = "Client_intense.png"
    image Client happy = "Client_happy.png"
    image Client trickster = "Client_trickster.png"
    image Client factorscale = im.FactorScale("Client_intense.png", 0.75, 0.75)
    
    #puzzle pieces
    if lang == "english":
        image puzzle1 = "en_puzzle1.png"
        image puzzle2 = "en_puzzle2.png"
        image puzzle3 = "en_puzzle3.png"
        image puzzle4 = "en_puzzle4.png"
    else:
        image puzzle1 = "fr_puzzle1.png"
        image puzzle2 = "fr_puzzle2.png"
        image puzzle3 = "fr_puzzle3.png"
        image puzzle4 = "fr_puzzle4.png"
    
    #form pictures
    image sport1 = "badminton.png"
    image sport2 = "pickleball.png"
    image sport4 = "pingpong.png"
    image sport3 = "tennis.png"
    if lang == "english":
        image form = "form_blank.jpg"
        image color1 = "blue.png"
        image facial1 = "glasses.png"
        image facial2 = "goatee.png"
    else:
        image form = "fr_form_blank.jpg"
        image color1 = "bleu.png"
        image facial1 = "lunette.png"
        image facial2 = "casquette.png"
        
    #demo form pictures
    image province = "province.png"
    if lang == "english":
        image teen1 = "adolescence.png"
        image teen2 = "teen.png"
        image teen3 = "teenager.png"
        image teen4 = "youth.png"
        image child1 = "child.png"
        image child2 = "children.png"
        image child3 = "kid.png"
        image child4 = "toddler.png"
        image provNB1 = "new_brunswick.png"
        image provNB2 = "new_brunswickian.png"
        image provNS1 = "nova_scotia.png"
        image provNS2 = "nova_scotian.png"
        image children = "child.png"
        image teenage = "teenager.png"
    else:
        image teen1 = "ado.png"
        image teen2 = "adolescence.png"
        image teen3 = "adolescent.png"
        image teen4 = "teen.png"
        image child1 = "enfance.png"
        image child2 = "enfant.png"
        image child3 = "children.png"
        image child4 = "kid.png"
        image provNB1 = "nouveau_brunswick.png"
        image provNB2 = "new_brunswick.png"
        image provNS1 = "nouvelle_ecosse.png"
        image provNS2 = "nova_scotia.png"
        image children = "enfant.png"
        image teenage = "adolescence.png"
        
    
    #inventory pictures
    if lang == "english":
        image inventory = "en_inventory.jpg"
    else:
        image inventory = "fr_inventory.jpg"
    
    #Venn Diagram pictures
    image Venn0 = im.FactorScale("Venn0.png", 1.35, 1.35)
    image Venn1 = im.FactorScale("Venn1.png", 1.35, 1.35)
    image Venn2 = im.FactorScale("Venn2.png", 1.35, 1.35)
    image Venn3 = im.FactorScale("Venn3.png", 1.35, 1.35)
    image Venn4 = im.FactorScale("Venn4.png", 1.35, 1.35)
    
    #images for main menu screen
    image creepyroom flashback = im.Grayscale("creepyRoom.jpg")
    
    image creepyroom invert = im.MatrixColor("creepyRoom.jpg",
                                       [ -1,  0,  0, 0, 1,
                                          0, -1,  0, 0, 1,
                                          0,  0, -1, 0, 1,
                                          0,  0,  0, 1, 0, ])
    
    image creepyroom flip = im.Flip("creepyRoom.jpg", vertical = True)
    
    image creepyroom composite = im.Composite(
    (959, 639),
    (0, 0), "creepyRoom.jpg",
    (150, 373), "shadow.png",
    (748, 239), "splatter.png")
    
    image creepyroom normal = "creepyRoom.jpg"

    image creepyroom animated:
        "creepyroom normal"
        pause 2.5
        choice:
            "creepyroom composite" with Dissolve(3)
            pause 6.5
        choice:
            "creepyroom normal" with Dissolve(3)
            pause 2
        choice:
            "creepyroom flashback" with Dissolve(3)
            pause 17
        choice:
            "creepyroom invert" with Dissolve(1.5)
            pause 13
        choice:
            "creepyroom flashback" with Dissolve(3)
            pause 14
        choice:
            "creepyroom composite" with Dissolve(3)
            pause 13
        choice:
            "creepyroom flip"
            pause 3
        choice:
            "creepyroom invert" with Dissolve(1.5)
            pause 16
        repeat
    
    #Rain effect
    image rain = SnowBlossom("blood.png", count=30, border=150, xspeed=(10,40), yspeed=(10,80), start=4, fast=False, horizontal=False)

    # Declare characters used by this game.
    define g = Character('Gabriel', color="#FFFF00")
    define e = Character('Évangeline', color="#c8ffc8")
    define b = Character("librarian_name", dynamic = True, color="#00FFFF")
    define cl = Character("class_name", dynamic = True, color = "#408080")
    define cli = Character("impatient_name", dynamic = True, color = "#40C0C0")
    define c = Character('creature_name', dynamic = True,color = "#8080C0")
    define r = Character('reception_name', dynamic = True,color = "#C0C0FF")
    define p = Character('pharmacist_name', dynamic = True, color = "#C0C0FF")
    define s = Character('sportsGo_name', dynamic = True, color = "#C0C0FF")
    define em = Character('employee_name', dynamic = True, color = "#FFC000")
    define an = Character('client_name', dynamic = True, color = "#FFC0C0")
    define ro = Character('robot_name', dynamic = True, color = "#FFC0C0")
    define narrator = Character(what_prefix = '{i}', what_suffix = '{/i}')

    #Keep track of chosen path in Chapter 1
    $chosenPath = ""
    
    #The character 'definition' calls a special screen used to create definitions of concepts encountered in the game
    $definition = Character(None, screen="definition_say", window_yfill=True, window_xmargin=20, 
        window_ymargin=20, window_background=Solid((0, 0, 0, 192)))
    
    #The book style used for book titles
    $style.book = Style(style.default)
    $style.book.color = "#C080FF"
    $style.book.italic = True
    
    #The bool style used for boolean operators
    $style.bool = Style(style.default)
    $style.bool.color = "#C0FFFF"
    
    #The word style used for significant words
    $style.word = Style(style.default)
    $style.word.color = "#8080FF"
    
    #The venn style used for displayed words in the venn diagrams
    $style.venn = Style(style.default)
    $style.venn.color = "#FFFFC0"
    
    #Gives a nice centered window-less text with an outline
    $titleCard= Character(None,
                        what_outlines=[(3, "#0008", 2, 2), (3, "#282", 0, 0)],
                        what_layout="subtitle",
                        what_xalign=0.5,
                        what_yalign=0.5,
                        what_text_align=0.5,
                        window_background=None,
                        window_yminimum=0,
                        window_xfill=False,
                        window_xalign=0.5,
                        window_yalign=0.5,
                        what_slow_cps=8)
    
    #Backgrounds used in ZomBool
    image bg creepyRoom = "creepyRoom.jpg"
    image bg creepyRoomFlashback = im.Sepia("creepyRoom.jpg")
    image bg classroom = "classroom.jpg"
    image bg creepyOffice = "creepyOffice.jpg"
    image bg receptionCharlie = "reception.jpg"
    image bg roomCharlie = "passageway.jpg"
    image bg street = "street.jpg"
    image bg bakery = "bakery.jpg"
    image bg pharmacy = "pharmacy.jpg"
    image bg sportsGo = "sportsGo.jpg"
    image bg electro = "electro.jpg"
    image bg electro2 = "electro2.jpg"
    image bg electro3 = "electro3.jpg"
    image bg safe = "safe_ground.jpg"
    
    
    #Form position
    $formPos = Position(xpos=0.0, xanchor=0.0, ypos=0.0, yanchor=0.0)
    $formPos1 = Position(xpos=93, ypos = 80, xanchor = 0.5, yanchor = 0.5)
    $formPos2 = Position(xpos=299, ypos=80, xanchor = 0.5, yanchor = 0.5)
    $formPos3 = Position(xpos=496, ypos=80, xanchor = 0.5, yanchor = 0.5)
    $formPos4 = Position(xpos=699, ypos=80, xanchor = 0.5, yanchor = 0.5)
    $formPos5 = Position(xpos=93, ypos =174, xanchor = 0.5, yanchor = 0.5)
    $formPos6 = Position(xpos=299, ypos=174, xanchor = 0.5, yanchor = 0.5)
    $formPos7 = Position(xpos=496, ypos=174, xanchor = 0.5, yanchor = 0.5)
    $formPos8 = Position(xpos=699, ypos=174, xanchor = 0.5, yanchor = 0.5)
    $formPos9 = Position(xpos=93, ypos=295, xanchor = 0.5, yanchor = 0.5)
    $formPos10 = Position(xpos=299, ypos=295, xanchor = 0.5, yanchor = 0.5)
    $formPos11 = Position(xpos=496, ypos=295, xanchor = 0.5, yanchor = 0.5)
    $formPos12 = Position(xpos=699, ypos=295, xanchor = 0.5, yanchor = 0.5)
    $formPos13 = Position(xpos=93, ypos=415, xanchor = 0.5, yanchor = 0.5)
    $formPos14 = Position(xpos=299, ypos=415, xanchor = 0.5, yanchor = 0.5)
    $formPos15 = Position(xpos=496, ypos=415, xanchor = 0.5, yanchor = 0.5)
    $formPos16 = Position(xpos=699, ypos=415, xanchor = 0.5, yanchor = 0.5)
    $formPos17 = Position(xpos=93, ypos=500, xanchor = 0.5, yanchor = 0.5)
    $formPos18 = Position(xpos=299, ypos=500, xanchor = 0.5, yanchor = 0.5)
    $formPos19 = Position(xpos=496, ypos=500, xanchor = 0.5, yanchor = 0.5)
    $formPos20 = Position(xpos=699, ypos=500, xanchor = 0.5, yanchor = 0.5)

    #Venn diagram position
    $venTop = Position(xalign=0.5, yalign=0.0)
    
    #Venn words position
    $venWord = Position(xpos = 0.2, xanchor=0.0, ypos=0.15, yanchor=0.0)
    
    #4 on-screen characters positions.
    $leftMid = Position(xpos = 0.2, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    $rightMid = Position(xpos = 0.4, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)  
    $leftAway = Position(xpos = 0.0, xanchor = 0.1, ypos = 1.0, yanchor = 1.0)
    $rightAway = Position(xpos = 1.0, xanchor = 0.9, ypos=1.0, yanchor = 1.0)
    
    #characters positions for credits
    $credPos1 = Position(xpos = 0.0, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    $credPos2 = Position(xpos = 0.1, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    $credPos3 = Position(xpos = 0.2, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    $credPos4 = Position(xpos = 0.3, xanchor = 1.0, ypos = 1.0, yanchor = 1.0)
    $credPos5 = Position(xpos = 0.4, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    $credPos6 = Position(xpos = 0.5, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    $credPos7 = Position(xpos = 0.6, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    $credPos8 = Position(xpos = 0.7, xanchor = 0.0, ypos = 1.0, yanchor = 1.0)
    
    #Initial Puzzle Positions - can be used no matter the size
    $combine1 = Position(xpos = 0.2, xanchor = 0.5, ypos = 0.2, yanchor = 0.5)
    $combine2 = Position(xpos = 0.8, xanchor = 0.5, ypos = 0.2, yanchor = 0.5)
    $combine3 = Position(xpos = 0.2, xanchor = 0.5, ypos = 0.55, yanchor = 0.5)
    $combine4 = Position(xpos = 0.8, xanchor = 0.5, ypos = 0.55, yanchor = 0.5)
    
    #Having the puzzle pieces combine in the center
    transform combine_center1:
        linear 0.3 xpos 0.655 ypos 0.55
        
    transform combine_center2:
        linear 0.3 xpos 0.4 ypos 0.55
        
    transform combine_center3:
        linear 0.3 xpos 0.655 ypos 0.313
        
    transform combine_center4:
        linear 0.3 xpos 0.4 ypos 0.315
        
    #Credit text
    $credit_text1 = Position(xpos = 0.2, ypos = 0.3)
    $credit_text2 = Position(xpos = 0.5, ypos = 0.1)
    $credit_text3 = Position(xpos = 0.2, ypos = 0.2)
    $credit_text4 = Position(xpos = 0.5, ypos = 0.35)
    $credit_text5 = Position(xalign = 0.5, yalign = 0.5)

    #This ATL takes a picture and makes it move out the bottom right (used for getting Évangeline in the basement)
    transform my_out:
        pause 0.3
        linear 1.0 xpos 0.8 yanchor 0.0 ypos 1.0
        
    #This position makes characters start at my_out
    $my_out_init = Position(xpos = 0.8, xanchor = 0.0, ypos = 1.0, yanchor = 0.0)
    $my_out_init_buffer = Position(xpos = 0.9, xanchor = 0.0, ypos = 1.0, yanchor = 0.0)
    $stageRight = Position(xpos = 1.0, xanchor = 0.0, ypos=1.0, yanchor = 0.0)
    $otherStageRight = Position(xpos=1.0, xanchor = 0.0, ypos=0.5, yanchor =0.5)


label initial_variables:  
    #Shuffle the random seeds so that every new game uses different menu options   
    if mySeed2 == 0:
        $persistent.mySeed2 = 1
    else:
        $persistent.mySeed2 = 0
        
    if mySeed2alt == 0:
        $persistent.mySeed2alt = 1
    else:
        $persistent.mySeed2alt = 0
        
    if mySeed3 == 0:
        $persistent.mySeed3 = 1
    elif mySeed3 == 1:
        $persistent.mySeed3 = 2
    else:
        $persistent.mySeed3 = 0
        
    if mySeed3alt == 0:
        $persistent.mySeed3alt = 1
    elif mySeed3alt == 1:
        $persistent.mySeed3alt = 2
    else:
        $persistent.mySeed3alt = 0

    $renpy.save_persistent()
    return
    
#Resets the choice trackers used at various points
label choixMenu:
    $chMenu1 = False
    $chMenu2 = False
    $chMenu3 = False
    $chMenu4 = False
    $chMenu5 = False
    $chMenu6 = False
    $chMenu7 = False
    $chMenu8 = False
    $chMenu9 = False
    $chMenu10 = False
    
    $flagCount = 0
    $flag2 = 0
    $flag3 = 0
    
    $victoryFlag = False
    
    return

#Resets the list and variables used to alternate the keywords used in the game
label cleanMadGab:
    $myList = ""
    $entry1 = ""
    $entry2 = ""
    $entry3 = ""
    $entry4 = ""
    $entry5 = ""
    $entry6 = ""
    $entry7 = ""
    $entry8 = ""
    $entry9 = ""
    
    return
    
#Removes a victory point if not already removed during exercise
label victoryLost:
    play sound "Blop.mp3"
    if not victoryFlag:
        $victory -=1
        $victoryFlag = True
    
    return
    
label victoryWon:
    queue sound "A_Tone.mp3"
    $victory += 1
    
    return
    
label victoryReset:
    $victoryFlag = False
    return