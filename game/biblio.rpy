#Use a relevant book chapter of a more general book
label fr_rech_livre:
    call sc_class from _call_sc_class_2
    show Librarian intense
    
    sv "La bibliothécaire semble professionelle et tient une tablette dans ses mains."
    
    $myList = (('rouge','vert', 'la toxicomanie', 'la dépendance à la cocaine'),
        ('de cuivre', 'd\'argent', 'le marketing publié assez récemment', 'l\'utilisation des médias sociaux pour la promotion de produits'))
    
    $entry1 = myList[mySeed2][0]
    $entry2 = myList[mySeed2][1]
    $entry3 = myList[mySeed2][2]
    $entry4 = myList[mySeed2][3]
     
    b "J'ai ici un robot QUI N'EN PEUT PLUS avec l'humanité et qui veut vous...éliminer."
    ro "Beep? Beep Beep!"
    cl "Ahhhhhhh! AHHHHHH!"
    b "On peut le...désarmer... en coupant le fil [entry1] ou peut-être le fil [entry2] qui connecte son processeur avec le reste de son corps!"
    b "Je dois admettre que je ne suis pas trop certaine comment ce robot fonctionne."
    ro "BEEP???"
    cl "AHHHHHHH!"
    
    show Librarian neutral
    b "Non, non, ne paniquez pas comme ça, j'utilise simplement cet example très réaliste pour expliquer mon prochain point."
    b "Vous trouvez un livre intitulé {=book}Comment désarmer un robot{/=book}. Est-ce que vous allez le consulter?"
    
    call victoryReset from _call_victoryReset_6
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Consulter {=book}Comment désarmer un robot{/=book}?"
        "Oui!":
            call victoryWon from _call_victoryWon_8
            cl "On va consulter le livre!"
            sv "La bibliothécaire semble contente."
            show Librarian smiling
        "Non!":
            call victoryLost from _call_victoryLost_21
            cl "On ne va pas consulter le livre!"
            b "QUOI? Vous voulez ÊTRE ÉLIMINÉS???"
    
    show Librarian neutral
    b "Bien entendu, on va consulter ce livre! Même si les processeurs avec fils [entry1] et [entry2] ne sont pas spécifiquement mentionnés dans le titre, 
       on pourrait simplement vérifier dans la table des matières si {=book}Comment désarmer un robot{/=book} comprend un chapitre qui explique comment désarmer {i}notre{/i} robot."
    show Librarian smiling
    ro "BEEP? BEEP! BEEP! BEEP!!!!"
    
    
    show Librarian neutral
    b "C'est la même chose lorsque vous avez des questions très spécifiques de recherche."
    b "Vous devrez parfois consulter des livres plus généraux et trouver votre réponse dans un chapitre ou une section du livre."
    b "Par exemple, un livre sur [entry3] pourrait être utile pour une recherche à propos de [entry4]."
    
    if mySeed2 == 0:
        b "{size=-4}Dommage qu'on ne peut pas guérir la dépendance avec seulement des livres...{/size}"
    else:
        b "{size=-4}Vous pourriez ajouter la bibliothèque comme amie dans vos médias sociaux?{/size}"
    
    return
    
#Use a relevant book chapter of a more general book

label en_rech_livre:
    call sc_class from _call_sc_class_3
    show Librarian intense
    
    sv "The librarian seems professional and holds a tablet in her hands."
    
    $myList = (('red','green', 'religions', 'Buddhism'),
        ('copper', 'gold', 'marketing published recently', 'the use of social media to promote products'))
    
    $entry1 = myList[mySeed2][0]
    $entry2 = myList[mySeed2][1]
    $entry3 = myList[mySeed2][2]
    $entry4 = myList[mySeed2][3]
     
    b "I have here a robot who just can't handle humanity anymore and wishes to...eliminate you."
    ro "Beep? Beep Beep!"
    cl "Ahhhhhhh! AHHHHHH!"
    b "We can...disarm him...by cutting the [entry1] wire or maybe the [entry2] wire that connects his processor to the rest of his extremely advanced robot body."
    ro "BEEP???"
    b "I'll admit that I'm not entirely sure what these different wires do."
    cl "AHHHHHHH!"
    
    show Librarian neutral
    b "Oh no, there's no need to panic, I'm using this very realistic example to illustrate my next point."
    b "You find a book titled {=book}How to defuse a robot{/=book}. Are you going to take a look?"
    
    call victoryReset from _call_victoryReset_7
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Consult {=book}How to defuse a robot{/=book}?"
        "Sure!":
            call victoryWon from _call_victoryWon_9
            cl "We'll take a look!"
            sv "The librarian seems happy."
            show Librarian smiling
        "No!":
            call victoryLost from _call_victoryLost_22
            cl "We're not going to read that book!"
            b "WHAT? Do you want to be ELIMINATED???"
    
    show Librarian neutral
    b "Of course you'll take a look at that book! Even if processors with [entry1] wires and [entry2] wires aren't explicitly mentioned in the title, 
       we could simply check the table of contents to see if {=book}How to defuse a robot{/=book} explains how to disarm {i}our{/i} robot."
    show Librarian smiling
    ro "BEEP? BEEP! BEEP! BEEP!!!!"
    
    show Librarian neutral
    b "It's the same thing when you have very specific research questions."
    b "You'll sometimes need to consult books on more general topics and hope to find an answer in a chapter or a section of the book."
    b "For example, a book about [entry3] could be useful when looking up information about [entry4]."
    
    if mySeed2 == 0:
        b "{size=-4}I had a Buddhist classmate once. Loved soccer and bird watching.{/size}"
    else:
        b "{size=-4}Should I tell them to friend their libraries on social networks?{/size}"
    
    return

