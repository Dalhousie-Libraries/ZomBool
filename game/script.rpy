# The game starts here.
 
label start:
    #Keeps track of victory points
    $victory = 0
    $victoryFlag = False

    #Initialize menu choices
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
    
    #Initialize Mad Gab entries
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
    
    #Initialize VennList (defined in Venn Setup in pthJoint)
    $vennList = ""
    $vennMenuList =("","","","")
    $vennMenuOpt = ""
    
    #Set default menu seeds
    $mySeed2 = persistent.mySeed2
    $mySeed2alt = persistent.mySeed2alt
    $mySeed3 = persistent.mySeed3
    $mySeed3alt = persistent.mySeed3alt
    
    #Initialize safe code cracking
    #$flagCount = 0 keeps track of the number of tries
    #If Charlie, safeIC = 0, safeCIB = 0
    #If sport, safeIC = 1, safeCIB = 2
    #If Pharm, safeIC = 2, safeCIB = 3
    $safeNumb = "" #Container for the number returned by clicking on safe numbers (in safe screen)
    $mySafeString = "" #A temporary string of numbers clicked by the user
    $safeButtonLists = [["2,7,8,4,7,*","2,7,8,4,7,8", "2,7,9,4,7,*", "2,7,9,4,7,8"],
        ["7,7,6,7,7,*", "7,7,6,7,7,4", "7,7,6,7,8,*", "7,7,6,7,8,4"],
        ["7,4,3,2,7,6", "7,4,3,2,7,*", "7,4,2,7,6,2", "7,4,2,7,6,*"],
        ["1,1,4,4,3,*", "2,2,4,4,3,3", "2,2,4,4,3,*", "2,2,4,4,3,8"]] #Values to put into the buttons
    $safeIC = -1 #Index Chapter. Controls which set of button values we are working with - set at start of chapter
    $safeCIB = -1 #Correct Index Button. Controls where the right answer is - set at the start of chapter
    $safeWord = ""
    
    $safeWord = "" #Contains the right word for the selected chapter and language
    $myWordString = "" #A temporary string of best guesses for letters from the numbers clicked by the user
    $myIteration = "1" #Allows to increment up
    
    
    #Different dialogue options during ending fight (win)
    if lang == "english":
        $fightWin = [
            "I feel great! Like I just solved another piece of the puzzle.",
            "Yes! I'm the BEST!",
            "I'm flooded with sudden insights about the nature of zombies. Excellent!",
            "I'm so happy I could just drop everything and find a poutinerie that still has electricity and hasn't been overrun and have delicious warm fries!",
            "This is great! As if I had time travelled into my own body to make myself make the right choices.",
            "With this step of the research process completed, I feel like I should be able to just do research super fast in seconds with a training montage or something.",
            "Not even that weird killer robot could have done any better.",
            "Yes!",
            "This is absolutely right!",
            "I've got this! I've really got this!",
            "My whole family is going to be so proud of me!",
            "Everything is going to be just fine, I can feel it.",
            "It feels like everything in my life has brought me to this moment.",
            "The zombies are not going to know what hit them!",
            "I feel like it's going to happen. I'm going to find out how to defeat the zombies."
            ]
    else:
        $fightWin = [
            "Oui! J'ai trouvé un autre morceau du casse-tête!",
            "Super! Personne ne peut m'arrêter!",
            "Je suis rempli d'idées à propos de la nature exacte des zombies. Super!",
            "Je suis tellement content que je pourrais tout oublier et aller trouver une poutinerie qui a encore du pouvoir et qui n'est pas pleine de zombies et me commander des bonnes frites!",
            "C'est parfait! Comme si j'avais voyagé dans le temps dans mon propre corps pour choisir les meilleures options possible!",
            "Dans le futur, j'aimerais bien jouer de la musique entraînante et juste faire mes recherches en quelques secondes.",
            "Je pense que le robot qui voulait nous exterminer pourrait travailler plus rapidement que moi, mais pas beaucoup plus vite!",
            "Oui!",
            "C'est exactement correct.",
            "Je suis capable! Je vais passer à travers le long processus de recherche!",
            "Ma famille va être tellement fière de moi!",
            "Tout va bien se passer.",
            "C'est comme si tout dans ma vie m'a préparé pour cette recherche.",
            "Les zombies ne vont pas pouvoir résister à mes découvertes!",
            "Je pense que je vais y arriver. Je vais trouver une façon de détruire les zombies."
            ]
    
    $renpy.random.shuffle(fightWin)
    $fightWin = fightWin[:9]
    $myFightWin = ""
    
    #To randomize consequences of failing in end fight
    $fightLost = [
        "bil_elect_fail_1",
        "bil_elect_fail_2",
        "bil_elect_fail_3",
        "bil_elect_fail_4",
        "bil_elect_fail_5",
        "bil_elect_fail_6",
        "bil_elect_fail_7",
        "bil_elect_fail_8"
        ]
    
    $renpy.random.shuffle(fightLost)
    $myFightLost = ""
    
    #To add style to segments in final fight
    $fightStart = ""
    $fightEnd = ""
    
    #For an early ending in sports route
    $sports_early = 0
    
    #Initialize characters joining the team in chapter 1 for chapter 2 and keep track of character status
    $companion = False
    $chosenPath = ""
    
    $companionRIP = False
    $EvaRIP = False
    $employeeRIP = False
    $clienteRIP = False
    
    #More kittens
    $kitten = False
    
    call initial_variables from _call_initial_variables #Toggle the menu seeds for next run through
    call language_path from _call_language_path #Send to the right path depending on language
    
    return
    
