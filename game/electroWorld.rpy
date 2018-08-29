label fr_elect_trans:
    
    call sc_black from _call_sc_black_4
    
    #If we brought a friend, change simple sentences accordingly - flag2 is the index to the list
    if companion:
        $flag2 = 1
    else:
        $flag2 = 0
        
    $myList = (("je l'ai", "Laisse-moi", "t'", "Donne", "J'ai"),
        ("on l'a", "Laisse-nous", "vous ", "Donnez", "On a"))
    
    #Loading the list in variables for easier retrieval inside Renpy strings
    $entry1 = myList[flag2][0]
    $entry2 = myList[flag2][1]
    $entry3 = myList[flag2][2] 
    $entry4 = myList[flag2][3]
    $entry5 = myList[flag2][4]

    "À la demande d'Évangeline, [entry1] accompagnée jusqu'au ÉlectroCoutu le plus près de chez elle."
    titleCard "Chapitre 2 de 2{vspace=30}Magasinez à ÉlectroCoutu pour tous vos besoins en électronique!"
    stop music fadeout 3
    
    #Setup everyone on stage  
    call ms_machine from _call_ms_machine
    call sc_electro from _call_sc_electro
    
    
    sv "Évangeline entre dans le magasin."
    show Eva pensive at center with moveinright
    
    #If companion, also have them appear
    if companion:
        if chosenPath == "Charlie":
            sv "Le réceptioniste la suit."
            show Reception neutral at right with moveinright
        elif chosenPath == "Pharmacy":
            sv "Le pharmacien la suit."
            show Pharma afraid at rightAway with moveinright
        else:
            sv "La propriétaire la suit."
            show Proprio satisfaction at right with moveinright
    
    play sound "Light_Bulb.mp3"
    "CRACK!"
    "Les lumières sont fermées et la porte est complètement défoncée. On a réussi à entrer facilement mais j'ai marché sur des morceaux de verre!"

    sv "Un employé du magasin court rapidement vers votre groupe."
    show Employee afraid at left with moveinleft
    em "Ahhh! Je vous entends! Qui est là? J'avais oublié de barrer la porte??? Vous êtes des zombies ou des gens?"
    
    g "On n'est pas des zombies!"
    show Eva satisfaction

    #Companions react to employee arrival
    if companion:
        if chosenPath == "Charlie":
            show Reception passion
            r "Nous sommes des êtres humains...et des artistes!"
        elif chosenPath == "Pharmacy":
            show Pharma relieved
            p "{size=-4}Je ne suis {i}probablement{/i} pas un zombie...{/size}"
        else:
            show Proprio drill
            s "On est ici pour DÉMOLIR les zombies!"
            
    sv "Une personne bizarre se joint à votre groupe."
    $client_name = "Cliente???"
    an "Moi, je suis simplement..."
    
     #Companions react to client appearance
    if companion:
        show Employee afraid
        show Client trickster at rightMid with moveinbottom
        show Eva pensive at leftMid with move
        
        if chosenPath == "Charlie":
            show Reception obssessed
        elif chosenPath == "Pharmacy":
            show Pharma terrified
        else:
            show Proprio unhappy
    else:
        show Client trickster at right with moveinbottom
        show Eva pensive
        
    an "...une cliente enthousiaste!"
    
    em "Ahhh! La porte a été démolie! Qui a fait ça? Ce sont les zombies? Ils sont dans le magasin?"
    show Client intense
    an "Désolé, c'était verrouillé et je voulais vraiment venir jeter un coup d'oeil à vos nouveautés. Et peut-être repartir avec une télévision ou deux."
    show Employee determination
    
    show Eva determ
    e "NOUS, on est ici pour sauver la ville des zombies! On n'est pas avec elle."
    show Eva satisfaction
    e "Je suis Évangeline."
    g "Gabriel."
    
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
            r "Wilfred le 1er. Artiste."
        elif chosenPath == "Pharmacy":
            show Pharma afraid
            p "Je suis Joey, juste Joey, pas 'Zombie Joey'."
        else:
            show Proprio satisfaction
            s "Viola. Enchantée..."
    
    show Client trickster
    $client_name = "Antonine"
    an "Antonine. Oui. C'est un bon nom..."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    "..."
    
    show Employee neutral
    em "Roméo. Pas de blagues svp, je les ai toutes entendues."
    $employee_name = "Roméo"
    
    return

label en_elect_trans:
    
    call sc_black from _call_sc_black_5
    
    #If we brought a friend, change simple sentences accordingly - flag2 is the index to the list
    if companion:
        $flag2 = 1
    else:
        $flag2 = 0
        
    $myList = (("I", "Laisse-moi", "t'", "Donne", "J'ai"),
        ("we", "Laisse-nous", "vous ", "Donnez", "On a"))
    
    #Loading the list in variables for easier retrieval inside Renpy strings
    $entry1 = myList[flag2][0]
    $entry2 = myList[flag2][1]
    $entry3 = myList[flag2][2] 
    $entry4 = myList[flag2][3]
    $entry5 = myList[flag2][4]

    "Évangeline suggested that [entry1] accompany her to the nearest ElectricMart."
    titleCard "Chapter 2 of 2{vspace=30}Shop at ElectricMart for all of your electronic needs!"
    stop music fadeout 3
    
    #Setup everyone on stage  
    call ms_machine from _call_ms_machine_1
    call sc_electro from _call_sc_electro_1
    
    sv "Évangeline comes into the store."
    show Eva pensive at center with moveinright
    
    #If companion, also have them appear
    if companion:
        if chosenPath == "Charlie":
            sv "She is followed by the receptionist."
            show Reception neutral at right with moveinright
        elif chosenPath == "Pharmacy":
            sv "She is followed by the pharmacist."
            show Pharma afraid at rightAway with moveinright
        else:
            sv "She is followed by the sports store owner."
            show Proprio satisfaction at right with moveinright

    play sound "Light_Bulb.mp3"
    "CRACK!"
    "The lights are off and the door has been demolished. We get in easily enough, but I walk on some glass shards."

    sv "An employee of the store runs to your group."
    show Employee afraid at left with moveinleft
    em "Ahhh! I can hear you! Who's there? I forgot to lock the door??? Are you zombies or people?"
    
    g "We're not zombies!"
    show Eva satisfaction
    
    #Companions react to employee arrival
    if companion:
        if chosenPath == "Charlie":
            show Reception passion
            r "We're artists and human beings!"
        elif chosenPath == "Pharmacy":
            show Pharma relieved
            p "{size=-4}I'm {i}probably{/i} not a zombie...{/size}"
        else:
            show Proprio drill
            s "We're here to DEFEAT the zombies!"
            
    sv "A weird-looking person joins your group."
    $client_name = "Suspicious Client"
    an "I'm simply..."
    
     #Companions react to client appearance
    if companion:
        show Employee afraid
        show Client trickster at rightMid with moveinbottom
        show Eva pensive at leftMid with move
        
        if chosenPath == "Charlie":
            show Reception obssessed
        elif chosenPath == "Pharmacy":
            show Pharma terrified
        else:
            show Proprio unhappy
    else:
        show Client trickster at right with moveinbottom
        show Eva pensive

    an "...an enthusiastic client of ElectricMart!"
    
    em "Ahhh! The door is a mess! Who broke down the door? The zombies? Are they in the store?"
    show Client intense
    an "Sorry, the door was locked and I really wanted to take a look at your new arrivals. And maybe leave with a television or two."
    show Employee determination
    
    show Eva determ
    e "Well, we're not with her. We're here to save the city from the zombies!"
    show Eva satisfaction
    e "I'm Évangeline."
    g "Gabriel."
    
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
            r "Wilfred the 1st. Artist."
        elif chosenPath == "Pharmacy":
            show Pharma afraid
            p "I'm Joey, juste Joey, not 'Zombie Joey'."
        else:
            show Proprio satisfaction
            s "Viola. Nice to meet you..."
    
    show Client trickster
    $client_name = "Antonine"
    an "Antonine. Yep. That's my own, very real name..."
    sv "A silent beat. Click twice to continue."
    "..."
    
    show Employee neutral
    em "Romeo. Please don't make any jokes, I've heard them all."
    $employee_name = "Romeo"
    
    return
    
label fr_elect_plan:
         
    g "Évangeline a un plan pour nous sauver des zombies."
    show Eva mwahaha
    e "Oui. On va...{size=26}chercher la solution sur internet!{/size}"
    
    #Reaction to internet search
    if companion:
        if chosenPath == "Charlie":
            show Reception stars
        elif chosenPath == "Pharmacy":
            show Pharma happy
        else:
            show Proprio happy
            
    show Employee neutral
    show Client happy
    
    em "...mais on n'a pas d'électricité."
    
    #Reaction to no electricity
    if companion:
        if chosenPath == "Charlie":
            show Reception passion
        elif chosenPath == "Pharmacy":
            show Pharma afraid
        else:
            show Proprio unhappy
    
    show Client intense
    
    an "C'est pour ça qu'ils sont ici! ÉlectroCoutu a de nombreux produits qui fonctionnent même pendant une panne d'électricité."
    show Eva determ
    e "Internet par satellite? Comme utilise l'armée et les clubs de yachts? Et des batteries avec chargeurs USB?"
    an "Je recommende l'{i}Ami Satellite 1002 Yay{/i} en stock dans ce magasin. Les batteries sont dans l'allée 3."
    
    if kitten:
        an "Le logo officiel de la compagnie est un adorable petit chaton — vous ne pouvez pas le manquer!"
    
    show Employee afraid
    em "Vous ne pouvez pas juste voler notre stock! Ils vont me mettre à la porte!"
    
    show Client trickster
    an "Roméo, tu nous laisses emprunter de l'équipement et en échange on va te défendre des zombies qui essaient d'entrer."
    em "QUOI?"
    "On a regardé vers la porte. Des zombies sont sur le point d'entrer dans l'ÉlectroCoutu!"
    
    #Reaction to zombies entering the store
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
        elif chosenPath == "Pharmacy":
            show Pharma terrified
        else:
            show Proprio drill
    
    em "Ahh!"
    
    show Eva determ
    e "Pas de panique. On va bloquer cette porte de notre mieux, puis on va sortir par une autre porte pour surprendre et attaquer les zombies."
    e "Pendant ce temps là, Gabriel et Roméo vont utiliser l'{i}Ami Satellite 1002 Yay{/i} pour trouver sur internet comment battre les zombies."
    
    if companion:
        if chosenPath == "Charlie":
            hide Reception with moveoutright
        elif chosenPath == "Pharmacy":
            hide Pharma with moveoutright
        else:
            hide Proprio with moveoutright
            
    hide Client with moveoutright
    hide Eva with moveoutright
    
    sv "Tout le monde sauf l'employé sortent du magasin."
    
    show Employee determination at center with move
    
    "Roméo a rapidement relié une machine à une batterie et a ouvert l'inventaire."
    
    an "Argh!"
    show Employee afraid
    
    em "Je suis un employé d'ÉlectroCoutu! Je dois aider à défendre mon magasin!"
    em "Fais une recherche pour l'{i}Ami Satellite 1002 Yay{/i} et ça va te donner un numéro qu'on peut utiliser pour le repérer rapidement dans notre stock à l'arrière du magasin."
    g "Ce serait plus logique..."
    
    hide Employee with moveoutright
    g "...que je m'occupe de les aider pendant que tu fais la recherche, tu connais ton propre système."
    sv "L'employé n'est plus là."
    g "...Il est déjà parti!"
    
    "J'ai entré les mots {=book}Ami Satellite 1002 Yay{/=book} dans le moteur de recherche de l'inventaire."
    window hide
    sv "Pleins de versions de Ami Satellite 1002 Yay apparaît à l'écran de l'inventaire du vieux ordinateur."
    show inventory at top with pixellate
    $renpy.pause(1.0)
    window show
    g "AHHH! C'EST QUOI TOUT CES RÉSULTATS?"
    g "Je vais utiliser le truc que j'avais appris... voyons voir..."
    g "Ugh, je me parle tout seul..."
    return
    

