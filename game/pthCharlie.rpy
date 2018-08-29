label fr_visit_Charlie:
    titleCard "Chapitre 1 de 2{vspace=30}Où est Charlie Waldo?"
    $chosenPath = "Charlie"
    
    stop music fadeout 3
    call sc_street from _call_sc_street_4
    "Je n'ai pas croisé beaucoup de zombies, mais je n'aime pas l'idée d'être séparé d'Évangeline. Je suis en train de briser la règle la plus importante des films d'horreur!"
    "Je ne connais même pas son ami... un étudiant d'art dramatique qui habite dans une résidence pour étudiants de la Faculté des arts ET qui a accès à un défibrillateur cardiaque?"
    "Et Évangeline a oublié de me dire dans quelle chambre il se trouve..."
    
    call sc_Charlie_main from _call_sc_Charlie_main
    
    call ms_ossuary from _call_ms_ossuary_18
    g "Bonjour! Je cherche Charlie Waldo."
    r "Ah bon."
    g "Pouvez-vous me dire où il se trouve?"
    sv "Le réceptionniste sent la peinture."
    show Reception passion
    r "Oui...mais tu dois d'abord participer à notre oeuvre d'art interactive."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Accepter de participer à l'oeuvre d'art interactive?"
        "Accepter de participer.":
            pass
        "Refuser de participer.":
            g "J'ai juste besoin du numéro de sa chambre. Je peux participer à votre oeuvre d'art interactive une autre fois?"
            g "De toute façon, je suis un peu trop préoccupé par tous les zombies."
            show Reception obssessed
            r "Nous sommes des PERSONNES CIVILISÉES et les PERSONNES CIVILISÉES ont du temps à consacrer pour l'Art."
    
    show Reception obssessed
    "Le réceptionniste me regarde très intensément. Je ne veux rien faire pour le provoquer."
    g "Pas de problème! Ça va me faire plaisir de participer à votre oeuvre d'art interactive plutôt que de m'occuper de faire ce que j'ai à faire."
    show Reception stars
    r "Excellent! Je vais donc te demander de remplir ce formulaire."
    g "\"Utilisez une expression de recherche booléenne pour décrire l'étudiant ou l'étudiante que vous désirez rencontrer.\""
    r "La bibliothécaire est venue visiter la plupart des départements de la Faculté des arts."
    r "Elle était MAGNIFIQUE!"
    show Reception happy
    r "Elle nous a expliqué que les expressions de recherche booléenne sont très efficaces pour faire nos recherches."
    r "Savais-tu qu'une fois que tu as créé une expression de recherche booléenne, tu peux la réutiliser dans TOUTES SORTES DE BASES DE DONNÉES? 
       Même Google — après quelques petites modifications."
    r "C'est absolument INCROYABLE."
    show Reception stars
    r "On va visionner son explication ensemble. On aime bien se rassembler à chaque jour pour réécouter l'enregistrement qu'on a fait de son cours."
    "Il a pointé vers une télévision située au plafond. Des annonces défilaient."
    "J'ai simplement besoin de visionner une vidéo et de remplir un formulaire? Ça ne risque pas d'être trop difficile!"
    "Le réceptionniste a appuyé sur un bouton de sa télécommande."
    
    return
    
label en_visit_Charlie:
    titleCard "Chapter 1 of 2{vspace=30}Where in the world is Charlie Waldo?"
    $chosenPath = "Charlie"
    
    stop music fadeout 3
    call sc_street from _call_sc_street_5
    "I don't notice many zombies on the streets, but I don't like splitting up. We're messing with the primordial rule of horror movies!"
    "I don't even know her friend...a theater student who lives in an art dorm AND who has access to a defibrillator?"
    "And Évangeline forgot to tell me what room he's in..."
    
    call sc_Charlie_main from _call_sc_Charlie_main_1
    
    call ms_ossuary from _call_ms_ossuary_19
    g "Hi! I'm looking for Charlie Waldo."
    r "That's nice."
    sv "The receptionist smells like paint."
    g "Could you tell me where he is?"
    show Reception passion
    r "Sure...but first, you have to participate in an interactive performance art piece."
    sv "A silent beat. Click twice to continue."
    g "..."
    
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Agree to participate in an interactive performance art piece?"
        "Agree":
            pass
        "Decline":
            g "I just need his room number. I'll try out your interactive performance art piece some other time."
            g "I'm a bit too distracted by all the zombies to really enjoy it."
            show Reception obssessed
            r "We are CIVILIZED citizens of the world, and CIVILIZED PEOPLE make time to appreciate Art."
    
    show Reception obssessed
    "The receptionist is looking at me pretty intensely. I don't want to do anything that might provoke him."
    g "No problem! Why not?! I'm happy to participate in your Art thing instead of just doing what I came here to do."
    show Reception stars
    r "Great! I'm going to ask you to fill out this form."
    g "\"Use a boolean search expression to describe the student you wish to locate.\""
    r "Most of the departments in the Faculty of Arts were visited by the librarian."
    r "She was MAGNIFICIENT!"
    show Reception happy
    r "She explained that boolean search expressions make research much more efficient."
    r "Did you know that once you've created a boolean search expression, you can recycle it in ALL KINDS OF DATABASES? Even Google, if you make
        some slight modifications first."
    r "It's absolutely MAGICAL."
    show Reception stars
    r "Let's view her explanation together. We really enjoy meeting in this lobby every morning to review the recording we've made of her presentation in one of my classes."
    "He points towards a television hanging from the ceiling."
    "I just need to view a video and fill out a form? That shouldn't be too hard!"
    "The receptionist hits a button on the remote control."
    
    return
                                                           