#Combine several relevant articles
label fr_rech_article:
    cli "Mes professeurs ne me demandent jamais si je peux trouver des livres sur mon sujet. Mes professeurs veulent des articles."
    b "Ah oui, les articles...Vous savez, la recherche, c'est un peu comme si on voulait compléter un casse-tête."
    show Librarian intense
    sv "Il y a de la tension dans la voix de la bibliothécaire."
    b "Mais les morceaux du casse-tête se trouvent dans pleins de boîtes différentes qui contiennent aussi des morceaux pour d'autres casse-têtes..."
    cli "Mes professeurs me demandent des articles, pas des morceaux de casse-têtes."
    b "Euh, oui, d'accord. Je vais vous donner un exemple concret. Toujours avec notre robot qui peut être neutralisé en coupant un fil [entry1] ou un fil [entry2]."
    show Librarian neutral
    b "On trouve un article intitulé {=book}Robots avec processeurs à fil [entry2]{/=book}."
    b "Voulez-vous consulter cet article pour vous aider à désarmer le robot qui veut vous exterminer?"
    ro "BEEEEEEEEEP!!!"
   
    call victoryReset from _call_victoryReset_8
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Consulter l'article {=book}Robots avec processeurs à fil [entry2]{/=book}?"
        "Oui!":
            call victoryWon from _call_victoryWon_10
            cl "Oui! Le robot a un fil [entry2] alors l'article devrait nous donner quelques indices."
            show Librarian smiling
            b "Bravo! Vous avez bien compris."
        "Non!":
            call victoryLost from _call_victoryLost_23
            cl "Non! On n'a pas oublié que le processeur du robot a un fil [entry2] ET un fil [entry1]."
            b "Vous ne semblez pas avoir compris la métaphore du casse-tête."
    
    show Librarian intense
    b "Pour effectuer une belle recherche, on doit souvent réunir des morceaux de plusieurs sources d'information jusqu'à ce qu'on réussisse à se construire une idée complète d'un sujet."
    b "On trouve l'information à propos des fils [entry2] dans {=book}Robots avec processeurs à fil [entry2]{/=book}, et on peut simplement 
       trouver l'information qui nous manque à propos des fils [entry1] dans un autre article."

    show Librarian smiling
    b "Aimeriez-vous un autre exemple?"
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Un autre exemple?"
        "Bof, pourquoi pas?":
            cl "Bof, pourquoi pas, on aimerait bien un autre exemple."
            b "Merci de me faire confiance! On apprend pleins de choses intéressantes ensemble!!!!"
            call fr_rech_article_exp from _call_fr_rech_article_exp
        "Oui!":
            cl "Ouiiii! C'est tellement intéressant ce que tu nous racontes!"
            show Librarian intense
            b "Intéressant, et tellement utile!"
            call fr_rech_article_exp from _call_fr_rech_article_exp_1
        "Non merci!":
            cl "Ce n'est pas nécessaire, on a bien compris!"
            show Librarian neutral
            b "D'accord... c'est bien correct."
            
    ro "...beep?"
    return
    
#Combine several relevant articles
label en_rech_article:
    cli "Well MY professors never ask me to find books on a topic. MY professors require articles."
    b "Ah yes, articles...you know, research is a bit like working on a puzzle."
    sv "The librarian's voice sounds tense."
    show Librarian intense
    b "But the puzzle pieces are scattered in many different boxes that also contain puzzle pieces for other puzzles..."
    cli "MY professors require articles, not puzzle pieces."
    b "Um, sure, of course. Let me give you a realistic scenario using our robot who has a processor with a [entry1] wire and a [entry2] wire."
    show Librarian neutral
    b "We find an article titled {=book}Wiring robots with a [entry2] wire{/=book}."
    b "Do you think that reading this article might help you disarm this DEFINITELY DANGEROUS robot?"
   
    call victoryReset from _call_victoryReset_9
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Read article titled {=book}Wiring robots with a [entry2] wires{/=book}?"
        "Sure!":
            call victoryWon from _call_victoryWon_11
            cl "Sure! The robot has a [entry2] wire so the article might give us a few hints on how to proceed."
            show Librarian smiling
            b "Great! You've got it."
        "No!":
            call victoryLost from _call_victoryLost_24
            cl "No! We haven't forgotten that the robot's processor has both a [entry2] wire AND a [entry1] wire."
            b "I'm not sure you've gotten the point of the puzzle metaphor."

    show Librarian intense
    b "For our searches to be effective, we often need to put together many different sources of information until we manage to get a pretty good overall understanding of a given topic."
    b "If we find information about [entry2] wires in {=book}How to disarm robots that have a processor with a [entry2] wire{/=book}, we can simply 
       find our missing information about [entry1] wires in another article."

    show Librarian smiling
    b "Would you like another example?"
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Another example?"
        "Well...maybe?":
            cl "Why not, sure, give us another example."
            b "Thanks for trusting me! We're learning so many interesting things together!"
            call en_rech_article_exp from _call_en_rech_article_exp
        "Sure!":
            cl "Yesssss! Everything you're telling us is so relevant!"
            show Librarian intense
            b "Relevant, and extremely useful!"
            call en_rech_article_exp from _call_en_rech_article_exp_1
        "No thanks!":
            cl "Not necessary, we get it already!"
            show Librarian neutral
            b "Alright... that's fine."
            
    ro "...beep?"
    return

#Combine several relevant sources - example
label fr_rech_article_exp:
    b "Alors, un autre exemple!"
    b "Une question de recherche à propos des causes de {=word}l'obésité{/=word} chez les {=word}adolescents{/=word} du {=word}Nouveau-Brunswick{/=word} pourrait nécessiter de combiner l'information trouvée dans plusieurs sources."
    show puzzle1 at combine1
    b "1. Une thèse à propos des liens entre {=word}l'obésité{/=word} et les boissons gazeuses."
    show puzzle2 at combine2
    b "2. Un article à propos de la fréquence {=word}d'exercice{/=word} des {=word}adolescentes{/=word} dans les écoles secondaires."
    show puzzle3 at combine3
    b "3. Un article partageant les taux {=word}d'obésité{/=word} des {=word}provinces canadiennes{/=word}."
    show puzzle4 at combine4
    b "4. Un livre à propos des causes de {=word}l'obésité{/=word} chez les {=word}adolescents{/=word}."
    
    sv "Des morceaux de casse-tête qui contiennent chacun de ces documents apparaîssent dans les coins de l'écran, puis se combinent au centre pour compléter un casse-tête."
    
    show puzzle1 at combine_center1 with move
    show puzzle2 at combine_center2 with move
    show puzzle3 at combine_center3 with move
    show puzzle4 at combine_center4 with move
    b "Par elles-mêmes, ces sources d'information ne répondent pas parfaitement à notre question de recherche."
    b "Mais elles peuvent être combinées pour nous aider à bien comprendre la situation."
    return
    