label en_elect_plan:
         
    g "Évangeline has a plan that will save us all from the zombies."
    show Eva mwahaha
    e "Yes. We're going to...{size=26}search the internet to find a solution!{/size}"
    
    #Reaction to internet search
    if companion:
        if chosenPath == "Charlie":
            show Reception stars
        elif chosenPath == "Pharmacy":
            show Pharma happy
        else:
            show Proprio happy
            
    show Employee neutral
    show Client happy
    
    em "...but there's no power."
    
    #Reaction to no electricity
    if companion:
        if chosenPath == "Charlie":
            show Reception passion
        elif chosenPath == "Pharmacy":
            show Pharma afraid
        else:
            show Proprio unhappy
    
    show Client intense
    
    an "That's why they're here! ElectricMart has lots of battery-powered products."
    show Eva determ
    e "Satellite internet? Like used by the army and yacht clubs? And batteries, with USB chargers?"
    an "I recommend the {i}Friend Satellite 1002 Yay{/i} in stock in this very store! Batteries are in aisle 3."
    
    if kitten:
        an "The official company logo is an adorable little kitten — you can't miss it!"
    
    show Employee afraid
    em "You can't just steal our stock! They'll fire me!"
    
    show Client trickster
    an "Romeo, you let us borrow a few products and in exchange, we'll defend the store from the zombies that are trying to get in."
    em "WHAT?"
    "We look towards the door. Zombies! Trying to get in!"
    
    #Reaction to zombies entering the store
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
        elif chosenPath == "Pharmacy":
            show Pharma terrified
        else:
            show Proprio drill
    
    em "Ahh!"
    
    show Eva determ
    e "Don't panic. We'll block this door as much as possible, and then we'll get out some other way to flank the zombies from outside."
    e "Meanwhile, Gabriel and Romeo will use the {i}Friend Satellite 1002 Yay{/i} to look up online how to fight zombies."
    
    if companion:
        if chosenPath == "Charlie":
            hide Reception with moveoutright
        elif chosenPath == "Pharmacy":
            hide Pharma with moveoutright
        else:
            hide Proprio with moveoutright
    
    hide Client with moveoutright
    hide Eva with moveoutright
    
    sv "Everyone but the employee leave."
    
    show Employee determination at center with move
    
    "Romeo quickly connects an employee computer to a battery and opens the inventory."
    
    an "Argh!"
    show Employee afraid
    
    em "What am I doing? I'm an employee of ElectricMart! I have to help defend the store!"
    em "Just search for {i}Friend Satellite 1002 Yay{/i} and that'll give you a number we can use to locate it in our stockroom."
    g "It would be way more logical..."
    
    hide Employee with moveoutright
    g "...that I go help with the zombies while you do the search, you know your own system better than I do."
    sv "The employee sneaks out."
    g "...He's already gone!"
    
    "I enter the words {=book}Friend Satellite 1002 Yay{/=book} in the inventory's search box."
    sv "Many different versions of the words Friend Satellite 1002 Yay appear on the inventory screen of the old computer."
    window hide
    show inventory at top with pixellate
    $renpy.pause(1.0)
    window show
    
    g "AHHH! WHAT ARE ALL OF THESE RESULTS?"
    g "I'm going to use that trick I learned... what was it again..."
    g "Ugh, I'm talking to myself..."
    return

label fr_elect_ami:
    call ms_machine from _call_ms_machine_2
    
    scene bg electro
    show inventory at top
    with dissolve
    
    sv "J'étudie de nouveau l'inventaire à l'écran du vieux ordinateur."
    
    sv "Les choix dans le menu suivant ne sont pas entièrement compatible avec le mode voix car ils sont présentés en ordre aléatoire
        et contiennent des guillemets. Dans le mode voix, votre choix sera révélé directement après votre sélection. Vous pouvez choisir de retourner pour sélectionner une option différente."
    sv "L'ordre ne changera pas avant votre prochaine session de jeu."
    sv "Menu"
    $shuffle_menu()
    sv "Menu"
    menu:
        "Donc, pour trouver l'{i}Ami Satellite 1002 Yay{/i}..."
        "\"Ami Satellite 1002 Yay\"":
            sv "Mode voix. Guillemets Ami Satellite 1001 Yay Y majuscule guillemet."
            call victoryWon from _call_victoryWon_2
            call victoryReset from _call_victoryReset
        "\"Ami Satellite\" 1002 Yay" if not chMenu1:
            sv "Mode voix. Guillemet Ami Satellite guillemet 1002 Yay."
            $chMenu1 = True
            call victoryLost from _call_victoryLost_2
            "Ça ne fonctionne pas!"
            jump fr_elect_ami
        "\"Ami Satellite 1002 yay\"" if not chMenu2:
            sv "Mode voix. Guillemet Ami Satellite 1002 yay guillemet y minuscule."
            $chMenu2 = True
            call victoryLost from _call_victoryLost_3
            "Oops, je pense que les majuscules font une différence dans ce système."
            jump fr_elect_ami
        "\"Ami Satellite\" AND \"1002 Yay\"" if not chMenu3:
            sv "Mode voix. Guillemet Ami Satellite guillemet AND guillemet 1002 Yay guillemet."
            $chMenu3 = True
            call victoryLost from _call_victoryLost_4
            "Non, j'ai encore trop d'options."
            jump fr_elect_ami
        "Ami AND Satellite AND 1002 AND Yay" if not chMenu4:
            sv "Mode voix. Ami AND Satellite AND 1002 AND Yay."
            $chMenu4 = True
            call victoryLost from _call_victoryLost_5
            "J'ai probablement besoin d'utiliser des guillemets pour ma recherche."
            jump fr_elect_ami
    return
    
label en_elect_ami:
    call ms_machine from _call_ms_machine_3
    scene bg electro
    show inventory at top
    with dissolve
    
    sv "I study the inventory on the screen of the old computer."
    
    sv "The choices offered in the next menu are not entirely compatible with self-voiced mode because they are presented in a random order
        and contain quotation marks. In self-voiced mode, your choice will be directly revealed after your selection. You can choose to go back to make a different selection."
    sv "The order in which options are presented won't change until your next playthrough."
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "In order to find the {i}Friend Satellite 1002 Yay{/i}..."
        "\"Friend Satellite 1002 Yay\"":
            sv "Self-voiced mode. Quotation marks Friend Satellite 1002 Yay Capital Y Quotation Marks."
            call victoryWon from _call_victoryWon_3
            call victoryReset from _call_victoryReset_1
        "\"Friend Satellite\" 1002 Yay" if not chMenu1:
            sv "Self-voiced mode. Quotation Mark Friend Satellite Quotation Mark. 1002 Yay."
            $chMenu1 = True
            call victoryLost from _call_victoryLost_6
            "That doesn't work!"
            jump en_elect_ami
        "\"Friend Satellite 1002 yay\"" if not chMenu2:
            sv "Self-voiced mode. Quotation mark Friend Satellite 1002 yay lower-case y quotation marks."
            $chMenu2 = True
            call victoryLost from _call_victoryLost_7
            "Oops, I think that capitalization might make a difference in this system."
            jump en_elect_ami
        "\"Friend Satellite\" AND \"1002 Yay\"" if not chMenu3:
            sv "Self-voiced mode. Quotation mark friend satellite quotation mark AND quotation mark 1002 yay quotation mark."
            $chMenu3 = True
            call victoryLost from _call_victoryLost_8
            "No, I still get too many results."
            jump en_elect_ami
        "Friend AND Satellite AND 1002 AND Yay" if not chMenu4:
            sv "Self-voiced mode. Friend AND satellite AND 1002 AND yay."
            $chMenu4 = True
            call victoryLost from _call_victoryLost_9
            "I probably need to use quotation marks in my search. I don't want to have a flashback again!"
            jump en_elect_ami
    return
    
label fr_elect_rech:
    hide inventory
    "J'ai réussi à trouver l'{i}Ami Satellite 1002 Yay{/i} et à brancher le système à un ordinateur portable."
    "Je peux entendre Évangeline et les autres se battre dehors."
    "Ce n'est pas le temps de faire des erreurs. Je vais utiliser les étapes de la recherche et les opérateurs booléens pour trouver 
     comment anéantir les zombies une fois pour toute! Sans prendre le temps de me souvenir de la visite de la bibliothécaire."
    "La recherche est un processus récursif, et l'ordre exact des étapes de recherche peut varier, mais je me sens comme si l'univers veut que je suive une séquence très spécifique..."

    return
    
label en_elect_rech:
    hide inventory
    "I find the {i}Friend Satellite 1002 Yay{/i} right where it should be and connect it to a computer and some powerful batteries."
    "I can hear Évangeline and the others fighting outside."
    "There's no room for error. I have to use boolean operators and all the steps involved in a good research process to 
     find out how to destroy zombies once and for all! Without taking a moment to mentally go over the steps."
    "Research is a circular process, and the exact order of the steps can vary, but I feel like the universe wants me to use a very specific sequence..."
    return
    