label en_start:
    #Start of the English path
    #Initializing some variables
    $librarian_name = "Librarian"
    $class_name = "Class"
    $impatient_name = "Impatient Student"
    $creature_name = "Creature"
    $reception_name = "Receptionist"
    $pharmacist_name = "Pharmacist"
    $sportsGo_name = "SportsGo Owner"
    $employee_name = "Employee"
    $client_name = "Client"
    $robot_name = "EVIL BOT"

    $save_name = "Prologue — Intro — Eng"
    
    $renpy.block_rollback()
    
    call sc_black from _call_sc_black_7
    sv "Menus where you must make a choice are announced with the word 'menu'. Go to the next line of dialogue, and then press up on the keyboard to hear the different options."
    sv "During most of the game, you can press down to interact with the quick menu, which allows you to save, change your preferences including the volume of the sound and music, etc."
    sv "When a character is announced as a self-voiced character, it means that punctuation was spelled out. The next line is a repeat and is the original line. Tests with self-voicing revealed that punctuation sometimes needs to be spelled out."
      
    if persistent.ending_achieved:
        "News reports announced that zombies had reached our city while I was studying at my friend's house."
        sv "A silent beat. Click twice to continue."
        "..."
        
        sv "Menu"
        $shuffle_menu()
        menu:
            "I feel weary — as if I've done all of this already."
            "Skip the prologue!":
                $victory = 3
                sv "Menu"
                $shuffle_menu()
                menu:
                    "How do I feel in general about KITTENS?"
                    "Kittens? I LOVE kittens!!!!":
                        $kitten = True
                    "Um, no? No, not for me?":
                        pass
                "We did a bunch of stuff at Évangeline's house. And then..."
    
                jump en_ch1
            "It's fine! I'll keep going!":
                sv "Menu"
                $shuffle_menu()
                menu:
                    "How do I feel in general about KITTENS?"
                    "Kittens? I LOVE kittens!!!!":
                        $kitten = True
                    "Um, no? No, not for me?":
                        pass
    
    call en_prologue from _call_en_prologue
    
    $save_name = "Prologue — The ring"
    call choixMenu from _call_choixMenu_2
    call en_corps from _call_en_corps #Can earn a victory point
    
    $save_name = "Prologue — Part of Everything"
    call cleanMadGab from _call_cleanMadGab_4
    call ms_party from _call_ms_party_12
    call en_rech_livre from _call_en_rech_livre
    call en_rech_article from _call_en_rech_article #Can earn a victory point
    
    $save_name = "Prologue — A Phone Book?"
    call ms_lithium from _call_ms_lithium_3
    call en_phone from _call_en_phone
    
    jump en_ch1

    return
    