label fr_Charlie_Form:
    call ms_ossuary from _call_ms_ossuary_20
    call sc_Charlie_main from _call_sc_Charlie_main_2
    show Reception obssessed
    "Le réceptionniste a des larmes dans les yeux."
    show Reception stars
    r "Wow, c'était tellement beau ça! C'est la cinquième fois que je visionne cette performance et je suis encore un peu ému!"
    show Reception happy
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    "Je veux remplir ce stupide formulaire et m'enfuir le plus rapidement possible d'ici."
    "Et là, je comprends enfin pourquoi Évangeline n'a pas pris la peine de me donner un numéro de chambre pour son ami."
    
    call ms_lithium from _call_ms_lithium_5
    call sc_evangeline_flash from _call_sc_evangeline_flash
    e "Ça ne va pas être trop dur de trouver Charlie."
    e "Sa couleur préféré est le {=word}bleu{/=word}."
    e "Il aime le {=word}badminton{/=word}, et le {=word}pickleball{/=word}, et le {=word}tennis{/=word}, et le {=word}ping-pong{/=word}."
    e "Il porte toujours des {=word}lunettes{/=word} et une {=word}casquette{/=word}."
    e "Ok, la voie est libre, tu peux courir jusqu'à la voiture."
    e "Bon voyage!"
    
    call ms_ossuary from _call_ms_ossuary_21
    call sc_Charlie_main from _call_sc_Charlie_main_3
    
    "Je sais maintenant quoi faire!"

    return
    
label en_Charlie_Form:
    call ms_ossuary from _call_ms_ossuary_22
    call sc_Charlie_main from _call_sc_Charlie_main_4
    show Reception obssessed
    "There's a tear or two on the receptionist's cheek."
    show Reception stars
    r "Wow, that was so beautiful! It's my fifth time viewing this performance and it still moves me!"
    show Reception happy
    sv "A silent beat. Click twice to continue."
    g "..."
    "I want to fill out the stupid form and run away from this place as fast as possible."
    "And now, I finally understand why Évangeline never bothered to give me her friend's room number."
    
    call ms_lithium from _call_ms_lithium_6
    call sc_evangeline_flash from _call_sc_evangeline_flash_1
    e "It won't be too difficult to find Charlie."
    e "{=word}Blue{/=word} is his favorite color."
    e "He likes {=word}badminton{/=word}, and {=word}pickleball{/=word}, and {=word}tennis{/=word}, and {=word}ping-pong{/=word}."
    e "He always wears his {=word}glasses{/=word} and a {=word}goatee{/=word}."
    e "Looks like there's a clear path to the car, get ready to run!"
    e "Safe travels!"
    
    call ms_ossuary from _call_ms_ossuary_23
    call sc_Charlie_main from _call_sc_Charlie_main_5
    
    "I know what to do now!"

    return

label fr_Charlie_ch_Form:
            
    #Le réceptionniste félicite la victoire
    if chMenu1 or chMenu2 or chMenu3:
        r "Ça a pris un peu de travail, mais tu as réussi!"
    elif chMenu4:
        r "Wow, tu as réussi sans gaspiller trop de formulaires!"
    else:
        r "Super! Tu as vraiment bien compris la recherche booléenne!"
    
    call sc_Charlie_main from _call_sc_Charlie_main_6
    
    #Charlie redemande le formulaire
    if flagCount == 4:
        g "Bon, puis-je ENFIN avoir le numéro de la chambre de Charlie?"
    elif flagCount == 3:
        g "Je pense qu'une bonne récompense serait le numéro de la chambre de Charlie?"
    elif flagCount == 2:
        g "Tu me donnes le numéro de la chambre de Charlie? Je l'ai vraiment mérité!"
    elif flagCount == 1:
        g "J'ai bien travaillé, alors tu me donnes le numéro de chambre de Charlie?"
    else:
        g "Woohooo! Je suis un véritable expert!"
        g "Alors tu me donnes le numéro de chambre de Charlie?"
    
    show Reception happy
    r "Oui, oui, je te donne le numéro dans quelques secondes."
    r "Il ne te reste qu'à réparer quelques problèmes avec ton formulaire pour finir la pièce d'art interactive en beauté."
    g "QUELS PROBLÈMES?"
    show Reception obssessed
    r "Tu as juste trois petites choses à régler: un problème avec la langue, l'absence de parenthèses, et mon paiement."
    
    return
    
label en_Charlie_ch_Form:
            
    #Le réceptionniste félicite la victoire
    if chMenu1 or chMenu2 or chMenu3:
        r "It took a bit of work, but you got it!"
    elif chMenu4:
        r "Wow, you managed to get the answer without wasting too many forms!"
    else:
        r "Awesome! You really understand boolean searches!"
    
    call sc_Charlie_main from _call_sc_Charlie_main_7
    
    #Charlie redemande le formulaire
    if flagCount == 4:
        g "Finally! Can I get Charlie's room number now?"
    elif flagCount == 3:
        g "I think a great reward would be Charlie's room number?"
    elif flagCount == 2:
        g "Can you give me Charlie's room number? I feel like I've really earned it!"
    elif flagCount == 1:
        g "I worked hard on your form, so will you give me Charlie's room number now?"
    else:
        g "Woohooo! I'm a total expert!"
        g "So will you give me Charlie's room number?"
    
    show Reception happy
    r "Sure, of course. I'll give you the room number in a few seconds."
    r "For the sake of artistic integrity, you just need to fix a few problems with your form."
    g "WHAT PROBLEMS?"
    show Reception obssessed
    r "Just three small things to fix: adding some brackets, capitalization, and my payment."
    
    return
    