label fr_elect_rech1:
    if not chMenu2:
        "Logiquement, la première étape d'une belle recherche efficace serait de..."
    else:
        "Logiquement, la prochaine étape d'une belle recherche efficace serait de..."
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "Pour une recherche efficace..."
        "Choisir ma question de recherche!":
            "Je ne peux pas faire une recherche si je ne sais pas ce que je veux chercher!"
            "Si je ne connaissais pas bien mon sujet, je pourrais faire une première recherche exploratoire pour me familiariser avec les concepts importants 
             et pour extraire les mots clés pertinents."
            "Mais aujourd'hui, c'est simple! J'ai besoin de trouver {b}une façon d'anéantir rapidement et efficacement les zombies!{/b}"
            call victoryWon from _call_victoryWon_4
            call victoryReset from _call_victoryReset_2
        "Trouver un outil dans lequel faire ma recherche!" if not chMenu1:
            $chMenu1 = True
            call victoryLost from _call_victoryLost_10
            "Logiquement, je ne peux pas faire une recherche si je n'ai pas un endroit où chercher!"
            "Mais... j'ai l'impression de me souvenir qu'on peut parfaitement préparer sa recherche avant de trouver où chercher..."
            jump fr_elect_rech1
        "NE PAS PANIQUER!" if not chMenu2:
            $chMenu2 = True
            "C'est vrai!"
            "Paniquer n'est jamais une bonne façon de débuter une recherche."
            jump fr_elect_rech1
    
    return
    
label en_elect_rech1:
    
    #2 steps with an optional third step
    if not chMenu2:
        "Logically, the first step to take when conducting research is..."
    else:
        "Logically, the next step of a good efficient search would be..."
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "Steps to conducting research..."
        "Define my research question!":
            "I can't search without having a goal! A question to answer!"
            "If I didn't know my subject very well, I could do a first exploratory search to learn the most important concepts 
             and extract some keywords from results."
            "But today is easy! I just need to find a way to {b}quickly and completly destroy zombies!{/b}"
            call victoryWon from _call_victoryWon_5
            call victoryReset from _call_victoryReset_3
        "Decide where to conduct my search!" if not chMenu1:
            $chMenu1 = True
            call victoryLost from _call_victoryLost_11
            "Logically, I can't do a search in a vacuum — I need to decide where I'll do my search!"
            "But... I seem to remember that we can do a lot of work to prepare a search before actually starting to worry about where we'll conduct the search..."
            jump en_elect_rech1
        "DON'T PANIC!" if not chMenu2:
            $chMenu2 = True
            "That's right! Panic doesn't really help with the research process."
            jump en_elect_rech1
    
    return

label fr_elect_rech2:
   
    sv "Menu"
    $shuffle_menu()
    menu:
        "La prochaine étape du processus de recherche..."
        
        "Identifier les mots clés importants dans ma question de recherche." if flag2 < 1:
            #Nécessaire pour menu choix des mots clés
            $chMenu1 = False
            $chMenu2 = False
            $chMenu3 = False
            
            g "Je dois commencer par identifier les mots clés importants de ma recherche."
            $victoryFlagTemp = victoryFlag
            call victoryReset from _call_victoryReset_4
            call bil_elect_atmos from _call_bil_elect_atmos
            call fr_elect_rech_bool from _call_fr_elect_rech_bool
            $victoryFlag = victoryFlagTemp
            jump bil_elect_success
        
        "Trouver des synonymes aux termes utilisés pour la recherche, y compris des synonymes en anglais." if flag2 < 2 and not chMenu1:
            if flag2 == 1:
                call bil_elect_atmos from _call_bil_elect_atmos_1
                call fr_elect_synonyme from _call_fr_elect_synonyme
                jump bil_elect_success
            else:
                $chMenu1 = True
                jump bil_elect_fail
        
        "Utiliser des opérateurs booléens, ou remplir un bordereau de recherche." if flag2 < 3 and not chMenu2:
            if flag2 == 2:
                call bil_elect_atmos from _call_bil_elect_atmos_2
                call fr_elect_rech_bool2 from _call_fr_elect_rech_bool2
                jump bil_elect_success
            else:
                $chMenu2 = True
                jump bil_elect_fail
                
        "Identifier les meilleurs moteurs de recherche ou bases de données où effectuer la recherche." if flag2 < 4 and not chMenu3:
            if flag2 == 3:
                call bil_elect_atmos from _call_bil_elect_atmos_3
                $chMenu1 = False
                $chMenu2 = False
                $chMenu3 = False
                $chMenu4 = False
                
                g "Je dois choisir mes bases de données et/ou des moteurs de recherche."
                g "Je me souviens vraiment bien des explications de la bibliothécaire à ce sujet."
            
                call fr_elect_source from _call_fr_elect_source
                jump bil_elect_success
            else:
                $chMenu3 = True
                jump bil_elect_fail
        
        "Lancer la recherche dans les sources d'information sélectionnées." if flag2 < 5 and flag2 > 2 and not chMenu4:
            if flag2 == 4:
                call bil_elect_atmos from _call_bil_elect_atmos_4
                call fr_elect_startsearch from _call_fr_elect_startsearch
                jump bil_elect_success
            else:
                $chMenu4 = True
                jump bil_elect_fail
                
        "Utiliser des filtres pour restreindre le nombre de résultats." if flag2 < 6 and flag2 > 2 and not chMenu5:
            if flag2 == 5:
                call bil_elect_atmos from _call_bil_elect_atmos_5
                call electroFiltre from _call_electroFiltre
                jump bil_elect_success
            else:
                $chMenu5 = True
                jump bil_elect_fail
                
        "Évaluer rapidement les résultat de la recherche et changer sa stratégie si nécessaire." if flag2 < 7 and flag2 > 2 and not chMenu6:
            if flag2 == 6:
                call bil_elect_atmos from _call_bil_elect_atmos_6
                call bil_elect_eval from _call_bil_elect_eval
                jump bil_elect_success
            else:
                $chMenu6 = True
                jump bil_elect_fail
                
        "Sélectionner des résultats de la recherche et y accéder." if flag2 < 8 and flag2 > 2 and not chMenu7:
            if flag2 == 7:
                call bil_elect_atmos from _call_bil_elect_atmos_7
                call electroSel from _call_electroSel
                jump bil_elect_success
            else:
                $chMenu7 = True
                jump bil_elect_fail
        
        "Analyser la pertinence des résultats individuels." if flag2 < 9 and flag2 > 6 and not chMenu8:
            if flag2 == 8:
                call bil_elect_atmos from _call_bil_elect_atmos_8
                $chMenu1 = False
                $chMenu2 = False
                $chMenu3 = False
                $chMenu4 = False
                call fr_elect_evalRes from _call_fr_elect_evalRes
                jump bil_elect_success
            else:
                $chMenu8 = True
                jump bil_elect_fail
        
        "Extraire l'information." if flag2 < 10 and flag2 > 6 and not chMenu9:
            if flag2 == 9:
                call bil_elect_atmos from _call_bil_elect_atmos_9
                g "Oui, c'est ça!"
                call bil_elect_extraction from _call_bil_elect_extraction
                jump bil_elect_success
            else:
                $chMenu9 = True
                jump bil_elect_fail
        
        "Sauver ses références." if flag2 < 11 and flag2 > 6 and not chMenu10:
            if flag2 == 10:
                g "Oui, c'est ça!"
                call fr_elect_ref from _call_fr_elect_ref
                jump bil_elect_success
            else:
                $chMenu10 = True
                jump bil_elect_fail
                
    return
    
label en_elect_rech2:
   
    #11 steps
    sv "Menu"
    $shuffle_menu()
    menu:
        "The next step to take when conducting research is to..."
        
        "Identify important keywords in my research question." if flag2 < 1:
            #Necessary for menu choix for keywords
            $chMenu1 = False
            $chMenu2 = False
            $chMenu3 = False

            call bil_elect_atmos from _call_bil_elect_atmos_10
            g "I have to start by identifying the most important keywords for my research topic."
            $victoryFlagTemp = victoryFlag
            call victoryReset from _call_victoryReset_5
            call en_elect_rech_bool from _call_en_elect_rech_bool
            $victoryFlag = victoryFlagTemp
            jump bil_elect_success
            
        "Find synonyms for the chosen keywords." if flag2 < 2 and not chMenu1:
            if flag2 == 1:
                call bil_elect_atmos from _call_bil_elect_atmos_11
                call en_elect_synonyme from _call_en_elect_synonyme
                jump bil_elect_success
            else:
                $chMenu1 = True
                jump bil_elect_fail
        
        "Use boolean operators, or fill out a search strategy form." if flag2 < 3 and not chMenu2:
            if flag2 == 2:      
                call bil_elect_atmos from _call_bil_elect_atmos_12
                call en_elect_rech_bool2 from _call_en_elect_rech_bool2
                jump bil_elect_success
            else:
                $chMenu2 = True
                jump bil_elect_fail
                
        "Identify the best search engines or databases where to conduct the search." if flag2 < 4 and not chMenu3:
            if flag2 == 3:
                $chMenu1 = False
                $chMenu2 = False
                $chMenu3 = False
                $chMenu4 = False
                
                call bil_elect_atmos from _call_bil_elect_atmos_13
                
                g "I have to pick some databases and/or search engines."
                g "I remember the librarian's explanations on that topic very well."
            
                call en_elect_source from _call_en_elect_source
                jump bil_elect_success
            else:
                $chMenu3 = True
                jump bil_elect_fail
        
        "Search in selected search engines or databases." if flag2 < 5 and flag2 > 2 and not chMenu4:
            if flag2 == 4:
                call bil_elect_atmos from _call_bil_elect_atmos_14
                call en_elect_startsearch from _call_en_elect_startsearch
                jump bil_elect_success
            else:
                $chMenu4 = True
                jump bil_elect_fail
                
                
        "Use search filters to reduce the number of results." if flag2 < 6 and flag2 > 2 and not chMenu5:
            if flag2 == 5:
                call bil_elect_atmos from _call_bil_elect_atmos_15
                call electroFiltre from _call_electroFiltre_1
                jump bil_elect_success
            else:
                $chMenu5 = True
                jump bil_elect_fail
                
        "Take a quick glance at the list of search results and change strategies as needed." if flag2 < 7 and flag2 > 2 and not chMenu6:
            if flag2 == 6:
                call bil_elect_atmos from _call_bil_elect_atmos_16
                call bil_elect_eval from _call_bil_elect_eval_1
                jump bil_elect_success
            else:
                $chMenu6 = True
                jump bil_elect_fail
                
        "Select and access some of the search results." if flag2 < 8 and flag2 > 2 and not chMenu7:
            if flag2 == 7:
                call bil_elect_atmos from _call_bil_elect_atmos_17
                call electroSel from _call_electroSel_1
                jump bil_elect_success
            else:
                $chMenu7 = True
                jump bil_elect_fail
        
        "Analyze the relevance of individual search results." if flag2 < 9 and flag2 > 6 and not chMenu8:
            if flag2 == 8:
                call bil_elect_atmos from _call_bil_elect_atmos_18
                $chMenu1 = False
                $chMenu2 = False
                $chMenu3 = False
                $chMenu4 = False
                call en_elect_evalRes from _call_en_elect_evalRes
                jump bil_elect_success
            else:
                $chMenu8 = True
                jump bil_elect_fail
        
        "Extract information." if flag2 < 10 and flag2 > 6 and not chMenu9:
            if flag2 == 9:
                call bil_elect_atmos from _call_bil_elect_atmos_19
                g "Yes, that's right!"
                call bil_elect_extraction from _call_bil_elect_extraction_1
                jump bil_elect_success
            else:
                $chMenu9 = True
                jump bil_elect_fail
        
        "Save your citations." if flag2 < 11 and flag2 > 6 and not chMenu10:
            if flag2 == 10:
                g "Yep!"
                call fr_elect_ref from _call_fr_elect_ref_1
                jump bil_elect_success
            else:
                $chMenu10 = True
                jump bil_elect_fail
                
    return
  