label fr_debut:
    #Start of the French path
    #Initializing some variables
    $librarian_name = "Bibliothécaire"
    $class_name = "Classe"
    $impatient_name = "Étudiant impatient"
    $creature_name = "Créature"
    $reception_name = "Réceptionniste"
    $pharmacist_name = "Pharmaciste"
    $sportsGo_name = "Propriétaire de SportsGo"
    $employee_name = "Employé"
    $client_name = "Cliente"
    $robot_name = "ROBOT REDOUTABLE"
        
    $save_name = "Prologue — Intro — Fra"
    
    $renpy.block_rollback()

    
    sv "Les menus où vous devez faire un choix sont annoncés à la ligne précédente avec le mot 'menu'. Changez de ligne, puis cliquez sur la flêche vers le haut sur le clavier pour entendre les différentes options."
    sv "Pendant la plupart du jeu, vous pouvez cliquez la flêche vers le bas pour interagir avec le menu rapide qui vous permet de sauvegarder, de changer les préférences y compris contrôler le volume du son et de la musique, etc."
    sv "Lorsqu'un personnage est annoncé avec la mention 'mode voix', la ponctuation a été écrit au long. La prochaine ligne se répète et est la ligne originale. Des tests avec le mode voix ont déterminés que la ponctuation doit parfois être écrit au long pour être compréhensible."
 
    
    if persistent.ending_achieved:
        call sc_black from _call_sc_black_8
        "Les nouvelles ont annoncé que les zombies étaient rendus dans notre ville pendant que j'étudiais chez mon amie Évangeline."
        sv "Un moment de silence. Cliquez deux fois pour continuer."
        "..."
        sv "Menu"
        $shuffle_menu()
        menu:
            "J'ai une sensation de déjà-vu. Comme si ce n'est pas la première fois que je me retrouve ici."
            "Sauter directement au chapitre 1!":
                $victory = 3
                sv "Menu"
                $shuffle_menu()
                menu:
                    "Est-ce que j'aime bien les minous?"
                    "Oui! J'adore les minous!":
                        $kitten = True
                    "Um, non? C'est pas vraiment mon truc.":
                        pass
                "On a fait plein de choses dans la maison d'Évangeline. Et ensuite..."
                jump fr_ch1
            "Ce n'est pas grave! Je vais continuer!":
                sv "Menu"
                $shuffle_menu()
                menu:
                    "Est-ce que j'aime bien les minous?"
                    "Oui! J'adore les minous!":
                        $kitten = True
                    "Um, non? C'est pas vraiment mon truc.":
                        pass
                
    call fr_prologue from _call_fr_prologue
    
    $save_name = "Prologue — La Bague"
    call choixMenu from _call_choixMenu_3
    call fr_corps from _call_fr_corps #Can earn a victory point
    
    $save_name = "Prologue — Une partie de tout"
    call cleanMadGab from _call_cleanMadGab_5
    call ms_party from _call_ms_party_13
    call fr_rech_livre from _call_fr_rech_livre
    call fr_rech_article from _call_fr_rech_article #Can earn a victory point
    
    $save_name = "Prologue — Un bottin de téléphone?"
    call ms_lithium from _call_ms_lithium_4
    call fr_phone from _call_fr_phone
    
    jump fr_ch1
    return