label fr_Charlie_ch_Form2:

    if not (chMenu1 and chMenu2 and chMenu3):
        sv "Menu"
    $unshuffle_menu()
    menu:
        "Que veux-tu réparer?"
        "Problèmes avec la langue!" if not chMenu1:
            $chMenu1 = True
            
            g "Un problème avec la langue?"
            show Reception neutral
            r "Absolument!"
            g "Mais j'ai tout écrit en français, et j'ai bien épellé les mots de ma recherche."
            r "Exactement!"
            g "Je ne comprends pas?!"
            show Reception obssessed
            r "Premièrement, on ne doit pas traduire les opérateurs booléens."
            r "{=bool}ET{/=bool} devrait être {=bool}AND{/=bool}. {=bool}OU{/=bool} devrait être {=bool}OR{/=bool}."
            g "Mais on est tous des francophones ici! Et c'est ce que vous avez mis sur le formulaire pour m'aider à construire mon expression!"
            show Reception neutral
            r "Ce n'est pas grave. La plupart des bases de données {i}y compris les bases de données francophones{/i} fonctionnent avec les opérateurs
                {=bool}AND{/=bool} et {=bool}OR{/=bool}."
            r "Le nombre d'exceptions est tellement minuscule que c'est mieux de s'habituer à utiliser les opérateurs booléens {=bool}AND{/=bool} et {=bool}OR{/=bool}."
            r "Mais ce n'est pas tout..."
            show Reception stars
            r "Hmm, j'ai l'enregistrement à quelque part, la bibliothécaire explique ça tellement bien..."
            "Impossible de l'arrêter."
            "Il a appuyé sur un bouton sur sa télécommande." 
            
            call fr_langue from _call_fr_langue_2
            call ms_ossuary from _call_ms_ossuary_24
            call sc_Charlie_main from _call_sc_Charlie_main_8
            
            g "J'ai bien compris. Je te remplis un nouveau formulaire?"
            r "Change simplement tes opérateurs booléens."
            r "Pas besoin de trouver des mots clés en anglais pour ta recherche...cette fois-ci."
            show Reception obssessed
            r "Je suis trop généreux!"
            
            if chMenu2 and chMenu3:
                g "Wow, tu es trop gentil."
                show Reception happy
                r "Merci!"
                sv "Un moment de silence. Cliquez deux fois pour continuer."
                g "..."
                g "Je te fais ça tout de suite!"
            elif chMenu2 or chMenu3:
                g "Je ne veux pas être obligé de refaire 100 fois le travail."
                g "Quel est le dernier problème avec mon formulaire?"
            else:
                g "Bon, quoi d'autre faut-il changer avec le formulaire?"
            
            jump fr_Charlie_ch_Form2
       
        "Absence de parenthèses!" if not chMenu2:
            $chMenu2 = True
            
            g "Des parenthèses? Tu veux que j'ajoute des parenthèses à mon expression de recherche booléenne?"
            show Reception neutral
            r "Oui!"
            g "Où? Comment? Pourquoi?"
            show Reception stars
            r "La bibliothécaire nous a expliqué que c'est comme pour l'ordre des opérateurs en mathématique." 
            r "Pour ne pas mélanger l'ordinateur, il faut lui dire quoi faire en premier et mettre des parenthèses aux bons endroits."
            show Reception neutral
            if not chMenu1:
                r "On doit chercher des synonymes avec {=bool}OU{/=bool} avant d'ajouter des concepts avec {=bool}ET{/=bool}."
            else:
                r "On doit chercher des synonymes avec {=bool}OR{/=bool} avant d'ajouter des concepts avec {=bool}AND{/=bool}."
            g "Alors je mets des parenthèses pour entourer..."
            show Reception passion
            r "Tous les sports, toutes les couleurs, tout le linge."
            show Reception happy
            r "Lorsque plus qu'un mot est utilisé pour l'exprimer, chaque concept mérite d'être tendrement caressée par des parenthèses, pour qu'on 
               sache que tous ces mots font partie d'un même grand concept."
            g "Wow! Je pense que je comprends!"
            
            sv "Menu"
            $unshuffle_menu()
            menu:
                "J'ai compris l'utilisation de parenthèses dans la recherche booléenne?"
                "Oui":
                    pass
                "Non":
                    show Reception neutral
                    r "Tu dis que tu comprends, mais tu n'as pas l'air très convaincu."
                    sv "Un moment de silence. Cliquez deux fois pour continuer."
                    g "..."
                    r "La bibliothécaire nous a laissé un exemple."
                    g "Oh non! Pas une AUTRE vidéo?"
                    show Reception obssessed
                    r "Non, non. Je peux t'expliquer moi-même plutôt que de te montrer une autre de ses merveilleuses présentations."
                    
                    if not chMenu1:
                        r "Si je vais à une animalerie et j'achète un {=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word} {=bool}ET{/=bool} {=word}laisse{/=word}"
                        r "Avec quoi je vais sortir de l'animalerie?"
                        sv "Gabriel est perplexe. Cliquer deux fois pour continuer."
                        g "???"
                        sv "Mode voix réceptioniste. Chien OU ouvre parenthese chat ET laisse ferme parenthese."
                        r "{=word}chien{/=word} {=bool}OU{/=bool} ({=word}chat{/=word} {=bool}ET{/=bool} {=word}laisse{/=word})"
                        r "Je vais avoir un {=word}chien{/=word}. Ou bien je vais avoir un {=word}chat{/=word} et une {=word}laisse{/=word}?"
                        sv "Mode voix réceptioniste. Ouvre parenthèse chien OU chat ferme parenthèse. Et laisse."
                        r "({=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word}) {=bool}ET{/=bool} {=word}laisse{/=word}"
                        r "Je vais avoir un {=word}chien{/=word} ou un {=word}chat{/=word}. Et je vais toujours sortir de l'animalerie avec une {=word}laisse{/=word}!"
                        sv "Un moment de silence. Cliquez deux fois pour continuer."
                        g "..."
                        show Reception neutral
                        r "Tu as l'air encore plus mélangé!"
                        g "Oui. Désolé!"
                        r "La règle est simple. Mets des parenthèses pour entourer tous les synonymes d'un concept."
                        r "Si tu as des {=bool}OU{/=bool}, tu dois entourer tous les mots reliés par des {=bool}OU{/=bool} par des parenthèses."
                        sv "Mode voix réceptioniste. Ouvre parenthèse chien OU chat ferme parenthèse ET laisse."
                        r "({=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word}) {=bool}ET{/=bool} {=word}laisse{/=word}"
                        sv "Mode voix réceptioniste. Ouvre parenthèse école OU université ferme parenthèese. ET ouvre parenthèse réussite OU succèes ferme parenthèse."
                        r "(ecole {=bool}OU{/=bool} université) {=bool}ET{/=bool} (réussite {=bool}OU{/=bool} succès)"
                        g "Je pense que j'ai compris! Merci!"
                        show Reception happy
                    else:
                        r "Si je vais à une animalerie et j'achète un {=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word} {=bool}AND{/=bool} {=word}laisse{/=word}"
                        r "Avec quoi je vais sortir de l'animalerie?"
                        sv "Gabriel est perplexe. Cliquer deux fois pour continuer."
                        g "???"
                        sv "Mode voix réceptioniste. Chien OR ouvre parenthese chat AND laisse ferme parenthese... Je vais avoir un chien. Ou bien je vais avoir unc hat et une laisse?"
                        r "{=word}chien{/=word} {=bool}OR{/=bool} ({=word}chat{/=word} {=bool}AND{/=bool} {=word}laisse{/=word})... Je vais avoir un {=word}chien{/=word}. Ou bien je vais avoir un {=word}chat{/=word} et une {=word}laisse{/=word}?"
                        sv "Mode voix réceptioniste. Ouvre parenthèse chien OR chat ferme parenthèse. AND laisse... Je vais avoir un chien ou un chat. Et je vais toujours sortir de l'animalerie avec une laisse?"
                        r "({=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word}) {=bool}AND{/=bool} {=word}laisse{/=word}... Je vais avoir un {=word}chien{/=word} ou un {=word}chat{/=word}. Et je vais toujours sortir de l'animalerie avec une {=word}laisse{/=word}!"
                        sv "Un moment de silence. Cliquez deux fois pour continuer."
                        g "..."
                        show Reception neutral
                        r "Tu as l'air encore plus mélangé!"
                        g "Oui. Désolé!"
                        r "La règle est simple. Mets des parenthèses pour entourer tous les synonymes d'un concept."
                        r "Si tu as des {=bool}OR{/=bool}, tu dois entourer tous les mots reliés par des {=bool}OR{/=bool} par des parenthèses."
                        sv "Mode voix réceptioniste. Ouvre parenthèse chien OU chat ferme parenthèse ET laisse."
                        r "({=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word}) {=bool}AND{/=bool} {=word}laisse{/=word}"
                        sv "Mode voix réceptioniste. Ouvre parenthèse école OU université ferme parenthèese. ET ouvre parenthèse réussite OU succèes ferme parenthèse."
                        r "(ecole {=bool}OR{/=bool} université) {=bool}AND{/=bool} (réussite {=bool}OR{/=bool} succès {=bool}OR{/=bool} success)"
                        g "Je pense que j'ai compris! Merci!"
                        show Reception happy

            if chMenu1 and chMenu3:
                g "Bon, je vais corriger mon formulaire!"
            else:
                g "Avant de corriger le formulaire, j'aimerais en savoir plus à propos des autres 'problèmes' que tu crois avoir décelés."
                
            jump fr_Charlie_ch_Form2
        
        "Paiement?" if not chMenu3:
            $chMenu3 = True
            
            show Reception stars
            r "Tu me dois $50 pour mes services."
            g "Je n'ai pas $50 sur moi, et on est en plein milieu d'une attaque de zombies?!"
            show Reception neutral
            r "D'accord, je ne vais pas te charger cette fois-ci pour toute l'aide que je suis en train de te fournir."
            
            jump fr_Charlie_ch_Form2
    
    show Reception neutral
    g "Je sais maintenant quoi faire."
    "J'ai réussi à remplir rapidement et correctement le formulaire, y comprit en pensant à des mots clés en anglais, ce qui m'a donné l'expression booléenne suivante:"
    sv "Mode voix narration. Ouvre parenthèse badminton OR pickleball OR tennis OR ping-pong ferme parenthèse. AND ouvre parenthèse lunette OR glasses ferme parenthèse.
        AND ouvre parenthèse casquette OR baseball cap ferme parenthèse. AND ouvre parenthèse bleu OR blue ferme parenthèse."
    "({=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} 
     {=word}ping-pong{/=word}) {=bool}AND{/=bool} ({=word}lunettes{/=word} {=bool}OR{/=bool} {=word}glasses{/=word}) {=bool}AND{/=bool} ({=word}casquette{/=word} {=bool}OR{/=bool}{=word}baseball cap{/=word}) {=bool}AND{/=bool} ({=word}bleu{/=word} {=bool}OR{/=bool} {=word}blue{/=word})"
    show Reception happy
    r "Bravo! Tu as réussi! Et tu vas voir! À ta prochaine visite, tu vas être un peu plus rapide."
    r "J'ai été obligé de te donner BEAUCOUP de mon temps!"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    "Le réceptionniste m'a donné le numéro de chambre de Charlie et des bonnes directions."        
        
    return
    
    