label fr_elect_rech_bool:
    
    sv "Menu"
    $shuffle_menu()
    menu:
        g "On veut anéantir efficacement et rapidement les zombies. Quels sont les mots clés importants?"
        
        "\"Anéantir efficacement et rapidement les zombies\"" if not chMenu1:
            $chMenu1 = True
            call victoryLost from _call_victoryLost_12
            
            g "C'est beaucoup de mots. Est-ce que c'est vraiment ce que je dois faire comme recherche?"
            g "Je devrais au moins enlever les mots vides comme {=book}et{/=book} et {=book}les{/=book}..."
            
            jump fr_elect_rech_bool
            
        "Combattre — Zombies — Efficacement et rapidement" if not chMenu2:
            $chMenu2 = True
            call victoryLost from _call_victoryLost_13
            
            g "Maintenant que j'y pense, je ne veux probablement pas chercher avec un mot vide comme {=book}et{/=book}..."
            
            jump fr_elect_rech_bool
            
        "Combattre — Zombies — Chatons" if kitten and not chMenu4:
            $chMenu4 = True
            call victoryLost from _call_victoryLost_14
            
            g "Non, à quoi je pense? Les chatons sont trop précieux pour utiliser contre les zombies."
            
            jump fr_elect_rech_bool
            
        "Combattre — Zombies":
            g "Oui, je pense que {=book}combattre{/=book} et {=book}zombies{/=book} sont les mots clés importants pour ma recherche."
            call victoryWon from _call_victoryWon_6
            
        "Combattre — Zombies — Efficacement — Rapidement" if not chMenu3:
            $chMenu3 = True
            call victoryLost from _call_victoryLost_15
                
            g "Tous les mots importants sont là!"
            g "Mais les adjectifs sont probablement de trop? Je voudrais trouver un article sur comment combattre les zombies même si les auteurs
               ont trouvé une méthode {=book}super bonne{/=book} ou {=book}incroyable{/=book} pour les battre plutôt que {=book}rapide{/=book} et/ou {=book}efficace{/=book}."
            
            jump fr_elect_rech_bool
    
    return
    
label en_elect_rech_bool:
    
    sv "Menu"
    $shuffle_menu()
    menu:
        g "How can we quickly and efficiently fight the zombies? What are the important keywords in this research question?"
        
        "\"Quickly and efficiently defeat the zombies\"" if not chMenu1:
            $chMenu1 = True
            call victoryLost from _call_victoryLost_16
            
            g "That's way too many words. Is that really what I want to put in the search box?"
            g "I should at last remove words empty of meaning like {=book}can{/=book} and {=book}we{/=book} and lowercase {=book}and{/=book}..."
            
            jump en_elect_rech_bool
            
        "Fight — Zombies — Quickly and efficiently" if not chMenu2:
            $chMenu2 = True
            call victoryLost from _call_victoryLost_17
            
            g "Now that I think about it, I probably don't want to search for an empty word like lowercase {=book}and{/=book}..."
            
            jump en_elect_rech_bool
            
            
        "Fight — Zombies — Kitten" if kitten and not chMenu4:
            $chMenu4 = True
            call victoryLost from _call_victoryLost_18
            
            g "No, what am I thinking? Kittens are too precious to use in the fight against zombies."
            
            jump en_elect_rech_bool
            
        "Fight — Zombies":
            g "Yes, {=book}fight{/=book} and {=book}zombies{/=book} are the most important keywords for my search."
            call victoryWon from _call_victoryWon_7
            
        "Fight — Zombies — Quickly — Efficiently" if not chMenu3:
            $chMenu3 = True
            call victoryLost from _call_victoryLost_19
            
            g "All the important words are there!"
            g "But the adjectives probably aren't needed? I want to be able to find an article about how to fight zombies, even if the authors 
               have found an {=book}awesome{/=book} or {=book}thorough{/=book} or {=book}speedy{/=book} method to fight instead of {=book}quickly{/=book} and/or {=book}efficiently{/=book}."
            
            jump en_elect_rech_bool
    
    return
    
label fr_elect_synonyme:
    g "Oui, c'est ça!"
    g "Je peux penser à un synonyme de {=book}zombies{/=book} : {=book}walking dead{/=book}."
    g "Et plusieurs synonymes de {=book}combattre{/=book}: {=book}battre{/=book}, {=book}lutter{/=book}, {=book}anéantir{/=book},
       {=book}batailler{/=book}, {=book}fight{/=book}, {=book}destroy{/=book}, {=book}eliminate{/=book}."
    g "Et quelques autres mots qui s'éloignent de synonymes de {=book}combattre{/=book}. Mais s'ils se trouvent dans les résultats de recherche,
        je suis intéressé!"
    g "Des mots comme {=book}arme{/=book}, {=book}weapon{/=book}, {=book}stratégie{/=book}, {=book}strategy{/=book}, {=book}offensive{/=book}."
    g "Je suis prêt pour la prochaine étape de recherche!"
    return
    
label en_elect_synonyme:
    g "Yes, that's right!"
    g "{=book}Walking dead{/=book} might be a good synonym of {=book}zombies{/=book}."
    g "And several synonyms of {=book}fight{/=book}: {=book}destroy{/=book}, {=book}anhiliate{/=book},
       {=book}defeat{/=book}, {=book}eradicate{/=book}, {=book}eliminate{/=book}."
    g "And other words that are not quite synonyms of {=book}fight{/=book}. But if they're in the search results, I'm interested!"
    g "Words like {=book}weapons{/=book}, or {=book}strategy{/=book}."
    g "I'm ready for the next step of the research process!"
    return
    
label fr_elect_rech_bool2:
    
    sv "Mode voix Gabriel. Une expression booléenne efficace pour ma question de recherche pourrait être ouvre parenthèse
        Zombie OR guillemet walking dead guillemet ferme parenthese. AND ouvre parenthèse comabt* OR batt* OR lutte* OR anéant* OR fight* OR 
        destroy* OR eliminat* OR arme* OR weapon* OR strat* OR offen* ferme parenthèse."
    g "Une expression booléenne efficace pour ma question de recherche pourrait être ({=word}Zombie{/=word} {=bool}OR{/=bool} {=word}\"walking dead\"{/=word}) 
       {=bool}AND{/=bool} ({=word}combat*{/=word} {=bool}OR{/=bool} {=word}batt*{/=word} {=bool}OR{/=bool} {=word}lutte*{/=word} {=bool}OR{/=bool} {=word}anéant*{/=word} {=bool}OR{/=bool} {=word}fight*{/=word} {=bool}OR{/=bool}
       {=word}destroy*{/=word} {=bool}OR{/=bool} {=word}eliminat*{/=word} {=bool}OR{/=bool} {=word}arme*{/=word} {=bool}OR{/=bool} {=word}weapon*{/=word} {=bool}OR{/=bool} {=word}strat*{/=word} {=bool}OR{/=bool} 
       {=word}offen*{/=word})"
    
    return
    
label en_elect_rech_bool2:
    
    sv "Self-voiced Gabriel. A great boolean search expression for my reserch question could be open parentheses zombies OR quotation marks walking dead quotation marks close parentheses. AND open parentheses
        fight* OR destroy* OR anhiliat* OR defeat* OR eradicat* OR destroy* OR eliminat* OR weapon OR strategy close parentheses."
    g "A great boolean search expression for my research question could be ({=word}Zombies{/=word} {=bool}OR{/=bool} {=word}\"Walking Dead\"{/=word}) {=bool}AND{/=bool} 
       ({=word}fight*{/=word} {=bool}OR{/=bool} {=word}destroy*{/=word} {=bool}OR{/=bool} {=word}anhiliat*{/=word} {=bool}OR{/=bool} {=word}defeat*{/=word} {=bool}OR{/=bool} {=word}eradicat*{/=word} {=bool}OR{/=bool} {=word}destroy*{/=word} {=bool}OR{/=bool} 
       {=word}eliminat*{/=word} {=bool}OR{/=bool} {=word}weapon{/=word} {=bool}OR{/=bool} {=word}strategy{/=word})"
    
    return
    