label fr_ch1:
    $save_name = "Ch1 — En route!"
    call fr_visit_transition from _call_fr_visit_transition
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "Qu'est-ce que je vais faire?"
        "Immédiatement partir à la recherche de l'ami d'Évangeline.":
            $save_name = "Charlie — Une petite visite"
            call fr_visit_Charlie from _call_fr_visit_Charlie
            
            $save_name = "Charlie — Art et OR et AND?"
            call fr_OrAndIntro from _call_fr_OrAndIntro #includes cleanMadGab
            
            $save_name = "Charlie — Fun avec les formulaires"
            call fr_Charlie_Form from _call_fr_Charlie_Form
            
            $save_name = "Charlie — Furieux avec les formulaires"
            call choixMenu from _call_choixMenu_4
            call fr_ch_Form from _call_fr_ch_Form #in pthJoint file, includes a victory point
            call fr_Charlie_ch_Form from _call_fr_Charlie_ch_Form
            
            $save_name = "Charlie — Perdre patience avec les formulaires"
            call choixMenu from _call_choixMenu_5
            call fr_Charlie_ch_Form2 from _call_fr_Charlie_ch_Form2
            
            $save_name = "Charlie et Venn"
            call fr_Venn_Charlie from _call_fr_Venn_Charlie #includes choixMenu and cleanMadGab, leads to 4 victory points
            
            $save_name = "Charlie — Quel est le bon code?"
            call choixMenu from _call_choixMenu_6
            call fr_Charlie_safe from _call_fr_Charlie_safe
            
            $save_name = "Charlie et le réanimateur"
            call fr_Charlie_reanim from _call_fr_Charlie_reanim
            
            $save_name = "Un peu de compagnie sans Charlie?"
            call ms_end from _call_ms_end_7
            sv "Menu"
            $shuffle_menu()
            menu:
                "Je veux retourner chez Évangeline."
                "Inviter le réceptionniste à me joindre.":
                    call fr_Charlie_invitation from _call_fr_Charlie_invitation
                "Souhaiter bonne chance au réceptionniste.":
                    call fr_Charlie_aurevoir from _call_fr_Charlie_aurevoir
            
        "Commencer par trouver une arme pour me défendre des zombies.":            
            $save_name = "SportGo — Mieux vaut une arme?"
            call fr_visit_Sport from _call_fr_visit_Sport
            
            $save_name = "SportGo — Sports et OR et AND?"
            call fr_OrAndIntro from _call_fr_OrAndIntro_1 #includes cleanMadGab
            
            $save_name = "SportGo — Fun avec les formulaires"
            call fr_Sport_form from _call_fr_Sport_form
            
            #Ends game early if wrong option picked
            if sports_early == 1:
                return
            
            $save_name = "SportGo — Se forcer avec un formulaire"
            call choixMenu from _call_choixMenu_7
            call fr_ch_Form from _call_fr_ch_Form_1 #in pthJoint file, includes a victory point
            call fr_Sport_ch_Form from _call_fr_Sport_ch_Form
            
            $save_name = "SportGo — Fatigué des formulaires"
            call choixMenu from _call_choixMenu_8
            call fr_Sport_ch_Form2 from _call_fr_Sport_ch_Form2
            
            $save_name = "SportGo — Combattre le code!"
            call choixMenu from _call_choixMenu_9
            call fr_Sport_safe from _call_fr_Sport_safe
            
            $save_name = "Venn sportif?"
            call fr_Venn_Sport from _call_fr_Venn_Sport #includes choixMenu and cleanMadGab, leads to 4 victory points

            $save_name = "L'union fait la force?"
            call ms_end from _call_ms_end_8
            sv "Menu"
            $shuffle_menu()
            menu:
                "Je veux partir trouver le réanimateur cardiaque."
                "Insister à inviter la propriétaire de SportsGo à me joindre.":
                    call fr_Sport_invitation from _call_fr_Sport_invitation
                "Souhaiter bonne chance à la propriétaire.":
                    call fr_Sport_aurevoir from _call_fr_Sport_aurevoir
            
        "Ma pharmacie a peut-être un réanimateur cardiaque en stock?":
            $save_name = "La pharmacie"
            call fr_visit_Pharm from _call_fr_visit_Pharm
            
            $save_name = "Pharmacie et OR et AND?"
            call fr_OrAndIntro from _call_fr_OrAndIntro_2 #includes cleanMadGab
            
            $save_name = "Pharmacie — Fun avec les formulaires"
            call fr_Pharm_form from _call_fr_Pharm_form
            
            $save_name = "Pharmacie — Tester sa sanité avec un formulaire"
            call choixMenu from _call_choixMenu_10
            call fr_ch_Form from _call_fr_ch_Form_2 #in pthJoint file, includes a victory point
            call fr_Pharm_ch_Form from _call_fr_Pharm_ch_Form
            
            $save_name = "Pharmacie — Fou furieux avec les formulaires"
            call choixMenu from _call_choixMenu_11
            call fr_Pharm_ch_Form2 from _call_fr_Pharm_ch_Form2
            
            $save_name = "Pharmacie — Quel est le bon code?"
            call choixMenu from _call_choixMenu_12
            call fr_Pharm_safe from _call_fr_Pharm_safe
            
            $save_name = "Pharmacie et Venn"
            call fr_Venn_Pharm from _call_fr_Venn_Pharm #includes choixMenu and CleanMadGab, leads to 4 victory points
            
            $save_name = "Pharmacien et réanimateur"
            call fr_Pharm_reanim from _call_fr_Pharm_reanim
            
            $save_name = "Le pharmacient s'en vient?"
            call ms_end from _call_ms_end_9
            sv "Menu"
            $shuffle_menu()
            menu:
                "Je veux retourner chez Évangeline..."
                "Inviter le pharmacien à me joindre.":
                    call fr_Pharm_invitation from _call_fr_Pharm_invitation
                "Me tenir loin d'un zombie potentiel.":
                    call fr_Pharm_aurevoir from _call_fr_Pharm_aurevoir
    
    call cleanMadGab from _call_cleanMadGab_6
    call choixMenu from _call_choixMenu_13
    call fr_ch1_ending from _call_fr_ch1_ending #in pthJoint file
    
    jump fr_ch2
    return