label en_Charlie_ch_Form2:

    if not (chMenu1 and chMenu2 and chMenu3):
        sv "Menu"
    $unshuffle_menu()
    menu:
        "What do you want to fix?"
        "Capitals!" if not chMenu1:
            $chMenu1 = True
            
            g "What's wrong with my capitals?"
            show Reception neutral
            r "Actually, nothing's wrong!"
            sv "A silent beat. Click twice to continue."
            g "..."
            show Reception obssessed
            r "I just want to make sure you know why we capitalize {=bool}AND{/=bool} and {=bool}OR{/=bool}."
            g "So that the computer doesn't search for the {i}words{/i} 'or' and 'and'?"
            r "That's right! Great guess!"
            g "The librarian told us in class. We're using the boolean operators {=bool}AND{/=bool} and {=bool}OR{/=bool}. They're not the {i}words{/i} 'and' and 'or', they're operators. Just like in math, where we have '+' and '-'."
            show Reception stars
            r "YOU'VE MET HER TOO?!"
            sv "A silent beat. Click twice to continue."
            g "..."
            
            if chMenu2 and chMenu3:
                g "So that's it?"
            elif chMenu2 or chMenu3:
                g "So that was easy! What's left on the list now?"
            else:
                g "So is anything actually wrong with the form? What's next?"
            
            jump en_Charlie_ch_Form2
            
        "Brackets!" if not chMenu2:
            $chMenu2 = True
            
            g "Brackets? You want me to add brackets to my boolean search expression?"
            show Reception neutral
            r "Yes!"
            g "Where? How? Why?"
            show Reception stars
            r "The librarian explains that it's the same as the priority of operations in math." 
            r "So we don't confuse the computer, we have to tell it what operation to do first by putting brackets — parentheses actually — in the right spots."
            show Reception neutral
            r "We have to search synonyms with {=bool}OR{/=bool} before adding concepts with {=bool}AND{/=bool}."
            g "So I put parentheses around..."
            show Reception passion
            r "All the sports, the colors if we had more than one, the accessories, and the facial distinctions."
            show Reception happy
            r "If more than one word is used to express it, every idea gets tenderly embraced by parentheses, so that we know that all the different words are part of one big idea."
            g "Wow! I think I get it!"
            
            sv "Menu"
            $unshuffle_menu()
            menu:
                "I understand the use of parentheses in boolean searches?"
                "Yep!":
                    pass
                "Nope!":
                    show Reception neutral
                    r "For someone that gets it, you don't look very convinced."
                    sv "A silent beat. Click twice to continue."
                    g "..."
                    r "The librarian did give us an example."
                    g "Oh no! Not ANOTHER video?"
                    show Reception obssessed
                    r "No. I can explain this myself instead of showing you another one of her magical presentations."

                    r "If I run out to my local animal shelter and buy a {=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word} {=bool}AND{/=bool} {=word}collar{/=word}"
                    r "What will I have with me when I come out of the animal shelter?"
                    sv "Gabriel doesn't know the answer. Click twice to proceed."
                    g "???"
                    sv "Self-voiced . Dog OR open parentheses cat AND collar close parentheses. I'll have a {=word}dog{/=word}. Or the other alternative is that I'll have a {=word}cat{/=word} and a {=word}collar{/=word}?"
                    r "{=word}dog{/=word} {=bool}OR{/=bool} ({=word}cat{/=word} {=bool}AND{/=bool} {=word}collar{/=word})... I'll have a {=word}dog{/=word}. Or the other alternative is that I'll have a {=word}cat{/=word} and a {=word}collar{/=word}?"
                    sv "Self-voiced Receptionist. Open parentheses Dog OR cat close parentheses AND collar. I'll have a {=word}dog{/=word} or a {=word}cat{/=word}. And I'll always come out of the shelter with a {=word}collar{/=word} for it!"
                    r "({=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word}) {=bool}AND{/=bool} {=word}collar{/=word}... I'll have a {=word}dog{/=word} or a {=word}cat{/=word}. And I'll always come out of the shelter with a {=word}collar{/=word} for it!"
                    sv "A silent beat. Click twice to continue."
                    g "..."
                    show Reception neutral
                    r "You look even more confused!"
                    g "Sorry!"
                    r "It's a pretty simple principle. Put parentheses to bracket all synonyms of a concept."
                    r "If you have any {=bool}ORs{/=bool}, you should surround all words linked by {=bool}ORs{/=bool} with parentheses."
                    sv "Self-voiced Receptionist. Open parentheses dog OR cat close parentheses AND collar."
                    r "({=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word}) {=bool}AND{/=bool} {=word}collar{/=word}"
                    sv "Self-voiced Receptionist. Open parentheses school OR university close parentheses AND open parentheses success OR achievement OR accomplishment close parentheses."
                    r "(school {=bool}OR{/=bool} university) {=bool}AND{/=bool} (success {=bool}OR{/=bool} achievement {=bool}OR{/=bool} accomplishment)"
                    g "I think I get it now! Thanks!"
                    show Reception happy
            
            if chMenu1 and chMenu3:
                g "Alright, I'm going to fix my form!"
            else:
                g "Before I fix my form, I want to know more about these other problems you've identified."
                

            jump en_Charlie_ch_Form2
        
        "Payment?" if not chMenu3:
            $chMenu3 = True
            
            show Reception stars
            r "You owe me $50 for my services."
            g "I don't have $50 on me, and we're in the middle of a zombie attack!"
            show Reception neutral
            r "Alright, I won't charge you anything this time for all the help I'm giving you."
            
            jump en_Charlie_ch_Form2
    
    show Reception neutral
    g "I know what to do now."
    "I quickly finish filling out the form correctly, creating the following boolean search expression:"
    sv "Self-voiced narration. Open parentheses badminton OR pickeball OR tennis OR ping-pong close parentheses. AND glasses AND goatee AND blue."
    "({=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} 
     {=word}ping-pong{/=word}) {=bool}AND{/=bool} {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word} {=bool}AND{/=bool} {=word}blue{/=word}"
    show Reception happy
    r "Congratulations! You've succeeded! And just you wait! At your next visit, you won't be so slow to get it."
    sv "A silent beat. Click twice to continue."
    g "..."
    "The receptionist gives me Charlie's room number and some basic directions."        
        
    return