label fr_elect_source:
    
    sv "Menu"
    $unshuffle_menu()
    menu:
        g "Je vais chercher dans les ressources suivantes!"
        "{i}\[ Bases de données Open Access! \]{/i}" if not chMenu1:
            $chMenu1 = True
            g "Des bases de données qui indexent du contenu {=book}Open Access{/=book} contiendraient peut-être des articles que je peux utiliser?"
            g "Normalement ça prend quand même un peu de temps pour passer à travers le processus de publication d'un article. 
               Un comité d'experts sur le sujet de l'article doit l'approuver avant sa publication."
            g "Certaines plateformes Open Access permettent la publication rapide d'articles sans nuire à la qualité du processus."
            jump fr_elect_source
        "{i}\[ Bases de données de journaux! \]{/i}" if not chMenu2:
            $chMenu2 = True
            g "Je vais définitivement consulter des bases de données de {=book}journaux{/=book} puisqu'on y trouve des nouvelles récentes."
            g "Si quelqu'un a trouvé une solution pour battre les zombies, ils l'ont certainement partagée avec des journalistes?!"
            jump fr_elect_source
        "{i}\[ Sites webs gouvernementaux et blogs de scientistes! \]{/i}" if not chMenu3:
            $chMenu3 = True
            g "Je veux aussi faire une recherche dans les {=book}sites webs gouvernementaux{/=book} et dans les {=book}blogs de scientistes{/=book}."
            g "Ce sont habituellement des sources fiables d'information, bien que je dois être prudent avec les blogs et vérifier les qualifications des auteurs."
            jump fr_elect_source
        "{i}\[ Forums de discussion et Wikipédia! \]{/i}" if not chMenu4:
            $chMenu4 = True
            g "Je suis assez désespéré que je vais également fouiller dans les {=book}forums de discussions{/=book} et dans {=book}Wikipédia{/=book}! 
               L'information ne sera pas nécessairement fiable mais je peux utiliser mon propre jugement pour voir si ça fait du sens."
            g "Au moins les zombies ne peuvent probablement pas contribuer aux forums de discussion et à Wikipédia!"
            jump fr_elect_source
        "{b}Je connais vraiment bien les différents types de ressources!{/b}":
            pass
   
    g "Bon, je pense que j'ai un bon plan de recherche!"
    g "Une CHANCE que la bibliothécaire nous a expliqué les différentes bases de données dans lesquelles ont peut faire de la recherche et ses
        merveilleux trucs pour faire des recherches efficace dans Google."

    return
    
label en_elect_source:
    
    sv "Menu"
    $unshuffle_menu()
    menu:
        g "I'm going to explore the following sources of information!"
        "{i}\[ Open access databases! \]{/i}" if not chMenu1:
            $chMenu1 = True
            g "Databases that index {=book}open access{/=book} content might have some articles I could use?"
            g "The article publication process is speedy compared to publishing a book, but it does take a bit of time. 
               For serious articles, a committee of experts on the article's topic have to approve it before it's allowed to be published."
            g "Some open access platforms enable a pretty quick turnaround with no negative impact on quality."
            jump en_elect_source
        "{i}\[ Newspaper article databases! \]{/i}" if not chMenu2:
            $chMenu2 = True
            g "I will definitely take a look at some {=book}newspapers{/=book} because they'll have the most recent information to share."
            g "If someone found a way to take out the zombies, they would definitely share that with a journalist!"
            jump en_elect_source
        "{i}\[ Government websites and scientific blogs! \]{/i}" if not chMenu3:
            $chMenu3 = True
            g "I also want to search in {=book}government websites{/=book} and {=book}scientist's blogs{/=book}."
            g "They're usually a reliable source of information, though I have to be extra careful to check the qualification of 
               authors when I look at blogs."
            jump en_elect_source
        "{i}\[ Discussion forums and wikipedia! \]{/i}" if not chMenu4:
            $chMenu4 = True
            g "I'm desperate enough that I'll look at {=book}discussion forums{/=book} and {=book}wikipedia{/=book}! 
               The information won't necessarily be reliable, but I'll use my own judgement to see if there's anything I can use."
            g "At least I know that zombies probably aren't contributing much to discussion forums or wikipedia!"
            jump en_elect_source
        "{b}I'm already familiar with all kinds of resources!{/b}":
            pass
   
    g "Well, I think I've come up with a good research plan!"
    g "It turned out well that the librarian visited last week, and 
       explained the differences between types of databases and gave us some wonderful Google search tricks."

    return
    
label fr_elect_startsearch:
    
    "J'ai lancé la recherche dans les sources d'information choisies."
    "J'ai plusieurs résultats!"
    "Mais je peux voir que j'ai trouvé beaucoup de résultats fictifs."
    "Ils proviennent d'avant qu'on se fasse envahir par les zombies."
    if kitten:
        "Quand j'avais le temps de rester assis sur le sofa avec mon minou."
    "Je sais quoi faire pour régler ce problème!"
    
    return
    
label en_elect_startsearch:
    
    "I search in my selected sources of information."
    "There are several results!"
    "But I can see that a lot of the results concern works of fiction."
    "They were published before we got inundated with zombies."
    if kitten:
        "Back when I had the time to sit on the couch curled up with my beloved cat."
    "That's a problem I know how to fix!"
    
    return
    
label electroFiltre:
    
    if lang == "english":
        "The zombies first appeared about a month ago, and we only really realized they weren't a hoax two weeks ago!"
        "I use a date filter to find documents that were published very recently."
        "Plenty of other filters exist: scientific article filter, full text filter, keyword filter, types of documents filter, etc."
        "I'm grateful the librarian patiently explained the best ways to use these filters."
    else:
        "Ça ne fait qu'environ 1 mois depuis la première apparition de zombies, et seulement 2 semaines depuis qu'on a réalisé que c'est vraiment vrai!"
        "J'ai utilisé des filtres pour obtenir des documents publiés très récemment."
        "Il existe pleins d'autres filtres : articles scientifiques, plein texte, mots clés, type de documents, etc."
        "Je suis content que la bibliothécaire nous a expliqué la meilleure façcon d'utiliser ces filtres."
    
    return
    
label electroSel:
    
    if lang == "english":
        "The University's Library pays for us to have access to many resources."
        "I'm happy to see that my access still works!"
    else:
        "La Bibliothèque de l'Université a payé pour nous donner accès à des ressources."
        "Je suis content de voir que j'y ai encore accès!"
    
    return
    
label fr_elect_evalRes:
    
    if not chMenu1 or not chMenu2 or not chMenu3 or not chMenu4:
        sv "Menu"
        $unshuffle_menu()
        menu:
            "Comment évaluer les résultats?"
            "{i}\[ Faire une lecture en diagonale du document. \]{/i}" if not chMenu1:
                $chMenu1 = True
                g "C'est vrai, je n'ai pas besoin de lire au complet un résultat pour décider s'il est intéressant."
                g "Je peux lire rapidement en diagonale pour saisir l'essentiel du texte."
                jump fr_elect_evalRes
            "{i}\[ Lire les sous-titres du document. \]{/i}" if not chMenu2:
                $chMenu2 = True
                g "Si le document a des sous-titres, simplement lire les sous-titres (et peut-être le premier paragraphe après chaque sous-titre)..."
                g "ça va me donner une bonne idée du contenu du document."
                jump fr_elect_evalRes
            "{i}\[ Lire l'abstrait d'un article. \]{/i}" if not chMenu3:
                $chMenu3 = True
                g "Un abstrait, c'est un petit résumé d'un article scientifique ou d'un plus gros document."
                g "Lire l'abstrait est une excellente façon d'évaluer un résultat de recherche."
                jump fr_elect_evalRes
            "{i}\[ Vérifier les métadonnées d'un résultat. \]{/i}" if not chMenu4:
                $chMenu4 = True
                g "Je peux regarder les sujets assignés au résultat, les auteurs, la date de publication, etc."
                g "Ces éléments peuvent m'aider à éliminer un résultat sans même être obligé de le lire!"
                jump fr_elect_evalRes
            "{b}Je sais déjà très bien comment évaluer les résultats d'une recherche.{/b}":
                $chMenu1 = True
                $chMenu2 = True
                $chMenu3 = True
                $chMenu4 = True
        
    return
    
label en_elect_evalRes:
    
    if not chMenu1 or not chMenu2 or not chMenu3 or not chMenu4:
        sv "Menu"
        $unshuffle_menu()
        menu:
            "How to evaluate a document?"
            "{i}\[ Skim quickly through the document. \]{/i}" if not chMenu1:
                $chMenu1 = True
                g "It's true, I don't need to read every last word of a search result to decide if it's relevant."
                g "I can skim through it quickly to get an overall sense of its contents."
                jump en_elect_evalRes
            "{i}\[ Read the document's headings. \]{/i}" if not chMenu2:
                $chMenu2 = True
                g "If a document has headings, quickly reading these headings (and maybe the first paragraph after each heading)..."
                g "That will give me a good idea of its contents."
                jump en_elect_evalRes
            "{i}\[ Read an article's abstract. \]{/i}" if not chMenu3:
                $chMenu3 = True
                g "An abstract is pretty useful, because it's a short recap of the full content."
                g "Reading abstracts is an excellent way to evaluate a search result."
                jump en_elect_evalRes
            "{i}\[ Check the metadata of a search result. \]{/i}" if not chMenu4:
                $chMenu4 = True
                g "I can look at the subjects assigned to the document, its authors, the publication date, etc."
                g "Any of these elements might help me eliminate a result without even having to read its title!"
                jump en_elect_evalRes
            "{b}I already know very well how to evaluate the results of a search.{/b}":
                $chMenu1 = True
                $chMenu2 = True
                $chMenu3 = True
                $chMenu4 = True
        
    return
    
label bil_elect_extraction:
    
    if lang == "english":
        "I'm starting to feel like I'm running out of time."
        "I print out the 5 most promising results."
        "Their abstracts have already given me some good ideas..."
    else:
        "Je sens que je commence à manquer de temps."
        "J'ai imprimé les 5 résultats les plus prometteurs."
        "Les abstraits de ces résultats me donnent déjà des bonnes idées!"
    
    return
  
label bil_elect_atmos:
    
    if flag2 != 3 and flag2 != 8:
        $myFightWin = fightWin.pop()
        "[myFightWin]"
        
    if flag2 == 3:
        if lang == "english":
            "I can hear the fighting intensify. I think I'm going to move away..."
        else:
            "Je peux entendre la bataille s'intensifier dehors. Je pense que je vais m'éloigner..."
        scene bg electro2 with fade
        
    if flag2 == 4:
        if lang == "english":
            sv "Blood splatters hit a wall near me."
        else:
            sv "Du sang revole contre un mur près de moi."
        show rain

    if flag2 == 6:
        scene bg electro3 with hpunch
        if lang == "english":
            "Urgh, things are shaking violently."
        else:
            "Argh, tout tremble!"
            
    if flag2 == 7:
        $style.menu_choice.outlines = [(18, "#3f603e", 4, 4), (10, "#000000", 0, 0), (5, "#FF0000", 0, 0)]
        
    if flag2 == 8 or flag2 == 9:
        scene bg electro2 with vpunch
        
    return
    
    