label en_ch1:
    $save_name = "Ch1 — Let's go!"
    
    call en_visit_transition from _call_en_visit_transition
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "What next?"
        "Immediately try to find Évangeline's friend.":
            $save_name = "Charlie — A Quick Visit?"
            call en_visit_Charlie from _call_en_visit_Charlie
            
            $save_name = "Charlie — Art and OR and AND?"
            call en_OrAndIntro from _call_en_OrAndIntro #includes cleanMadGab
            
            $save_name = "Charlie — Fun with Forms"
            call en_Charlie_Form from _call_en_Charlie_Form
            
            $save_name = "Charlie — Furious with Forms"
            call choixMenu from _call_choixMenu_14
            call en_ch_Form from _call_en_ch_Form #in pthJoint file, includes a victory point
            call en_Charlie_ch_Form from _call_en_Charlie_ch_Form
            
            $save_name = "Charlie — Return to Form"
            call choixMenu from _call_choixMenu_15
            call en_Charlie_ch_Form2 from _call_en_Charlie_ch_Form2
            
            $save_name = "Charlie and Venn"
            call en_Venn_Charlie from _call_en_Venn_Charlie #includes choixMenu and cleanMadGab, leads to 4 victory points

            $save_name = "Charlie — What's the right combination?"
            call choixMenu from _call_choixMenu_16
            call en_Charlie_safe from _call_en_Charlie_safe

            $save_name = "Charlie and the defibrillator"
            call en_Charlie_reanim from _call_en_Charlie_reanim
            
            $save_name = "An unexpected new friend?"
            call ms_end from _call_ms_end_10
            sv "Menu"
            $shuffle_menu()
            menu:
                "I need to go back to Évangeline's place."
                "Invite the receptionist to join me.":
                    call en_Charlie_invitation from _call_en_Charlie_invitation
                "Wave goodbye to the receptionist.":
                    call en_Charlie_aurevoir from _call_en_Charlie_aurevoir
            
        "Start by finding a weapon to defend myself.":            
            $save_name = "SportsGo — Better with firepower?"
            call en_visit_Sport from _call_en_visit_Sport
            
            $save_name = "SportsGo — Sports and OR and AND?"
            call en_OrAndIntro from _call_en_OrAndIntro_1 #includes cleanMadGab
            
            $save_name = "SportsGo — Fun with Forms"
            call en_Sport_form from _call_en_Sport_form
            
            #Ends the game if wrong option is picked
            if sports_early == 1:
                return
            
            $save_name = "SportsGo — Fighting with Forms"
            call choixMenu from _call_choixMenu_17

            call en_ch_Form from _call_en_ch_Form_1 #in pthJoint file, includes a victory point
            call en_Sport_ch_Form from _call_en_Sport_ch_Form
            
            $save_name = "SportsGo — Return to form"
            call choixMenu from _call_choixMenu_18
            call en_Sport_ch_Form2 from _call_en_Sport_ch_Form2
            
            $save_name = "SportsGo — Fight the code!"
            call choixMenu from _call_choixMenu_19
            call en_Sport_safe from _call_en_Sport_safe
            
            $save_name = "Is Venn a Sport?"
            call en_Venn_Sport from _call_en_Venn_Sport #includes choixMenu and cleanMadGab, leads to 4 victory points

            $save_name = "Two heads fight better than one?"
            call ms_end from _call_ms_end_11
            sv "Menu"
            $shuffle_menu()
            menu:
                "I need to go find the cardiac defibrillator."
                "Insist on inviting the SportsGo owner.":
                    call en_Sport_invitation from _call_en_Sport_invitation
                "Wish good luck to the SportsGo Sports owner.":
                    call en_Sport_aurevoir from _call_en_Sport_aurevoir
            
        "I might find a cardiac defibrillator in a pharmacy?":
            $save_name = "The Pharmacy"
            call en_visit_Pharm from _call_en_visit_Pharm
            
            $save_name = "Pharmacist and OR and AND?"
            call en_OrAndIntro from _call_en_OrAndIntro_2 #includes cleanMadGab
            
            $save_name = "Pharmacist — Fun with Forms"
            call en_Pharm_form from _call_en_Pharm_form
            
            $save_name = "Pharmacist — In Good Form?"
            call choixMenu from _call_choixMenu_20
            call en_ch_Form from _call_en_ch_Form_2 #in pthJoint file, includes a victory point
            call en_Pharm_ch_Form from _call_en_Pharm_ch_Form
            
            $save_name = "Pharmacist — Furious with the Form"
            call choixMenu from _call_choixMenu_21
            call en_Pharm_ch_Form2 from _call_en_Pharm_ch_Form2
            
            $save_name = "Pharmacist — Numb to the Numbers!"
            call choixMenu from _call_choixMenu_22
            call en_Pharm_safe from _call_en_Pharm_safe
            
            $save_name = "Pharmacist and Venn"
            call en_Venn_Pharm from _call_en_Venn_Pharm #includes choixMenu and CleanMadGab, leads to 4 victory points
            
            $save_name = "Pharmacist and ressucitation"
            call en_Pharm_reanim from _call_en_Pharm_reanim
            
            $save_name = "Take the pharmacist out of the pharmacy?"
            call ms_end from _call_ms_end_12
            sv "Menu"
            $shuffle_menu()
            menu:
                "I need to go back to Évangeline's place..."
                "Invite the pharmacist to join me.":
                    call en_Pharm_invitation from _call_en_Pharm_invitation
                "Stay far away from a potential zombie.":
                    call en_Pharm_aurevoir from _call_en_Pharm_aurevoir
    
    call cleanMadGab from _call_cleanMadGab_7
    call choixMenu from _call_choixMenu_23
    call en_ch1_ending from _call_en_ch1_ending #in pthJoint file
    
    jump en_ch2
    return