label fr_Venn_Charlie:
    call ms_unpromised from _call_ms_unpromised_1
    call sc_Charlie_corridor from _call_sc_Charlie_corridor
    "Impossible d'ouvrir la porte du couloir menant à la chambre de Charlie."
    "Une tablette est fixée dans la porte avec des instructions."
    g "ARGHH!!!"
    
    call choixMenu from _call_choixMenu_34
    call cleanMadGab from _call_cleanMadGab_12

    $myList = (('{b} Artiste                              Profit{/b}', 'Artiste','Profit'))
    call fr_Venn_Setup from _call_fr_Venn_Setup_2
    call sc_Charlie_corridor from _call_sc_Charlie_corridor_1
    
    "Enfin! J'ai réussi à entrer dans le couloir pour me rendre jusqu'à la chambre de Charlie."
    "J'ai cogné plusieurs fois sans obtenir de réponse."
    
    return

label en_Venn_Charlie:
    call ms_unpromised from _call_ms_unpromised_2
    call sc_Charlie_corridor from _call_sc_Charlie_corridor_2
    "The door to the corridor leading to Charlie's room is locked."
    "There's a tablet attached to the lock with some instructions."
    g "ARGHH!!!"
    
    call choixMenu from _call_choixMenu_35
    call cleanMadGab from _call_cleanMadGab_13

    $myList = (('{b}  Artist                               Profit{/b}', 'Artist','Profit'))
    call en_Venn_Setup from _call_en_Venn_Setup_2
    call sc_Charlie_corridor from _call_sc_Charlie_corridor_3

    "The door unlocks and I FINALLY walk to Charlie's room. I knock on the door several times. There's no answer."
    
    return
    