label bil_elect_success:   
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
        
    $flag2 +=1
        
    if lang == "english":
        jump en_elect_rech2
    else:
        jump fr_elect_rech2
    return
    
label bil_elect_eval:
    
    if lang == "english":
        "The results look very promising."
        "Otherwise, I would adjust the parameters of my search, rethink my boolean operators, or remove some filters."
    else:
        "Les résultats sont très prometteurs."
        "Sinon, il faudrait ajuster ma recherche, resonger des opérateurs booléens, ou abandonner des filtres."
    
    return
    
label fr_elect_ref :
    
    if lang == "english":
        "The librarian also taught us how to save our references using a bibliography manager."
        "It takes only seconds to do, so I save the citations. You never know!"
        sv "Ignore the next menu mention."
    else:
        "La bibliothécaire nous a aussi enseigné commment sauver les références en utilisant un logiciel de gestion de bibliographie."
        "Ça prend juste quelques secondes, alors j'ai sauvé mes références. On ne sait jamais!"
        sv "Ignorer la prochaine mention de menu."
        
    return
    
label fr_elect_Concl:

    "Une fois le dernier article imprimé, j'ai ramassé le portable et vite couru vers l'entrée d'ÉlectroCoutu."
    call sc_electro from _call_sc_electro_2
    
    "Il y avait des corps partout."
    
    call ms_end from _call_ms_end_2
    
    #Vérifier si on a un allié
    if companion:
        #Si tout le monde est mort
        if companionRIP and clienteRIP and employeeRIP:
            "Les zombies...et tout nos nouveaux alliés."
            sv "Évangeline entre dans le magsin."
            show Eva pensive at center with moveinright
            "Est-ce que les articles que j'ai trouvés valaient vraiment ce sacrifice?"
            
            e "La victoire nous a coûté très chère."
        
        #Si une personne ou plus est morte
        elif companionRIP or clienteRIP or employeeRIP:
            "Les zombies...et certains de nos alliés."
            sv "Évangeline entre dans le magasin."
            show Eva pensive at left with moveinright
            e "Tiens, salut Gabriel."
        
            #Antonine et Roméo survivent
            if companionRIP and not clienteRIP and not employeeRIP:
                sv "L'employé et la cliente la suive de près."
                show Employee neutral at center with moveinright
                show Client intense at right with moveinright
                
                if chosenPath == "Charlie":
                    g "Wilfred?"
                    sv "Évangeline ne sait pas quoi dire. Cliquer deux fois pour continuer."
                    e "..."
                    "Le pauvre réceptionniste. Je n'aurais jamais dû l'inviter à nous joindre!"
                elif chosenPath == "Sport":
                    g "Viola?"
                    an "Elle a emporté 5 zombies avec elle! C'était impressionant à voir!"
                    sv "Un moment de silence. Cliquez deux fois pour continuer."
                    "..."
                else:
                    g "Le pharmacien?"
                    em "Euh, il est devenu un zombie. Je pense qu'il s'est fait mordre pendant la bataille? On s'est occupé de lui..."
                    sv "Un moment de silence. Cliquez deux fois pour continuer."
                    "..."
                
                an "Tu as récupéré l'Ami Satellite 1002 Yay?"
                g "Oui. J'ai imprimé de l'information qui va être utile."
                show Employee afraid
                em "Je ne suis toujours pas très comfortable avec l'idée de voler un ordinateur portable!"
                show Eva determ
                e "C'est correct, on va rembourser ton magasin lorsqu'on va avoir terminé d'éliminer les zombies."
                show Client trickster
                an "On va être des héros!!! Ils vont nous donner tout votre stock!"
                
            #Roméo survit
            if companionRIP and clienteRIP and not employeeRIP:
                show Employee afraid at right with moveinright
                sv "L'employée la suit de près."
                
                em "AHHHH! J'espère qu'on ne va pas me demander de nettoyer tout ça!"
                show Eva determ
                e "Tu nous as trouvé une solution?"
                
                if chosenPath == "Charlie":
                    g "oui...pauvre Antonine. Pauvre réceptionniste."
                elif chosenPath == "Pharmacy":
                    g "oui...pauvre Antonine. Pauvre pharmacien."
                else:
                    g "Oui..pauvre Antonine. Pauvre Viola."
                    
                show Employee neutral
                em "Oui, oui, c'est terriblement triste..."
                show Eva pensive
                e "Terriblement triste!"
                show Employee afraid
                em "Notre meilleure cliente!"
                sv "Un moment de silence. Cliquez deux fois pour continuer."
                g "..."
                show Eva determ
                e "Alors, tu as une solution pour vaincre les zombies? Parce qu'un autre groupe s'approche rapidement!"
            
            #Antonine survit
            if companionRIP and not clienteRIP and employeeRIP:
                
                show Client intense at right with moveinright
                sv "La cliente la suit de près."
                
                an "Quelle victoire! On en a seulement perdu deux. Un bon ratio de zombies/humains."
                e "C'est quand même dommage. Ils sont dans des tous petits morceaux alors on ne peut même pas les recycler..."
                
                if chosenPath == "Charlie":
                    g "Pauvre réceptionniste!"
                    show Eva determ
                    e "Wilfred."
                elif chosenPath == "Sport":
                    g "Pauvre propriétaire de magasin de sport!"
                    show Eva determ
                    e "Viola."
                else:
                    g "Pauvre pharmacien."
                    show Eva determ
                    e "Joey."
                    
                g "Pauvre employé."
                e "Roméo."
                g "Avec ce que j'ai trouvé, on va peut-être au moins pouvoir éviter d'autres victimes."
            
            #Companion et Roméo survit
            if not companionRIP and clienteRIP and not employeeRIP:
                
                show Employee neutral at center with moveinright
                sv "Suivit de près par l'employée."
                
                if chosenPath == "Charlie":
                    sv "Et le réceptionniste!"
                    show Reception obssessed at right with moveinright
                    r "On a eu le droit à un magnifique combat!"
                elif chosenPath == "Sport":
                    sv "Et la propriétaire!"
                    show Proprio drill at right with moveinright
                    s "On les a eu, on les a eu, on les a eu!"
                else:
                    sv "Et le pharmacien!"
                    show Pharma relieved at rightAway with moveinright
                    p "Les zombies m'ont vraiment attaqués! Ils ne me considèrent pas membre du goupe..."
                
                show Employee afraid
                em "C'était horrible."
                g "Pauvre Antonine."
                show Employee afraid
                em "Antonine?"
                e "Elle est dans la pile de corps juste là."
                em "Eeeep!"
                g "Qu'est-ce qu'on fait maintenant? J'ai imprimé de l'information qui va être utile."
                
            #Companion et Antonine survit
            if not companionRIP and not clienteRIP and employeeRIP:

                show Client trickster at center with moveinright
                sv "Suivit de près par la cliente."

                if chosenPath == "Charlie":
                    sv "Et par le receptionniste!"
                    show Reception obssessed at right with moveinright
                elif chosenPath == "Sport":
                    sv "Et par la propriétaire!"
                    show Proprio drill at right with moveinright
                else:
                    sv "Et par le pharmacien!"
                    show Pharma relieved at rightAway with moveinright
                
                an "Tout ce que tu as ramassé dans le magasin, c'est l'ami Satellite?"
                g "Euh, oui."
                an "Vite, va me ramasser les dernières générations des consoles de jeux vidéos. Et un ordinateur performant."
                an "Roméo n'a pas d'objection, n'est-ce pas Roméo?"
                g "Parce qu'il est mort..."
                
                if chosenPath == "Charlie":
                    r "Moi, j'aimerais bien une tablette avec crayon pour faire mes croquis!"
                elif chosenPath == "Sport":
                    s "UN PEU DE RESPECT!"
                else:
                    p "Je pourrais bien utiliser une nouvelle tablette."
                
                show Eva determ
                e "On n'a pas le temps pour tout ça."
                
            #Companion survit
            if not companionRIP and clienteRIP and employeeRIP:
                
                if chosenPath == "Charlie":
                    sv "suivit de près par le réceptionniste."
                    show Reception obssessed at right with moveinright
                    r "Donnez moi une seconde, je veux prendre des photos."
                    show Eva determ
                    e "Les corps d'Antonine et Roméo qui n'ont pas réussi à survivre? Wow..."
                    show Reception stars
                    r "Mmm, non...j'aime bien comment les ombres des arbres sont projetés contre ce mur."
                    sv "Un moment de silence. Cliquez deux fois pour continuer."
                    g "..."
                    e "...ben là, on a d'autres choses à faire!"
                    
                elif chosenPath == "Sport":
                    sv "suivit de près par la propriétaire."
                    show Proprio unhappy at right with moveinright
                    s "Tellement de victimes. Comment va-t-on en venir à bout?"
                    g "Tu as de quoi sur ton soulier."
                    s "Un morceau d'oreille, je pense."
                    show Proprio drill
                    "Elle a donné un bon kick dans les airs, et l'oreille s'est logée dans le mur!"
                    
                else:
                    sv "suivit de près par le pharmacien."
                    show Pharma relieved at right with moveinright
                    p "Il y avait des zombies partout! Pleins de zombies! Et ils ne m'ont pas touchés!!!"
                    show Pharma happy
                    p "Je me sens bien!!!! JE ME SENS BIEN!!!!"
                    e "Tu tentes ta chance là. Si on était dans un film, un dernier zombie se jetterait sur toi."
                    show Pharma terrified
                    p "EEP!"
                    g "Euh, c'est correct, vous avez vraiment eu l'air de les avoir!"
                    e "Pas toi aussi, Gabriel. Tu vas me manquer!"
                    sv "Un moment de silence. Cliquez deux fois pour continuer."
                    "..."
                    
                g "J'ai probablement la solution!"
            
        #Tout le monde a survécu
        else:
            "Mais juste des corps de zombies!"
            sv "Tout le groupe entre dans le magasin!"
            show Eva pensive at left with moveinright
            show Employee neutral at center with moveinright
            show Client happy at leftMid with moveinright
            
            g "Wow, vous êtes une équipe redoutable!!!"
            
            if chosenPath == "Charlie":
                show Reception happy at right with moveinright
                em "Je voulais vraiment défendre le magasin."
                an "Je voulais vraiment défendre le contenu du magasin — on se ramasse une télévision?"
                r "Moi, je voulais simplement survivre!"
                e "Et moi, je suis curieuse de voir ce que tu as trouvé..."
                
            elif chosenPath == "Sport":
                show Proprio happy at right with moveinright
                s "Ils ont été vraiment impressionants!"
                e "Wow Viola, même si je t'ai vu allé, j'ai de la difficulté à croire le nombre de zombies que tu as personnellement arrêté!"
                em "Est-ce que tu travaille comme garde de sécurité?"
                an "Tu fais partie de la mafia?"
                show Proprio satisfaction
                s "Hahahaha. Peut-être bien..."
                e "Et Gabriel, as-tu rempli ta mission?"
                
            else:
                show Pharma happy at rightAway with moveinright
                p "On a passé tellement de temps à obséder à propos des zombies, que c'était presque comme si on pouvait penser comme eux pour mieux les battre!"
                em "Penser comme eux? Parle pour toi-même, j'étais terrifié tout le long!"
                show Pharma afraid
                an "Juste une théorie, mais peut-être que tu deviens un zombie, et c'est pour ça que tu pouvais t'identifier à leurs actions?"
                show Pharma terrified
                e "Ne t'en fait pas comme ça, je sais exactement de quoi tu parles."
                show Pharma relieved
                e "Gabriel, comment ça a été de ton côté?"
            
            g "Après mes recherches, je pense que j'ai trouvé des bonnes idées!"
            

    #On n'avait pas un allié!
    else:
        #Si tout le monde est mort
        if  clienteRIP and employeeRIP:
            "Les zombies...et tous nos nouveaux alliés."
            sv "Évangeline entre dans le magasin."
            show Eva pensive at center with moveinright
            "Est-ce qu'on n'aurait pas dû se sauver avant que je prenne le temps de faire ma recherche?"
            
            e "La victoire nous a coûté très chère."
        
        #Si un allié est mort
        elif clienteRIP or employeeRIP:
            "Les zombies...et une nouvelle connaissance."
            sv "Évangeline entre dans le magasin."
            show Eva pensive at left with moveinright
            e "Ah, te voilà Gabriel!"
    
            #Roméo
            if clienteRIP and not employeeRIP:
                sv "suivit de près par l'employé."
                show Employee afraid at right with moveinright
                em "C'est terrible! Je ne peux pas croire que notre meilleure cliente n'a pas survécu!"
                em "Le futur du magasin est rendu vraiment incertain!"
                e "Gabriel, j'espère que tu as trouvé de quoi qu'on va pouvoir utiliser."
                g "Oui!"
                em "Elle a essayé tellement fort! Tellement fort! À la fin, j'ai crié qu'elle pouvait utiliser mon rabais e'employé si elle survivait."
                e "Ça a eu l'air de la distraire...c'est à cet instant qu'un zombie l'a mordu dans le dos!"
                sv "Un moment de silence. Cliquez deux fois pour continuer."
                g "..."
            
            #Antonine
            if not clienteRIP and employeeRIP:
                sv "suivit de près par la cliente."
                show Client intense at right with moveinright
                an "Quelle victoire! On a seulement perdu une personne!"
                e "Wow, tu semble être une personne très positive!"
                an "Et là, personne ne peut nous empêcher de ramasser quelques morceaux d'équipement supplémentaire!"
                g "Comme quoi? J'ai rapporté l'{i}Ami Satellite 1002 Yay{/i}. Et j'ai des pistes intéressantes..."
                an "J'aimerais avoir quelques disques durs, des appareils photos, des consoles de jeux vidéo..."
                g "Euh...donc rien pour arrêter les zombies..."
            
        #Tout le monde a survécu
        else:
            "Mais juste des corps de zombies!"
            sv "Tout le groupe entre dans le magasin."
            show Eva pensive at left with moveinright
            show Employee neutral at right with moveinright
            show Client trickster at center with moveinright
            
            g "Wow, vous êtes une équipe redoutable!!!"
            em "Rien de tout ça était couvert dans le manuel d'employé!"
            e "C'est toujours bien d'apprendre des nouvelles choses!"
            an "On devrait ramasser de l'équipement à l'intérieur...pour lancer aux zombies lorsqu'on en rencontre d'autres."
            g "Euh, j'ai au moins ramené l'{i}Ami Satellite 1002 Yay{/i}, et quelques possibilités intéressantes."
    
    e "On va aller discuter de la prochaine étape chez moi."
    
    return
    