label fr_ch2:
    
    #In electroWorld file
    $save_name = "Une autre direction."
    call choixMenu from _call_choixMenu_24
    call cleanMadGab from _call_cleanMadGab_8
    call fr_elect_trans from _call_fr_elect_trans
    
    $save_name = "Un autre plan."
    call fr_elect_plan from _call_fr_elect_plan
    
    $save_name = "Un autre opérateur booléen."
    call fr_quotation from _call_fr_quotation
    
    $save_name = "Un étrange ami."
    call choixMenu from _call_choixMenu_25
    call fr_elect_ami from _call_fr_elect_ami #1 victory point
    
    $save_name = "Une autre étape..."
    call fr_elect_rech from _call_fr_elect_rech
    
    if persistent.ending_achieved:
        call sc_black from _call_sc_black_9
        sv "Menu"
        $shuffle_menu()
        menu:
            "J'ai de nouveau un sentiment de déjà-vu. Je connais tellement bien les étapes de recherche que je peux simplement m'assir et chercher..."
            "S'assir, et chercher, et sauter cette séquence.":
                scene bg electro3 with fade
                $victory += 2
                
                "J'espère que ma décision n'aura pas de conséquences..."
                if mySeed2alt == 1:
                    $companionRIP = True
                    
                if mySeed3 == 1:
                    $clienteRIP = True
                
                if mySeed3alt == 1:
                    $employeeRIP = True
                
                call fr_elect_Concl from _call_fr_elect_Concl
                jump the_end
                
            "Ignorer le sentiment de déjà-vu et penser aux étapes de recherche.":
                call sc_electro from _call_sc_electro_4
    else:
        sv "Menu"
        $shuffle_menu()
        menu:
            "Est-ce que je veux réellement une 'bataille' finale palpitante (?) dans laquelle je pense aux étapes de recherche? Ou bien est-ce que 
             je veux simplement relaxer et me rendre à la conclusion?"
            "S'assir, et sauter la recherche, et relaxer jusqu'à la conclusion.":
                scene bg electro3 with fade
                $victory += 2
                
                "J'espère que ma décision n'aura pas de conséquences..."
                if mySeed2alt == 1:
                    $companionRIP = True
                    $victory -=1
                    
                if mySeed3 == 1:
                    $clienteRIP = True
                    $victory -= 1
                
                if mySeed3alt == 1:
                    $employeeRIP = True
                    $victory -=1
                
                call fr_elect_Concl from _call_fr_elect_Concl_1
                jump the_end
                
            "Whoa, on ne va pas sauter les étapes de recherche!":
                call choixMenu from _call_choixMenu_26 
                call fr_elect_rech1 from _call_fr_elect_rech1 #1 victory point
                
                call choixMenu from _call_choixMenu_27 
                call fr_elect_rech2 from _call_fr_elect_rech2  #1 victory point but can lose an additional 4 points
                
                $save_name = "Un survivant?"
                call fr_elect_Concl from _call_fr_elect_Concl_2
                
                jump the_end
    
    return
    