#Combine several relevant sources - example
label en_rech_article_exp:
    b "So, another example!"
    b "A research question about the risk factors for {=word}obesity{/=word} in {=word}New Brunswick{/=word} {=word}teenagers{/=word} could require combining knowledge gleaned from the following sources of information."
    show puzzle1 at combine1
    b "1. A thesis about the links between {=word}obesity{/=word} and soft drinks."
    show puzzle2 at combine2
    b "2. An article about the decreased {=word}exercise frequency{/=word} of high school {=word}teen{/=word} girls."
    show puzzle3 at combine3
    b "3. An article sharing {=word}obesity{/=word} rates by {=word}province{/=word}."
    show puzzle4 at combine4
    b "4. A book about the causes of {=word}obesity{/=word} in {=word}young adults{/=word}."
    
    sv "Four scattered puzzle pieces containing each of these documents appears on the screen, and combine together in the center, completing the puzzle."
    show puzzle1 at combine_center1 with move
    show puzzle2 at combine_center2 with move
    show puzzle3 at combine_center3 with move
    show puzzle4 at combine_center4 with move
    b "Individually, none of these sources of information fully answer our question."
    b "But once combined, they give us a pretty good picture of the situation!"
    return
    
label fr_OrAndIntro:
    call cleanMadGab from _call_cleanMadGab
    call ms_party from _call_ms_party
    call sc_class from _call_sc_class_4
    b "J'aime introduire l'opérateur booléen {=bool}OR{/=bool} avec l'exemple d'un amoureux en train de trouver une petite 
       gâterie dans une pâtisserie."
    call sc_bakery from _call_sc_bakery
    show Librarian smiling at right
    with move
    b "\"Ramène-moi quelque chose de bon,\" lui dit son chum."
    b "\"Du gâteau, {=bool}ou{/=bool} bien des éclairs, {=bool}ou{/=bool} des truffles, {=bool}ou{/=bool} des tartelettes au 
       citron, {=bool}ou{/=bool} des muffins!\""
    sv "Menu"
    $shuffle_menu()
    menu:
        b "Lequel des choix suivant pourrait satisfaire le besoin d'un gâteau, ou des éclairs, ou des
            truffles, ou des tartelettes au citron, ou des muffins?"
        "Du gâteau?":
            show Librarian intense
            b "Bien entendu!"
            b "{size=-4}J'ai fait mon propre gâteau d'anniversaire, il était délicieux...{/size}"
        "Des éclairs?":
            show Librarian intense
            b "Absolument!"
            b "Mais je ne vais jamais comprendre pourquoi je peux acheter des éclairs mais pas du tonnerre?"
        "Des truffles?":
            show Librarian intense
            b "Vous avez bien raison!"
            b "Vous savez, les truffles font une excellente récompense lorsqu'une bibliothécaire vient vous visiter..."
        "Des tartelettes à l'érable?":
            show Librarian intense
            b "Le chum voulait des tartelettes au citron, pas à l'érable!"
        "Des muffins?":
            show Librarian intense
            b "Oui, oui!"
            b "Pleins de sortes de muffins existent, alors le chum aurait été en mesure d'être encore plus spécifique."
            b "Après tout, vous ne voudriez pas d'un muffin au raisin plutôt qu'un délicieux muffin aux pépittes de chocolat!"
    
    show Librarian neutral
    b "L'amoureux avait BEAUCOUP d'options pouvant faire plaisir à son chum."
    b "L'opérateur booléen {=bool}OR{/=bool} (ou) veut simplement dire \"n'importe lesquelles de ces options vont me faire plaisir\""
    
    show Librarian smiling
    b "Maintenant, imaginez une mère en train d'essayer de choisir un gâteau pour sa fille dans cette même pâtisserie."
    b "\"Je veux un gâteau\", n'est pas une demande très difficile à remplir."
    
    if kitten:
        b "Mais \"Je veux un gâteau, {=bool}et{/=bool} ça doit être un gâteau au chocolat {=bool}et{/=bool} je veux des sprinkles
            sur mon gâteau, {=bool}et{/=bool} des cerises {=bool}et{/=bool} un dessin d'Iron Man en train de battre une tortue ninja
           {=bool}et{/=bool} du glaçage à la vanille {=bool}et{/=bool} plein de chatons...\""
    else:
        b "Mais \"Je veux un gâteau, {=bool}et{/=bool} ça doit être un gâteau au chocolat {=bool}et{/=bool} je veux des sprinkles
            sur mon gâteau, {=bool}et{/=bool} des cerises {=bool}et{/=bool} un dessin d'Iron Man en train de battre une tortue ninja
           {=bool}et{/=bool} du glaçage à la vanille...\""
        
    b "Ça va être un peu plus difficile à trouver."
    
    if kitten:
        sv "Menu"
        $shuffle_menu()
        menu:
            b "Lequel des choix suivant répondrait au désir de la petite fille d'avoir un gâteau au chocolat avec sprinkles,
                et cerises et Iron Man en train de battre des tortues ninja et du glaçage à la vanille et pleins de chatons?"    
            "Un gâteau à la vanille avec glaçage au chocolat et une tortue et des minous qui battent Iron Man?":
                b "\"Je voulais un gâteau au chocolat\", pleure la petite fille."
            "Un gâteau au chocolat avec sprinkles, et cerises, et du glaçage à la vanille?":
                b "\"Où est Iron Man? Et les chatons?\" pleure la petite fille."
            "Un gâteau au chocolat avec cerises, glaçage à la vanille, et Iron Man et des chatons en train de battre une tortue?":
                b "\"Tu as oublié les sprinkles\", pleure la petite fille"
            "Un panier remplit de chatons?":
                b "\"Mais je n'ai pas de gâteau?\", pleure la petite fille"
            "C'est impossible à trouver!":
                pass
    else:
        sv "Menu"
        $shuffle_menu()
        menu:
            b "Lequel des choix suivant répondrait au désir de la petite fille d'avoir un gâteau au chocolat avec sprinkles,
                et cerises et Iron Man en train de battre des tortues ninja et du glaçage à la vanille?"    
            "Un gâteau à la vanille avec glaçage au chocolat et une tortue en train de battre Iron Man?":
                b "\"Je voulais un gâteau au chocolat\", pleure la petite fille."
            "Un gâteau au chocolat avec sprinkles, et cerises, et du glaçage à la vanille?":
                b "\"Où est Iron Man?\" pleure la petite fille."
            "Un gâteau au chocolat avec cerises, glaçage à la vanille, et Iron Man en train de battre une tortue?":
                b "\"Tu as oublié les sprinkles\", pleure la petite fille"
            "C'est impossible à trouver!":
                pass

    
    show Librarian intense at center
    with move
    b "La petite fille a été beaucoup trop exigente, alors la mère s'est retrouvée avec très peu...
       voir zéro options pouvant lui faire plaisir."
    b "L'opérateur booléen {=bool}AND{/=bool} (et) veut dire : \"l'on doit respecter TOUS 
       ces critères pour me faire plaisir.\""
    
    show Librarian smiling

    $myList = (('adolescents','ado', 'adolescence', 'teens', 'teenagers', 'youths', 'Nouveau Brunswick', 'New Brunswick','du'),
        ('enfants', 'enfance', 'child', 'children', 'kid', 'toddler', 'Nouvelle Écosse', 'Nova Scotia', 'de la'))
    
    $entry1 = myList[mySeed2alt][0]
    $entry2 = myList[mySeed2alt][1]
    $entry3 = myList[mySeed2alt][2]
    $entry4 = myList[mySeed2alt][3]
    $entry5 = myList[mySeed2alt][4]
    $entry6 = myList[mySeed2alt][5]
    $entry7 = myList[mySeed2alt][6]
    $entry8 = myList[mySeed2alt][7]
    $entry9 = myList[mySeed2alt][8]

    b "La magie de la recherche booléenne vient lorsqu'on combine les opérateurs ensemble."
    b "Par exemple, une recherche sur les {=word}[entry1]{/=word} [entry9] {=word}[entry7]{/=word}..."
    b "pourrait demander de chercher pour {=word}[entry1]{/=word} {=bool}ou{/=bool} {=word}[entry2]{/=word} {=bool}ou{/=bool} {=word}[entry3]{/=word} {=bool}ou{/=bool} {=word}[entry4]{/=word} {=bool}ou{/=bool} {=word}[entry5]{/=word} {=bool}ou{/=bool} {=word}[entry6]{/=word}"
    b "{=bool}ET{/=bool} {=word}[entry7]{/=word} {=bool}ou{/=bool} {=word}[entry8]{/=word}."
    b "Vous trouverez peut-être utile d'utiliser un formulaire pour penser à vos opérateurs booléens."
    b "Par exemple, voici un formulaire remplit qui fonctionnerait pour notre sujet."
    call bil_bib_showform from _call_bil_bib_showform
    
    return
    