label fr_Charlie_safe:
    $safeIC = 0
    $safeCIB = 0
    $safeWord = "Artistique"
    
    "Une note sur la porte me dit que je peux entrer en désactivant la serrure avec un code de 6 chiffres."
    "C'est vrai qu'il y a une serrure bizarre sur la porte."
    
    sv "J'examine la serrure. C'est un clavier téléphonique. Les numéros sont associés avec des lettres."
    
    window hide
    scene bg safe with dissolve
    $renpy.pause(2.0)
    window show
    call sc_Charlie_corridor from _call_sc_Charlie_corridor_4
    
    g "ARGHHH!!!!!"
    "Selon la note, le mot de passe est 'Artistique'."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    "..."
    "'Artistique' est composé de 10 lettres! Pas 6 chiffres!"
    
    "Je veux entrer pour voir si Charlie se cache sous son lit avec son défibrillateur cardiaque. Comment je vais m'y prendre?"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    "..."
    "La petite étoile en bas à la gauche...c'est une astérix. Ça me rappèle des souvenirs de la visite de la Bibliothécaire!"
    
    call fr_troncature from _call_fr_troncature_2
    
    call ms_unpromised from _call_ms_unpromised_3
    call sc_Charlie_corridor from _call_sc_Charlie_corridor_5
    "Je sais comment procéder! Je ne dois pas oublier que le mot de passe est 'artistique'."

    sv "Utiliser la flêche vers le haut et la flêche vers le bas pour naviguer sur les différents numéros du clavier électronique dans le prochain écran."
    sv "Après deux entrées incorrectes, 4 codes — 1 des codes est correct — pourront être sélectionné."
    call fr_load_safe from _call_fr_load_safe_4 #in pthJoint
    
    if flagCount <= 1:
        "Ça ne m'a pas pris beaucoup de temps! Je jette un coup d'oeil dans la chambre."
    else:
        "Enfin! Je jette un coup d'oeil dans la chambre."
    "ELLE EST PLEINE DE ZOMBIES."
    g "AHHHHHHHhhhhhh!"
    "Je referme la porte rapidement mais les zombies sont agités et je les entends se masser contre le mur et la porte."
    "Difficile à croire que je ne les ai pas entendu plus tôt! Pourquoi y a-t-il tellement de zombies dans la chambre de Charlie?"
    
    call ms_ossuary from _call_ms_ossuary_25
    call sc_Charlie_main from _call_sc_Charlie_main_9
    "J'ai couru rapidement jusqu'à la réception. Je ne veux pas rester dans cette résidence une seule seconde de plus!"
    show Reception obssessed
    r "Tu es déjà de retour?! Je peux te donner un indice pour la localisation de la chambre de Charlie si tu remplis ce form-"
    g "C'EST PLEINS DE ZOMBIES DANS SA CHAMBRE!"
    show Reception neutral
    sv "Plusieurs moments de silence pendant qu'on s'observe avec consternation. Cliquer 5 fois pour continuer."
    r "!!!"
    g "..."
    r "..."
    g "..."
    r "Je suppose qu'il ne va pas être trop fâché si je ne vais pas faire un tour à son party à la fin de mon shift."
        
    return