label en_elect_Concl:

    "The last article prints, I grab my laptop, and run for ElectricMart's entrance."
    
    call sc_electro from _call_sc_electro_3
    "Bodies are everywhere."
    
    call ms_end from _call_ms_end_3
    
    #Vérifier si on a un allié
    if companion:
        #Si tout le monde est mort
        if companionRIP and clienteRIP and employeeRIP:
            "The zombies...and all of our new allies."
            sv "Évangeline steps into the store."
            show Eva pensive at center with moveinright
            "Were the articles I found worth all of this death?"
            
            e "Our victory was costly."
        
        #Si une personne ou plus est morte
        elif companionRIP or clienteRIP or employeeRIP:
            "The zombies...and some of our allies."
            sv "Évangeline steps into the store."
            show Eva pensive at left with moveinright
            e "Oh, hi Gabriel."
        
            #Antonine et Roméo survivent
            if companionRIP and not clienteRIP and not employeeRIP:
                sv "followed closely by the employee and the client."
                show Employee neutral at center with moveinright
                show Client intense at right with moveinright
                
                if chosenPath == "Charlie":
                    g "Wilfred?"
                    sv "Évangeline doesn't know what to say. Click twice to continue."
                    e "..."
                    "That poor receptionist. I should never have invited him to join us!"
                elif chosenPath == "Sport":
                    g "Viola?"
                    an "She got 10 zombies before they got to her! It was incredible to see!"
                    sv "A silent beat. Click twice to continue."
                    "..."
                else:
                    g "The pharmacist?"
                    em "Um, he became a zombie. I think he got bit during the battle? We took care of him..."
                    sv "A silent beat. Click twice to continue."
                    "..."
                
                an "Did you grab the {i}Friend Satellite 1002 Yay{/i}?"
                g "I did. And I've printed information that should come in handy."
                show Employee afraid
                em "I'm still not very comfortable with the idea of stealing a laptop!"
                show Eva determ
                e "That's okay, we can pay back your store once we're finished eliminating the zombie threat."
                show Client trickster
                an "Are you kidding? We'll be heroes!!! Your store is going to give us anything we want!"
                
            #Roméo survit
            if companionRIP and clienteRIP and not employeeRIP:
                sv "Followed quickly by the employee."
                show Employee afraid at right with moveinright
                
                em "AHHHH! I hope I'm not going to be expected to clean up this mess!"
                show Eva determ
                e "Did you find a solution to our problem?"
                
                if chosenPath == "Charlie":
                    g "Yes...poor Antonine. Poor receptionist."
                elif chosenPath == "Pharmacy":
                    g "Yes...poor Antonine. Poor pharmacist."
                else:
                    g "Yes..poor Antonine. Poor Viola."
                    
                show Employee neutral
                em "Yes, yes, it's all terribly sad..."
                show Eva pensive
                e "Really sad!"
                show Employee afraid
                em "Our best client!"
                sv "A silent beat. Click twice to continue."
                g "..."
                show Eva determ
                e "So, did you find a solution or not? Because it looks like another group of zombies is closing in!"

            
            #Antonine survit
            if companionRIP and not clienteRIP and employeeRIP:
                
                sv "Followed quickly by the client."
                show Client intense at right with moveinright
                
                an "What a victory! We only lost two people. A really good zombie/human ratio."
                e "What a waste of potential. They're in tiny little pieces, so we can't even recycle them..."
                
                if chosenPath == "Charlie":
                    g "Poor receptionist!"
                    show Eva determ
                    e "Wilfred."
                elif chosenPath == "Sport":
                    g "Poor sports store owner!"
                    show Eva determ
                    e "Viola."
                else:
                    g "Poor pharmacist."
                    show Eva determ
                    e "Joey."
                    
                g "Poor employee."
                e "Romeo."
                g "With everything I've found, we might at least be able to stop losing people to the zombies."
            
            #Companion et Roméo survit
            if not companionRIP and clienteRIP and not employeeRIP:
                
                sv "Followed quickly by the employee."
                show Employee neutral at center with moveinright
                
                if chosenPath == "Charlie":
                    sv "And the receptionist!"
                    show Reception obssessed at right with moveinright
                    r "What a magnificient battle!"
                elif chosenPath == "Sport":
                    sv "And the sports store owner!"
                    show Proprio drill at right with moveinright
                    s "We got them, we got them, we got them!"
                else:
                    sv "And the pharmacist!"
                    show Pharma relieved at rightAway with moveinright
                    p "The zombies attacked me! It was great! They don't consider me as part of their group at all..."
                
                show Employee afraid
                em "It was horrible."
                g "Poor Antonine."
                show Employee afraid
                em "Antonine?"
                e "She's in that pile of bodies right there."
                em "Eeeep!"
                g "What do we do now? I've printed some stuff that might be useful."
                
            #Companion et Antonine survit
            if not companionRIP and not clienteRIP and employeeRIP:

                sv "Followed quickly by the client."
                show Client trickster at center with moveinright

                if chosenPath == "Charlie":
                    sv "And the receptionist!"
                    show Reception obssessed at right with moveinright
                elif chosenPath == "Sport":
                    sv "And the sports store owner!"
                    show Proprio drill at right with moveinright
                else:
                    sv "And the pharmacist!"
                    show Pharma relieved at rightAway with moveinright
                
                an "The only thing you grabbed in that store, was the Friend Satellite 1002 Yay?"
                g "Um, yes."
                an "Quick, go grab me the latest video game consoles, I want some spares. And a high performing computer."
                an "Romeo won't mind, will he?"
                g "Because he's dead..."
                
                if chosenPath == "Charlie":
                    r "Are you taking orders? I would like a pen and tablet so that I can do some sketches!"
                elif chosenPath == "Sport":
                    s "A LITTLE RESPECT PLEASE!"
                else:
                    p "I could use a new laptop!"
                
                show Eva determ
                e "We don't have time for any of that."
                
            #Companion survit
            if not companionRIP and clienteRIP and employeeRIP:
                
                if chosenPath == "Charlie":
                    sv "Followed quickly by the receptionist."
                    show Reception obssessed at right with moveinright
                    r "Give me a second, I want to take some pictures."
                    show Eva determ
                    e "Of what? Antonine and Romeo's corpses? Wow..."
                    show Reception stars
                    r "Mmm, no...I really like the shadows these trees are making on that wall."
                    sv "A silent beat. Click twice to continue."
                    g "..."
                    e "...we've definitely got better things to do!"
                    
                elif chosenPath == "Sport":
                    sv "Followed quickly by the sports store owner."
                    show Proprio unhappy at right with moveinright
                    s "So many victims."
                    g "You have something on your shoe."
                    s "A piece of ear, I think."
                    show Proprio drill
                    "She kicks the air, and an ear flies away and hits a wall!"
                    
                else:
                    sv "Followed quickly by the pharmacist."
                    show Pharma relieved at right with moveinright
                    p "There were zombies everywhere! Lots of zombies! And they didn't touch me!!!"
                    show Pharma happy
                    p "I feel good!!! I FEEL GREAT!!!!"
                    e "You're pushing your luck there, buddy. If we were in a movie, this is the exact moment where a zombie would jump up and bite you."
                    show Pharma terrified
                    p "EEP!"
                    g "Um, that's okay, you seem to have gotten every last one!"
                    e "Not you too, Gabriel. I'll miss you!"
                    sv "A silent beat. Click twice to continue."
                    "..."
                    
                g "Right, so, I probably have a solution!"
            
        #Tout le monde a survécu
        else:
            "But none of them are Évangeline or our new friends!"
            show Eva pensive at left with moveinright
            show Employee neutral at center with moveinright
            show Client happy at leftMid with moveinright
            
            sv "The group enters the store."
            
            g "Wow, you guys are incredible!!!"
            
            if chosenPath == "Charlie":
                show Reception happy at right with moveinright
                em "I really wanted to defend my store."
                an "I really wanted to defend the contents of the store — let's grab a tv?"
                r "I just really wanted to survive!"
                e "And I'm curious to see what you've found..."
                
            elif chosenPath == "Sport":
                show Proprio happy at right with moveinright
                s "They really were amazing!"
                e "Not as amazing as you, Viola! The things I've seen you do to these zombies...the sheer number that you personally dispatched..."
                em "Have you ever worked as a security guard?"
                an "Did you ever do work for the mafia?"
                show Proprio satisfaction
                s "Hahahaha. Maybe..."
                e "So Gabriel, have you accomplished your mission?"
                
            else:
                show Pharma happy at rightAway with moveinright
                p "We've spent some much time obsessing about zombies, it's almost as if we started thinking like them to better defeat them!"
                em "Think like them? Talk for yourself, I was terrified the whole time!"
                show Pharma afraid
                an "Just a theory, but maybe you're becoming a zombie and that's why you feel like this?"
                show Pharma terrified
                e "Don't worry about it, I know exactly what you mean."
                show Pharma relieved
                e "Gabriel, how did things go for you?"
            
            g "I think there are some good ideas in my search results!"
            

    #On n'avait pas un allié!
    else:
        #Si tout le monde est mort
        if  clienteRIP and employeeRIP:
            "The zombies...and all of our new friends."
            sv "Évangeline enters the store."
            show Eva pensive at center with moveinright
            "Maybe I should have grab the Friend Satellite 1002 Yay and ran instead of taking the time to do the search. Maybe more people would have made it."
            
            e "Our victory comes at a terrible cost."
        
        #Si un allié est mort
        elif clienteRIP or employeeRIP:
            "The zombies...and one of our new friends."
            "Évangeline enters the store."
            show Eva pensive at left with moveinright
            e "Ah, there you are, Gabriel!"

            #Roméo
            if clienteRIP and not employeeRIP:
                sv "Followed by the employee."
                show Employee afraid at right with moveinright
                em "It's awful! I can't believe that our best client is gone!"
                em "I don't know if the store can recover from her death!"
                e "Gabriel, I hope you found some information we'll be able to use."
                g "I think so!"
                em "She tried so hard! So hard! At the end, I yelled that I would let her use my employee rebate if she survived the zombie mob."
                e "I think that's what distracted her...that's the moment a zombie bit her in the back!"
                sv "A silent beat. Click twice to continue."         
                g "..."
            
            #Antonine
            if not clienteRIP and employeeRIP:
                sv "Followed by the client."
                show Client intense at right with moveinright
                an "What a victory! And we only lost one person!"
                e "Wow, you seem like a very positive person!"
                an "And now, no one can stop us from grabbing a few extra supplies from ElectricMart!"
                g "Like what? I brought back the Friend Satellite 1002 Yay. And I think I got some interesting articles..."
                an "I would like a few hard drives, some of the newer cameras, video game consoles..."
                g "Um...so nothing to stop the zombies..."
            
        #Tout le monde a survécu
        else:
            "But none of them are Évangeline or our new friends!"
            sv "The group enters the store."
            show Eva pensive at left with moveinright
            show Employee neutral at right with moveinright
            show Client trickster at center with moveinright
            
            g "Wow, you guys were a fantastic team!!!"
            em "None of this was covered in the employee manual!"
            e "It's always great to learn new things!"
            an "We should grab some more supplies from inside... to throw at the zombies when we meet the next batch."
            an "{size=-4}Let's see if they buy that.{/size}"
            g "Um, well, at least I got the {i}Friend Satellite 1002 Yay{/i}, and some promising articles."
    
    e "Let's go discuss the next steps at my place."
    
    return
    
   