#To display a demo form in bib or and intro
label bil_bib_showform:
    
    #teens and New Brunswick
    if mySeed2alt == 0:
        
        if lang == "english":
            sv "A table appears on screen. The first column is about teens. The words 'Adolescence', 'teen', 'teenager', and 'youth' appear on different rows of the first column."
            sv "The second column is about the province. The words 'New Brunswick' and 'New Brunswickian' appear on different rows."
            sv "The table will remain on screen for 5 seconds unless you click to continue."
        else:
            sv "Un tableau apparaît à l'écran. La première colonne est à propos des adolescents. Les mots 'ado', 'adolescence', 'adolescent' et le mot anglais 'teen' sont sur différentes lignes de la première colonne."
            sv "La deuxième colonne est à propos de la province. Les mots 'Nouveau Brunswick' et en anglais 'New Brunswick' apparaîssent sur différentes lignes."
            sv "Le tableau va demeurer à l'écran 5 secondes à moins de cliquer pour continuer."
            
        show image "form"
        show teenage at formPos17
        show teen1 at formPos1
        show teen2 at formPos5
        show teen3 at formPos9
        show teen4 at formPos13
        
        show province at formPos18
        show provNB1 at formPos2
        show provNB2 at formPos6
        
        window hide
        $renpy.pause(14.0)
        window show
    #Kids and Nova Scotia
    else:
        
        if lang == "english":
            sv "A table appears on screen. The first column is about children. The words 'Child', 'children', 'kid', and 'toddler' appear on different rows of the first column."
            sv "The second column is about the province. The words 'Nova Scotia' and 'Nova Scotian' appear on different rows."
            sv "The table will remain on screen for 5 seconds unless you click to continue."
        else:
            sv "Un tableau apparaît à l'écran. La première colonne est à propos des enfants. Les mots 'enfance', 'enfant', et les mots anglais 'children' et 'kid' sont sur différentes lignes de la première colonne."
            sv "La deuxième colonne est à propos de la province. Les mots 'Nouvelle Écosse' et en anglais 'Nova Scotia' apparaîssent sur différentes lignes."
            sv "Le tableau va demeurer à l'écran 5 secondes à moins de cliquer pour continuer."
        
        show image "form"
        show children at formPos17
        show child1 at formPos1
        show child2 at formPos5
        show child3 at formPos9
        show child4 at formPos13
        
        show province at formPos18
        show provNS1 at formPos2
        show provNS2 at formPos6
        
        window hide
        $renpy.pause(14.0)
        window show
    
    return
    