label en_Charlie_safe:
    $safeIC = 0
    $safeCIB = 0
    $safeWord = "Artistic"
    
    "A note tells me that I need to deactivate the lock with a 6 digit code."
    "There is indeed a weird-looking mechanism attached to the door knob."
    
    sv "I examine the mechanism. It's a keypad. The numbers are associated with letters."
    
    window hide
    scene bg safe with dissolve
    $renpy.pause(2.0)
    window show
    call sc_Charlie_corridor from _call_sc_Charlie_corridor_6
    
    g "ARGHHH!!!!!"
    "According to the note, the password is 'Artistic'."
    sv "A silent beat. Click twice to continue."
    "..."
    "'Artistic' has 8 letters! Not 6 numbers!"
    
    "I need to get in to see if Charlie is hiding under his bed with his cardiac defibrillator. How am I going to crack the code?"
    sv "A silent beat. Click twice to continue."
    "..."
    
    "The asterix in the bottom left corner...that reminds me of something we learned during the librarian's visit!"
    
    call en_troncature from _call_en_troncature_2
    
    call ms_unpromised from _call_ms_unpromised_4
    call sc_Charlie_corridor from _call_sc_Charlie_corridor_7
    "I now have a good idea how to unlock the door using 'artistic'."

    sv "You will have to enter a code on the screen. Use the up or down arrow on the keyboard to select a different number on the keypad."
    sv "After two wrong attempts, a list of 4 possible codes will appear and can be selected on the screen. One of the codes will be the correct code."
    call fr_load_safe from _call_fr_load_safe_5 #in pthJoint
    
    if flagCount <= 1:
        "That didn't take me too long! I take a look inside Charlie's room."
    else:
        "Finally! I take a look inside Charlie's room."
    "IT'S FILLED WITH ZOMBIES."
    g "AHHHHHHHhhhhhh!"
    "I quickly close the door, but the zombies definitely noticed me. I can hear them massing against the door."
    "Hard to believe that I didn't hear them earlier! Why are there so many zombies in Charlie's room?"
    
    call ms_ossuary from _call_ms_ossuary_26
    call sc_Charlie_main from _call_sc_Charlie_main_10
    "I run back to the reception. I want out of this dorm!"
    show Reception obssessed
    r "Already back?! I can give you a clue about the location of Charlie's room if you complete the following for-"
    g "HIS ROOM IS FILLED WITH ZOMBIES!"
    show Reception neutral
    sv "Several silent beats. Click 5 times to continue."
    r "!!!"
    g "..."
    r "..."
    g "..."
    r "I guess he won't be too mad if I don't drop by his room to party at the end of my shift."
        
    return

    
label fr_Charlie_reanim:
    r "Tu as mes condoléances. Charlie était très sympathique."
    g "Je ne le connaissais même pas. Je voulais juste lui emprunter un défibrillateur cardiaque."
    r "Tu peux prendre le notre, si tu veux."
    g "QUOI?"
    show Reception obssessed
    r "On fait attention à la sécurité des étudiants. On a des cas d'empoisonnement d'alcool à chaque année, des cas d'électrocution, la combustion spontanée..."
    show Reception neutral
    g "QUOI? Tu n'es pas sérieux?!"
    r "Et oui! C'est juste une petite minorité qui boit jusqu'à se rendre malade mais c'est toujours ceux qui aiment le plus raconter des histoires."
    g "Euh...donc, tu as un défibrillateur cardiaque?!"
    r "On a une sérieuse trousse de premier soin et un défibrillateur cardiaque. Tu peux l'avoir si tu veux."
    "Il a fouillé un peu derrière son comptoir et m'a sorti un défibrillateur cardiaque!"
    g "Merci!!!"
    show Reception happy
    "J'ai l'impression d'entendre des craquements de partout. Combien de zombies se promènent dans les couloirs de la résidence?"
    "C'est le temps de repartir trouver Évangeline."
    return
    
label en_Charlie_reanim:
    r "My condoleances. Charlie was a great dude."
    g "I didn't even know the guy. I just wanted to borrow a cardiac defibrillator."
    r "You could take the dorm's defibrillator."
    g "WHAT?"
    show Reception obssessed
    r "We're mindful of student safety. Every year, we deal with alcohol poisoning, electrocutions, spontaneous combustions..."
    show Reception neutral
    g "What? You're joking, right?!"
    r "Alcohol poisoning is no joke! It's just a small number of students that drink too much, but somehow they're always the ones bragging about their drinking stories."
    g "Um...anyway, you have a cardiac defibrillator?!"
    r "Yes, we have a seriously well-equipped first aid kit, and a cardiac defibrillator. You can have it if you want."
    "He looks behind his counter for a bit and comes up with exactly what Évangeline requested!"
    g "Thanks!!!"
    show Reception happy
    "I feel like I can hear shuffling noises coming from all the corridors now. How many zombies are in the dorm? It's definitely time to go."
    return