label bil_elect_fail:
                
    if len(fightLost) > 0:
        $myFightLost = fightLost.pop()
        call expression myFightLost from _call_expression
    else:
        if lang == "english":
            "No, no, that's not it."
        else:
             g "Non, non, ce n'est pas ça."
        
    if flagCount == 0 or flagCount == 2 or flagCount == 4 or flagCount == 6:
        $victoryFlag = False
        
    call victoryLost from _call_victoryLost_20
    $flagCount +=1
    
    if lang == "english":
        jump en_elect_rech2
    else:
        jump fr_elect_rech2
    return
    
#Generic fail
label bil_elect_fail_1:
    
    if lang == "english":
        g "I have the feeling that I'm wrong..."
    else:
        g "J'ai le sentiment que je me trompe..."
    
    return
    
#Generic fail
label bil_elect_fail_2:
    
    if lang == "english":
        "I can hear screams outside."
        g "No, this isn't the right option."
    else:
        "J'entends des cris dehors."
        g "Non, non, ce n'est pas la bonne option."
    
    return
    
#Possible death of companion
label bil_elect_fail_3:
    
    if lang == "english":
        if companion:
            if chosenPath == "Charlie":
                r "AHHHHHH!"
            elif chosenPath == "Sport":
                s "NOOOOOOO!"
            else:
                p "IT'S HAPPENING, THEY'RE MAKING ME INTO ONE OF THEM!"
                
            e "OH NO! Not the arm!"
            if mySeed2alt == 0:
                $companionRIP = True
            
        else:
            em "AHHHHHHHH!"
            e "OH NO!"

        g "I have to concentrate hard and really remember the steps to a good research process..."
        
    else:
        if companion:
            if chosenPath == "Charlie":
                r "AHHHHHH!"
            elif chosenPath == "Sport":
                s "NOOOOOOON!"
            else:
                p "JE VAIS VOUS JOINDRE MAINTENANT!"
                
            e "OH NON! Son bras!"
            if mySeed2alt == 0:
                $companionRIP = True
            
        else:
            em "AHHHHHHHH!"
            e "OH NON!"

        g "Je dois me concentrer et BIEN me souvenir des étapes de la recherche..."
    
    return
    
#Generic fail
label bil_elect_fail_4:
    
    if lang == "english":
        an "HIYAAAAAA! TAKE THIS!"
        g "No, no, there's definitely another step that needs to get done first..."
    else:
        an "HIYAAAAAA! PRENDS ÇA!"
        g "Non, non, il y a une autre étape à faire en premier..."
    
    return
    
#Possible death of client
label bil_elect_fail_5:
    
    if lang == "english":
        if mySeed2alt == 1:
            em "OH NO! OUR CLIENT!! WHAT IS MY BOSS GOING TO SAY?"
            $clienteRIP = True
        else:
            an "HAHAHAHAHA! EVEN ZOMBIES CAN'T STOP ME!"
            em "AHHH! WE DON'T USE ELECTRONIC EQUIPMENT TO DO...THAT!"
        "It's hard to concentrate when people scream so much. I think I'm messing up the steps of the research process."
    else:
        if mySeed2alt == 1:
            em "OH NON! NOTRE CLIENTE!! QU'EST-CE QUE MON BOSS VA DIRE?"
            $clienteRIP = True
        else:
            an "HAHAHAHAHA! MÊME DES ZOMBIES NE PEUVENT PAS M'ARRÊTER!"
            em "AHHH! ON N'UTILISE PAS DE L'ÉQUIPEMENT ÉLECTRONIQUE POUR FAIRE...ÇA!"
        "C'est difficile de se concentrer lorsque les gens crient autant. Je me suis trompé dans mes étapes de la recherche."
    
    return
    
#Possible death of employee
label bil_elect_fail_6:
    
    if lang == "english":
        if mySeed3alt >= 1:
            e "CAREFUL! NO, NOT THERE!"
            em "AHHHHHH!"
            $employeeRIP = True
        else:
            e "BE CAREFUL! STOP TRIPPING EVERYWHERE!"
        "I have to hurry! I think I can make the search go faster if I go for a different step in the research process."
    else:
        if mySeed3alt >= 1:
            e "ATTENTION! NON, PAS PAR LÀ!"
            em "AHHHHHH!"
            $employeeRIP = True
        else:
            e "ATTENTION! ARRÊTE DE TRÉBUCHER PARTOUT!"
        "Je dois me dépêcher! Je sens que je peux faire ma recherche de façon plus efficace si je choisis une autre étape en premier."    
    
    return
    
#Generic fail
label bil_elect_fail_7:
    
    if lang == "english":
        e "AHHHHHHHHHHHHHHHHHhhhhhhhhhhhhhhhhhhhhhhhhh"
        sv "A silent beat. Click twice to continue."
        e "..."
        sv "Another silent beat. Click twice to continue."
        g "..."
        "I think this is wrong..."
    else:
        e "AHHHHHHHHHHHHHHHHHhhhhhhhhhhhhhhhhhhhhhhhhh"
        sv "Un moment de silence. Cliquer deux fois pour continuer."
        e "..."
        sv "Un autre moment de silence. Cliquer deux fois pour continuer."
        g "..."
        "Je me suis trompé..."
    
    return

#Generic fail
label bil_elect_fail_8:
    
    if lang == "english":
        g "...this is definitely wrong."
    else:
        g "...je me suis trompé."
    
    return