label en_OrAndIntro:
    call cleanMadGab from _call_cleanMadGab_1
    call ms_party from _call_ms_party_1
    call sc_class from _call_sc_class_5
    b "I like to introduce the {=bool}OR{/=bool} boolean operator with the example of a boyfriend trying to find a treat for his partner in a bakery."
    call sc_bakery from _call_sc_bakery_1
    b "\"Bring me back something good,\" says his partner."
    show Librarian smiling at right
    b "\"Cake, {=bool}or{/=bool} a bear claw, {=bool}or{/=bool} some truffles, {=bool}or{/=bool} a lemon meringue pie, {=bool}or{/=bool} some muffins!\""
    sv "Menu"
    $shuffle_menu()
    menu:
        b "Which of the following choices would have satisfied the boyfriend's request for a cake, or a bear claw, or some truffles, or muffins, or a lemon meringue pie?"
        "Cake?":
            show Librarian intense
            b "Yes!"
            b "{size=-4}I baked my own birthday cake, it was delicious...{/size}"
        "A bear claw?":
            show Librarian intense
            b "Absolutely!"
            b "But I'll never understand why I can get bear claws at the bakery store but not moose hooves?"
        "Truffles?":
            show Librarian intense
            b "That's right!"
            b "{size=-4}You know, chocolate truffles make an excellent thank you gift appropriate for any librarian giving a presentation...{/size}"
        "Muffins?":
            show Librarian intense
            b "Yes, that's right!"
            b "Of course, all kinds of muffins exist, so his partner should have been a bit more specific so as not to be disappointed with a raisin bran muffin instead of getting a delicious chocolate chip muffin!"
    
    show Librarian neutral
    b "The boyfriend had LOTS of options that would have satisfied his partner."
    b "The {=bool}OR{/=bool} boolean operator simply tells us that \"any of these options would satisfy my request.\""
    
    show Librarian smiling
    b "Now, imagine a mother trying to select a cake for her daughter in that same bakery."
    b "\"I want a cake\", isn't a very complicated request."
    
    if kitten:
        b "But \"I want a cake, {=bool}and{/=bool} it has to be a chocolate cake {=bool}and{/=bool} I want sprinkles on my cake, 
           {=bool}and{/=bool} cherries {=bool}and{/=bool} a drawing of Iron Man fighting against a Ninja Turtle, 
           {=bool}and{/=bool} vanilla frosting {=bool}and{/=bool} tons of kittens...\""
    else:
        b "But \"I want a cake, {=bool}and{/=bool} it has to be a chocolate cake {=bool}and{/=bool} I want sprinkles on my cake, 
           {=bool}and{/=bool} cherries {=bool}and{/=bool} a drawing of Iron Man fighting against a Ninja Turtle, 
           {=bool}and{/=bool} vanilla frosting...\""

    b "That's going to be a bit harder to find."
    
    if kitten:
        sv "Menu"
        $shuffle_menu()
        menu:
            b "Which of the following options would have best satisfied the little girl's desire for a chocolate cake with vanilla frosting 
               and sprinkles, a drawing of Iron Man fighting against a Ninja Turtle, cherries, and lots of kittens?"    
            "A vanilla cake with chocolate frosting and a Ninja Turtle and some kitties fighting Iron Man?":
                b "\"I wanted chocolate cake\", cries the little girl."
            "A chocolate cake with sprinkles, vanilla frosting, and cherries on top?":
                b "\"Where's Iron Man? And the kittens?\" cries the little girl."
            "A chocolate cake with cherries on top, vanilla frosting, and Iron Man and some kittens beating up a Ninja Turtle?":
                b "\"You forgot the sprinkles\", cries the little girl."
            "A basket filled with kittens?":
                b "\"SO I DON'T GET CAKE AT ALL?\", cries the little girl."
            "This is impossible!":
                pass
    else:
        sv "Menu"
        $shuffle_menu()
        menu:
            b "Which of the following options would have best satisfied the little girl's desire for a chocolate cake with vanilla frosting 
               and sprinkles, a drawing of Iron Man fighting against a Ninja Turtle, and cherries?"    
            "A vanilla cake with chocolate frosting and a Ninja Turtle fighting Iron Man?":
                b "\"I wanted chocolate cake\", cries the little girl."
            "A chocolate cake with sprinkles, vanilla frosting, and cherries on top?":
                b "\"Where's Iron Man?\" cries the little girl."
            "A chocolate cake with cherries on top, vanilla frosting, and Iron Man beating up a Ninja Turtle?":
                b "\"You forgot the sprinkles\", cries the little girl."
            "This is impossible!":
                pass

    
    show Librarian intense at center
    with move
    b "The little girl had a lot of criterias for her perfect cake, so her mother was left with very few...or zero options that could satisfy her."
    b "The {=bool}AND{/=bool} boolean operator says: \"my request is satisfied only if ALL of these criterias are met.\""
    
    show Librarian smiling

    $myList = (('adolescent', 'teens', 'teenagers', 'youths', 'New Brunswick', 'New Brunswickian'),
        ('child', 'children', 'kid', 'toddler', 'Nova Scotia', 'Nova Scotian'))
    
    $entry1 = myList[mySeed2alt][0]
    $entry2 = myList[mySeed2alt][1]
    $entry3 = myList[mySeed2alt][2]
    $entry4 = myList[mySeed2alt][3]
    $entry5 = myList[mySeed2alt][4]
    $entry6 = myList[mySeed2alt][5]

    b "The magic behind boolean searches is unleashed when we combine boolean operators."
    b "For example, a search about {=word}[entry6]{/=word} [entry9]{=word}[entry2]{/=word}..."
    b "Could require us to search for {=word}[entry1]{/=word} {=bool}or{/=bool} {=word}[entry2]{/=word} {=bool}or{/=bool} {=word}[entry3]{/=word}"
    b "{=bool}AND{/=bool} {=word}[entry5]{/=word} {=bool}or{/=bool} {=word}[entry6]{/=word}."
    b "You might find it useful to use a form to help you think about how to use boolean operators to link together different concepts."
    b "Here's a search strategy form we could have used for our example!"
    call bil_bib_showform from _call_bil_bib_showform_1

    return
    