label fr_Charlie_invitation:
    $companion = True
    g "Tu n'es pas en sécurité ici. Viens avec moi! Mon amie pense qu'elle a une solution qui pourrait nous protéger."
    show Reception neutral
    r "Non, merci. C'est mieux que je reste ici pour avertir les gens qu'ils vont plus loin à leur propre risque."
    show Reception stars
    r "Dans une grosse résidence comme celle-ci, on reçoit beaucoup de visiteurs dans une journée."
    g "Tu pourrais laisser une note!"
    show Reception passion
    r "On a encore le pouvoir, mais pour combien longtemps? Même si je mets une note sur toutes les portes, qui va lire une note dans le noir?"
    g "Les gens ne vont certainement pas se balader dans le noir en plein milieu d'une attaque de zombies. Ils vont avoir des lampes de poches ou ils vont se déplacer pendant le jour."
    show Reception neutral
    r "...d'accord. On va continuer cette aventure ensemble!"
    
    if kitten:
        if flagCount >= 4:
            "Le réceptioniste écrit rapidement une note, puis passe beaucoup de temps à ajouter un dessin d'un chat et des chatons en train de grimper un arbre."
        elif flagCount == 3:
           "Le réceptioniste écrit rapidement une note, puis passe beaucoup du temps à ajouter un dessin d'une abeille en train de danser avec un chat."
        elif flagCount == 2:
            "Le réceptioniste écrit rapidement une note, puis passe beaucoup de temps à ajouter un dessin d'un chat qui saute en bas d'un hélicoptère en train d'exploser."
        elif flagCount == 1:
            "Le réceptioniste écrit rapidement une note, puis ajoute un dessin rapide d'un minou qui s'enfuit d'un zombie en train d'exploser."
        else:
            "Le réceptioniste écrit rapidement une note, puis ajoute un dessin rapide de nous deux et d'un chat en tant que superhéros."
    else:
        if flagCount >= 4:
            "Le réceptioniste écrit rapidement une note, puis passe beaucoup de temps à ajouter un dessin d'un chat en train de grimper un arbre."
        elif flagCount == 3:
           "Le réceptioniste écrit rapidement une note, puis passe beaucoup du temps à ajouter un dessin d'une abeille en train de danser."
        elif flagCount == 2:
            "Le réceptioniste écrit rapidement une note, puis passe beaucoup de temps à ajouter un dessin d'un hélicoptère en train d'exploser."
        elif flagCount == 1:
            "Le réceptioniste écrit rapidement une note, puis ajoute un dessin rapide d'un zombie en train d'exploser."
        else:
            "Le réceptioniste écrit rapidement une note, puis ajoute un dessin rapide de nous deux en tant que superhéros."
    
    show Reception happy
    "On est parti trouver Évangeline."
    
    return
    
label en_Charlie_invitation:
    $companion = True
    g "You're not safe here. Come with me! My friend thinks she might have a solution to the zombie problem."
    show Reception neutral
    r "No, but thanks for thinking of me. It's better that I stay here to warn people to be careful if they want to journey further into the dorm."
    show Reception stars
    r "In a big dorm like this one, we get lots of visitors."
    g "You could leave a note!"
    show Reception passion
    r "We still have power, but for how long? Even if I leave a note on the door who will see it once it gets dark?"
    g "People are not going to be going on leisurely night walks in the middle of a zombie attack. They'll move during the day, or they'll definitely have flashlights!"
    show Reception neutral
    r "...ok. Let's tackle this adventure together!"
    
    if kitten:
        if flagCount >= 4:
            "The receptionist quickly writes a note, and then takes a lot of time decorating it with the image of a cat and some kittens climbing a tree."
        elif flagCount == 3:
           "The receptionist quickly writes a note, and then takes lots of time decorating it with the image of a dancing bee and a dancing kitten."
        elif flagCount == 2:
            "The receptionist quickly writes a note, and then takes a lot of time decorating it with the image of a cat jumping out of an exploding helicopter."
        elif flagCount == 1:
            "The receptionist quickly writes a note, and then decorates it with the image of a cat running around from an exploding zombie."
        else:
            "The receptionist quickly writes a note, and then decorates it with the image of a cat and the two of us as superheroes."
    else:
        if flagCount >= 4:
            "The receptionist quickly writes a note, and then takes a lot of time decorating it with the image of a cat climbing a tree."
        elif flagCount == 3:
           "The receptionist quickly writes a note, and then takes lots of time decorating it with the image of a dancing bee."
        elif flagCount == 2:
            "The receptionist quickly writes a note, and then takes a lot of time decorating it with the image of an exploding helicopter."
        elif flagCount == 1:
            "The receptionist quickly writes a note, and then decorates it with the image of an exploding zombie."
        else:
            "The receptionist quickly writes a note, and then decorates it with the image of the two of us as superheroes."

    
    show Reception happy
    "We leave for Évangeline's place."
    
    return
    
label fr_Charlie_aurevoir:
    g "Bon, je vais y aller. Mais je veux te souhaiter bonne chance!"
    show Reception stars
    r "Pas d'inquiétude, je vais m'assurer d'avertir qui que ce soit qui décide de venir se balader ici qu'on a un problème de zombies."
    g "Sans les forcer à répondre à des questions à propos des opérateurs booléens?"
    show Reception obssessed
    r "Monsieur, on est quand même une résidence pour les étudiants de la Faculté des arts! La liberté d'expression artistique doit être défendue à tout prix!"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    
    "Après avoir remercié une dernière fois le réceptionniste, je suis parti retrouver Évangeline."
    return
    
label en_Charlie_aurevoir:
    g "Well, time to go. But I want to wish you luck!"
    show Reception stars
    r "No worries, I'll make sure to warn whoever shows up here that we have a bit of a zombie problem."
    g "Without forcing them to answer questions about boolean operators?"
    show Reception obssessed
    r "Sir, we are still a dorm for art students! Artistic freedom must be defended at all costs !"
    sv "A silent beat. Click twice to continue."
    g "..."
    
    "After thanking the receptionist one last time, I leave for Évangeline's place."
    return