label en_ch2:
    
    #In electroWorld file
    $save_name = "Another direction."
    call choixMenu from _call_choixMenu_28
    call cleanMadGab from _call_cleanMadGab_9
    call en_elect_trans from _call_en_elect_trans
    
    $save_name = "Another plan."
    call en_elect_plan from _call_en_elect_plan
    
    $save_name = "Another boolean operator."
    call en_quotation from _call_en_quotation
    
    $save_name = "A strange friend."
    call choixMenu from _call_choixMenu_29
    call en_elect_ami from _call_en_elect_ami #1 victory point
    
    $save_name = "Another step..."
    call en_elect_rech from _call_en_elect_rech
    
    if persistent.ending_achieved:
        call sc_black from _call_sc_black_10
        sv "Menu"
        $shuffle_menu()
        menu:
            "I have a weird feeling of déjà-vu. I know the steps to a good search with boolean operators so well that I could just sit down and do my search..."
            "Sit down, and do my search, skipping any actual work in a training montage or something.":
                scene bg electro3 with fade
                $victory += 2
                
                "I hope that I won't regret my decision..."
                if mySeed2alt == 1:
                    $companionRIP = True
                    
                if mySeed3 == 1:
                    $clienteRIP = True
                
                if mySeed3alt == 1:
                    $employeeRIP = True
                
                call en_elect_Concl from _call_en_elect_Concl
                jump the_end
                
            "Ignore the feeling of déjà-vu and think about the steps to a good search.":
                call sc_electro from _call_sc_electro_5
                
    else:
        sv "Menu"
        $shuffle_menu()
        menu:
            "Do I REALLY want an epic (?) battle where I think through the steps of the research process? Or do I just want to training montage my
              way to an ending?"
            "Let's skip this as if we were doing a training montage.":
                scene bg electro3 with fade
                $victory += 2
                
                "I hope that I won't regret my decision..."
                if mySeed2alt == 1:
                    $companionRIP = True
                    $victory -=1
                    
                if mySeed3 == 1:
                    $clienteRIP = True
                    $victory -=1
                
                if mySeed3alt == 1:
                    $employeeRIP = True
                    $victory -=1
                
                call en_elect_Concl from _call_en_elect_Concl_1
                jump the_end
                
            "Whoa, let's work our way through to an epic ending!":
                call sc_electro from _call_sc_electro_6
    
                call choixMenu from _call_choixMenu_30
                call en_elect_rech1 from _call_en_elect_rech1 #1 victory point
                
                call choixMenu from _call_choixMenu_31
                call en_elect_rech2 from _call_en_elect_rech2 #1 victory point but can lose an additional 4 points
                
                $save_name = "Any survivors?"
                call en_elect_Concl from _call_en_elect_Concl_2
                
                jump the_end
    
    return
    
label the_end:
    
    call bil_ending from _call_bil_ending
    call bil_credits from _call_bil_credits
    
    return
    

#initvariable.rpy contains initialized pictures, characters, styles, etc.
#language.rpy contains almost everything needed for handling two languages - screens.rpy and options.rpy have a few configurations
#scenes.rpy contains the setup for all scenes - would rather call them
#prologue.rpy contains the initial variable setup and all scenes before the fork
#biblio has all of the library scenes
#pthCharlie contains chapter 1 scenes for trying to find Charlie Waldo
#pthPharm contains chapter 1 scenes for getting a reanimator at the pharmacy
#pthSport contains chapter 1 scenes for trying to find a weapon at a sports shop
#pthJoint contains the code that is common to all 3 branches in chapter 1
#electroWorld contains all of chapter 2
#epilogues contains the endings