label fr_troncature:

    call ms_party from _call_ms_party_2
    call sc_class from _call_sc_class_6
    cli "Madame, chercher pour tous les synonymes possibles d'un mot quand on fait une recherche prend trop de temps."
    cli "{=word}Famille{/=word} {=bool}OR{/=bool} {=word}familial{/=word} {=bool}OR{/=bool} {=word}familles{/=word} {=bool}OR{/=bool} {=word}family{/=word}? Je ne peux pas passer deux heures par projet juste à préparer des expressions de recherche booléenne."
    show Librarian smiling
    b "Haha, deux heures c'est beaucoup trop, mais si vous prenez un peu de temps pour bien réfléchir
        à votre recherche, vous allez réduire le temps total que ça va vous prendre pour chercher."
    b "Vous n'aurez pas tellement de résultats inutiles à regarder et éliminer."
    b "Vous allez déjà avoir une idée d'où chercher, et des mots à utiliser pour la recherche."
    show Librarian intense
    b "Et en plus, je peux vous montrer un autre opérateur booléen qui va vous aider à sauver du temps!"
    cli "J'espère que ton explication n'est pas trop longue..."

    b "Dans la plupart des bases de données, vous pouvez utiliser le symbole {=bool}*{/=bool} pour trouver des variations
        dans la terminaison d'un mot."
    sv "La classe ne sait pas comment réagir. Cliquer deux fois pour continuer."
    cl "???"
    show Librarian neutral
    b "Euh, je peux voir que vous n'avez pas trop suivi."
    b "Voyons voir... si je vous demandais de limiter votre recherche au {=word}{b}Canada{/b}{/=word}?"
    b "Vous pourriez être intéressés par les résultats contenant les mots..."
    b "{=word}Canad{b}a{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ien{/b}{/=word} {=bool}OR{/=bool} 
       {=word}Canad{b}ienne{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}iens{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}iennes{/b}{/=word} 
       {=bool}OR{/=bool} {=word}Canad{b}ian{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ians{/b}{/=word}"
    cli "C'est LONG. C'est BEAUCOUP TROP LONG."
    show Librarian intense
    b "Exactement! Mais ce sont des variations d'un même mot. La souche reste identique, mais la terminaison du mot
        change. On peut utiliser l'opérateur booléen {=bool}*{/=bool} pour ce genre de situations."
    b "{=word}{b}Canad*{/b}{/=word}"
    b "{=word}{b}Canad*{/b}{/=word} est l'équivalent d'une recherche pour {=word}Canad{b}a{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ien{/b}{/=word} 
       {=bool}OR{/=bool} {=word}Canad{b}ienne{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}iens{/b}{/=word} {=bool}OR{/=bool} 
       {=word}Canad{b}iennes{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ian{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ians{/b}{/=word}"
    if kitten:
        b  "{=word}{b}Chat*{/b}{/=word} est l'équivalent de {=word}Chat{/=word} {=bool}OR{/=bool} {=word}Chat{b}te{/b}{/=word} {=bool}OR{/=bool} {=word}Chat{b}on{/b}{/=word}"
    cl "Wow!"
    show Librarian smiling
    b "Lorsqu'on fait une recherche et qu'on a repéré les mots clés importants à utiliser pour sa recherche, on trouve les
        synonymes de ces mots clés. Ensuite, on regarde chacun des termes composant notre recherche."
    sv "Mode voix bibliothécaire. Si ces termes ont différentes terminaisons, on trouve la souche commune du mot et on place astérix à la fin de la souche."
    b "Si ces termes ont différentes terminaisons, on trouve la souche commune du mot et on place {=bool}*{/=bool}
        à la fin de la souche."
    sv "Mode voix bibliothécaire. Habituellement, on a juste besoin d'effacer quelques lettres puis de placer notre astérix."
    b "Habituellement, on a juste besoin d'effacer quelques lettres puis de placer notre {=bool}*{/=bool}."
    show Librarian neutral
    b "Est-ce que vous voulez des exemples?"
    
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Voulez-vous des exemples d'utilisation de l'opérateur booléen de troncature?"
        "Oui!":
            show Librarian intense
            cl "Oui!"
            b "On pourrait chercher pour {=word}{b}ado*{/b}{/=word} plutôt que de chercher pour {=word}{b}ado{/b}{/=word} {=bool}OR{/=bool} {=word}ado{b}s{/b}{/=word} {=bool}OR{/=bool} {=word}ado{b}lescent{/b}{/=word} {=bool}OR{/=bool} {=word}ado{b}lescente{/b}{/=word}
                {=bool}OR{/=bool} {=word}ado{b}lescents{/b}{/=word} {=bool}OR{/=bool} {=word}ado{b}lescentes{/b}{/=word} {=bool}OR{/=bool} {=word}ado{b}lescence{/b}{/=word}."
            b "{=word}{b}Diabèt*{/b}{/=word} pour {=word}diabèt{b}e{/b}{/=word} {=bool}OR{/=bool} {=word}diabèt{b}ique{/b}{/=word}."
            b "{=word}{b}Immigr*{/b}{/=word} pour {=word}immigr{b}ant{/b}{/=word} {=bool}OR{/=bool} {=word}immigr{b}ante{/b}{/=word} {=bool}OR{/=bool} {=word}immigr{b}ants{/b}{/=word}
                {=bool}OR{/=bool} {=word}immigr{b}er{/b}{/=word} {=bool}OR{/=bool} {=word}immigr{b}ation{/b}{/=word}."
        "Non!":
            show Librarian neutral
            cl "Non!"
            b "Vous comprenez vite!"
            b "Juste une dernière petite explication."
    
    show Librarian smiling
    b "Ce serait pratiquement {=word}{i}criminel{/i}{/=word} de ma part de ne pas mentionner que la plupart des bases de données
        s'occupent automatiquement du pluriel des mots."
    b "Si vous cherchez pour {=word}crim{b}e{/b}{/=word}, vous allez donc trouver aussi {=word}crim{b}es{/b}{/=word}."
    b "Mais pas nécessairement {=word}crim{b}inel{/b}{/=word} ou {=word}crim{b}inalité{/b}{/=word}."

    return
    
label en_troncature:

    call ms_party from _call_ms_party_3
    call sc_class from _call_sc_class_7
    cli "Hey! It takes too long to search databases for all possible synonyms of a word."
    cli "{=word}Teen{/=word} {=bool}OR{/=bool} {=word}teenager{/=word} {=bool}OR{/=bool} {=word}teenaged{/=word} {=bool}OR{/=bool} {=word}teenagers{/=word}? I don't want to spend two hours just preparing keywords for every assignment I have."
    show Librarian smiling
    b "Haha, two hours is way too much, but if you take a bit of time to plan your search, you'll reduce the total time spent searching."
    b "You won't have so many useless results to go through in your list of search results."
    b "You'll have a good idea of where to search, and what keywords to use to search effectively."
    show Librarian intense
    b "And I'm going to show you another boolean operator that will help you save lots of time!"
    cli "I hope your explanation won't take too long..."

    b "In most databases, you can use the asterix symbol {=bool}*{/=bool} to find variations in word endings."
    sv "The class doesn't know how to react. Click twice to continue."
    cl "???"
    show Librarian neutral
    b "Um, I can see that you guys aren't following me too well."
    b "Let's see... if I wanted you to limit your search to {=word}{b}Canadian{/b}{/=word} material?"
    b "You might be interested in results containing the words..."
    b "{=word}Canad{b}a{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ien{/b}{/=word} {=bool}OR{/=bool} 
       {=word}Canad{b}ienne{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}iens{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}iennes{/b}{/=word} 
       {=bool}OR{/=bool} {=word}Canad{b}ian{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ians{/b}{/=word}"
    cli "That's SO MUCH. That would take WAY TOO MUCH TIME to type."
    show Librarian intense
    b "Exactly! But these are all variations on a same word. The root stays the same, but the ending of the word changes. 
       So we can use the {=bool}*{/=bool} boolean operator as a shortcut."
    b "{=word}{b}Canad*{/b}{/=word}"
    b "{=word}{b}Canad*{/b}{/=word} is the equivalent of searching for {=word}Canad{b}a{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ien{/b}{/=word} 
       {=bool}OR{/=bool} {=word}Canad{b}ienne{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}iens{/b}{/=word} {=bool}OR{/=bool} 
       {=word}Canad{b}iennes{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ian{/b}{/=word} {=bool}OR{/=bool} {=word}Canad{b}ians{/b}{/=word}"
    if kitten:
        b  "{=word}{b}Kitt*{/b}{/=word} is the equivalent of searching for {=word}Kitt{b}y{/b}{/=word} {=bool}OR{/=bool} {=word}Kitt{b}en{/b}{/=word} {=bool}OR{/=bool} {=word}Kitt{b}ens{/b}{/=word}"
    cl "Wow!"
    show Librarian smiling
    b "When planning a search, after thinking about all of the important keywords to use, we think about the synonyms to those keywords. 
       Next, we look at every search term individually."
    b "If the search terms have different endings, we find the common root to the words and put an asterix after the root."
    sv "Self-voiced librarian. Usually, we just need to truncate a few letters at the end of the word before placing our asterix."
    b "Usually, we just need to truncate a few letters at the end of the word before placing our {=bool}*{/=bool}."
    show Librarian neutral
    b "Would you like some examples?"
    
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Do you want some more examples of the truncation boolean operator?"
        "Sure!":
            show Librarian intense
            cl "More examples, please!"
            b "We could search for {=word}psych*{/=word} instead of searching for {=word}psych{/=word} {=bool}OR{/=bool} {=word}psych{b}ologist{/b}{/=word} {=bool}OR{/=bool}
               {=word}psych{b}ology{/b}{/=word} {=bool}OR{/=bool} {=word}psych{b}iatry{/b}{/=word}
                {=bool}OR{/=bool} {=word}psych{b}iatrist{/b}{/=word} {=bool}OR{/=bool} {=word}psych{b}ological{/b}{/=word}."
            b "{=word}Diabet*{/=word} for {=word}diabet{b}es{/b}{/=word} {=bool}OR{/=bool} {=word}diabet{b}ic{/b}{/=word}."
            b "{=word}Immigr*{/=word} for {=word}immigr{b}ant{/b}{/=word} {=bool}OR{/=bool} {=word}immigr{b}ants{/b}{/=word}
                {=bool}OR{/=bool} {=word}immigr{b}ate{/b}{/=word} {=bool}OR{/=bool} {=word}immigr{b}ation{/b}{/=word}."
        "Nope!":
            show Librarian neutral
            cl "No thanks!"
            b "You're quick learners!"
            b "Just one last quick explanation."
    
    show Librarian smiling
    b "It would be practically a {=word}{i}crime{/i}{/=word} on my part to neglect from mentioning that most databases 
       automatically handle the plural form of words."
    b "If you search for {=word}crim{b}e{/b}{/=word}, you will also find results containing the word {=word}crim{b}es{/b}{/=word}."
    b "But not necessarily {=word}crim{b}inal{/b}{/=word} or {=word}crim{b}inality{/b}{/=word}."

    return
    
label fr_langue:
    call ms_party from _call_ms_party_4
    call sc_class from _call_sc_class_8
    cli "{=word}adolescent{/=word} {=bool}OR{/=bool} {=word}teenager{/=word} {=bool}OR{/=bool} {=word}adolescence{/=word} {=bool}OR{/=bool} {=word}teen{/=word} {=bool}OR{/=bool} {=word}ado{/=word}?"
    cli "MADAME! Je voulais des trucs pour trouver des résultats en FRANÇAIS."
    show Librarian neutral
    b "Oui, c'est ce qu'on fait!"
    cli "MADAME! C'est plein de mots anglais dans ton expression de recherche!"
    show Librarian intense
    b "C'est mieux de créer des expressions de recherche booléenne bilingue, parce que-"
    cli "MADAME!"
    show Librarian neutral
    b "...Oui?"
    cli "Des COURTES explications."
    show Librarian intense
    b "Les bases de données anglophones vont prendre un article écrit en francais et vont traduire le titre en anglais."
    b "Ils utilisent l'abstrait/résumé anglais ou le traduisent. Ils ajoutent des mots clés en anglais."
    b "Enfin, ils vont identifier la langue de l'article en écrivant 'language French'."
    show Librarian smiling
    b "Parfois la seule façon de trouver un article en français {b}est de chercher en anglais!{/b}"
    cl "QUOI? Wow!"
    cli "Et si je ne connais pas les mots en anglais à utiliser, MADAME?"
    show Librarian intense
    b "Tu peux consulter un thésaurus, ajouter des mots après une première recherche exploratoire, utiliser Google translate,
     faire une recherche dans Termium pour avoir la traduction d'un terme spécifique à ta discipline..."
    b "Et tu peux utiliser plusieurs de ces trucs pour trouver d'autres mots pour ta recherche en français."
    show Librarian smiling
    b "Viens me consulter si tu as besoin d'aide."
    b "C'est tellement important de choisir les bons mots pour sa recherche..."
    return
    
label fr_quotation:
    call ms_party from _call_ms_party_5
    call sc_class from _call_sc_class_9
    b "Un exemple d'une belle recherche booléenne pour le {=word}diabète{/=word} chez les {=word}personnes âgées{/=word} pourrait être..."
    sv "Mode voix bibliothécaire. Ouvre parenthèse guillemets personnes âgées guillements OR vieill* OR gerontol* OR  guillemets older adults guillemets OR elder* ferme parenthèse. AND diabet*"
    b "(\"{=word}personnes âgées{/=word}\" {=bool}OR{/=bool} {=word}vieill*{/=word} {=bool}OR{/=bool} {=word}gerontol*{/=word} {=bool}OR{/=bool} \"{=word}older adults{/=word}\" {=bool}OR{/=bool} {=word}elder*{/=word}) {=bool}AND{/=bool} {=word}diabet*{/=word}"
    cl "Madame? Pourquoi les guillemets?"
    cli "C'est presque l'heure de la pause, alors on ne prend pas trop de temps pour l'explication!"
    sv "Il y avait des guillemets autour de personnes âgées."
    show Librarian smiling
    b "Ah oui! Je ne peux pas croire que j'ai presque oublié de vous expliquer les guillemets!"
    b "C'est très utile pour encadrer {b}des termes composés de plus qu'un mot{/b}."
    b "Si vous cherchez un terme composé de plus qu'un mot, entourez les mots de guillemets."
    sv "La classe ne sait pas comment réagir. Cliquer deux fois pour continuer."
    cl "???"
    show Librarian intense
    b "C'est surtout utile lorsqu'on créé une expression de recherche booléene."
    b "Si vous cherchez par exemple pour '{=word}personnes âgées{/=word}' mais que vous ne mettez pas de guillemets..."
    b "Vous pourriez trouver un article qui a la phrase suivante dans son introduction:"
    b "{i}{b}{=word}Personne{/=word}{/b} ne comprend réellement comment bien s'occuper des enfants {b}{=word}âgés{/=word}{/b} de 2 à 3 ans{/i}."
    b "La phrase comprend les mots '{=word}personnes{/=word}' et '{=word}âgées{/=word}' que l'on cherchait, mais il ne s'agit pas du tout de
        {b}'{=word}personnes âgées{/=word}'{/b}."
    show Librarian smiling
    b "L'utilisation des guillemets force les bases de données à trouver tous les mots que l'on cherche exactement
        dans le même ordre dans lequel ces mots se trouvent à l'intérieur de nos guillemets."
    b "La raison principale pour laquelle vous pourriez vouloir utiliser les guillemets en dehors de
        vos recherches académiques, c'est pour chercher un titre d'un livre ou des paroles dans Google."
    b "Google comprend très bien l'utilisation des guillemets!"
    
    show Librarian intense
    sv "Dans le menu qui suit, la première option est guillemet mal de mer guillemet. La deuxième option est guillemet mal guillemet de guillemet mer guillemet."
    sv "Menu"
    $unshuffle_menu()
    menu:
        "Si je ne veux pas être malade en bateau, comment je devrais composer ma recherche?"
        "\"Mal de mer\"":
            show Librarian smiling
            b "Oui, c'est un bon exemple de l'utilisation de guillemets!"
            b "Je n'aime pas les bateaux!"
        "\"Mal\" de \"mer\"":
            show Librarian neutral
            b "Non, ça ne fait pas de sens! Je vais être malade!"
            b "Vous devez mettre l'expression de recherche au complet dans les guillemets."
            sv "Mode voix bibliothécaire. Vous devriez chercher pour guillemet mal de mer guillement."
            b "Vous devriez chercher pour \"Mal de mer\"."
    return
    
label en_quotation:
    call ms_party from _call_ms_party_6
    call sc_class from _call_sc_class_10
    b "An example of a good boolean search strategy for {=word}aboriginal governance{/=word} could be..."
    sv "Self-voiced librarian. Open parentheses quotation marks first nations quotation marks OR aboriginal OR indigen* close parentheses. AND govern*"
    b "(\"{=word}first nations{/=word}\" {=bool}OR{/=bool} {=word}aboriginal{/=word} {=bool}OR{/=bool} {=word}indigen*{/=word}) {=bool}AND{/=bool} {=word}govern*{/=word}"
    b "Can you think of more synonyms to use to complete our search expression?"
    cl "Miss? Why the quotation marks?"
    cli "Try to make it quick, it's almost time for our break!"
    show Librarian smiling
    b "Of course! I can't believe I almost forgot to discuss quotation marks!"
    b "It's really useful to use quotation marks around {b}terms composed of more than one word{/b}."
    b "If you're searching for an expression composed of more than one word, surround the words with quotation marks."
    sv "The class doesn't know how to react. Click twice to continue."
    cl "???"
    show Librarian intense
    b "This is mostly of use when creating boolean search expressions."
    b "For example, if you're trying to find recipes that use '{=word}peanut butter{/=word}' as a component, but you don't put in the quotation marks..."
    b "You could find a recipe that has {b}{=word}peanuts{/=word}{/b} as an ingredient, and then a few more ingredients, and then {b}{=word}butter{/=word}{/b}."
    b "Both the words {b}{=word}peanuts{/=word}{/b} and {b}{=word}butter{/=word}{/b} are there, but not the {b}{=word}peanut butter{/=word}{/b} we actually wanted."
    show Librarian smiling
    b "Using quotes forces databases to find the exact expression. All of the  words that are encapsulated by the 
       quotation marks boolean operator, in the same exact order, with no breaks in the word sequence."
    b "One reason to use quotation marks outside of academic research is to search using the 
       title of a book or song lyrics in Google."
    b "Google understands quotation marks very well!"
    
    show Librarian intense
    sv "In the following menu, the first option is quotation mark car crash quotation mark. The second option is quotation mark car quotation mark space quotation mark crash quotation mark. Reverse the order if pressing up to reach the menu options."
    sv "Menu"
    $unshuffle_menu()
    menu:
        "What words should I put in a database if I'm about to get involved in a {=word}car crash{/=word}?"
        "\"Car crash\"":
            show Librarian smiling
            b "Yes, that's an excellent use of quotation marks!"
            b "Drive safe, everyone!"
        "\"Car\" \"crash\"":
            show Librarian neutral
            b "No, that doesn't make sense! You're steering out of control!"
            b "The entire expression should be encased in quotation marks."
            sv "Self-voiced librarian. You need to search for the words quotation mark car crash quotation mark."
            b "You need to search for {=word}\"Car crash\"{/=word}."
    return
