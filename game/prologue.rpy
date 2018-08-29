#First part of the story! :) Introduce to scenario and get to image map of body parts
label fr_prologue:
    call sc_black from _call_sc_black
    
    if persistent.ending_achieved:
        "Malgré la sensation de déjà vu, j'ai couché sur le sofa de mon amie. Ça m'a pris des heures avant d'arriver à m'endormir."
    else:
        "Les nouvelles ont annoncé que les zombies étaient rendus dans notre ville pendant que j'étudiais chez mon amie Évangeline."
        "J'ai couché sur son sofa. Ça m'a pris des heures avant d'arriver à m'endormir."
        
    "Je ne savais pas encore que les {=bool}OPÉRATEURS BOOLÉENS{/=bool}, ces formules magiques qui forcent les ordinateurs 
     à faire des recherches efficaces..."
    "...allaient être une de mes armes les plus efficaces pour lutter contre les zombies."
    
    titleCard "ZomBool"
    
    call sc_evangeline from _call_sc_evangeline
    call ms_lithium from _call_ms_lithium
    
    e "Gabriel! Réveille!"
    show Eva mwahaha
    "J'ai à peine le temps d'apercevoir Évangeline qu'elle descend dans son sous-sol. Sa voix sonne de plus en plus lointaine."
    sv "Elle portait un sarrau de laboratoire."
    
    show Eva at my_out
    
    if kitten:
        "Je n'ai pas besoin d'Évangeline pour faire passer le temps. Son chat est installé tranquille sur un coussin du sofa."
        sv "Menu"
        $shuffle_menu()
        menu:
            "Flatter le beau petit minou d'Évangeline?"
            "Oui!":
                "Le minou ronronne très fort. Quel beau petit minou!"
            "Oh, je ne veux pas le déranger!":
                "Le yeux du minou clignotent une fois, deux fois, puis il s'endort. TELLEMENT MIGNON!"
        "Tout d'un coup, j'entends Évangeline m'appeler. Ça ne semble pas troubler le minou."
    
    e "J'ai besoin que tu me lances une main ET la main doit avoir une 
       bague pouvant conduire l'électricité."
    "Je peux voir des morceaux de corps empilés derrière mon sofa. C'est dégoûtant!"
    
    return
    
label en_prologue:
    call sc_black from _call_sc_black_1
    
    if persistent.ending_achieved:
        "I slept on my friend's sofa. It took me hours before I managed to fall asleep."
    else:
        "News reports announced that zombies had reached our city while I was studying at my friend's house."
        "I slept on her sofa. It took me hours before I managed to fall asleep."
    
    "I didn't yet know that {=bool}BOOLEAN OPERATORS{/=bool}, these magical formulas that force computers to search databases more effectively..."
    "...would become one of our best weapons in the fight against the zombies."
    
    titleCard "ZomBool"
    
    call sc_evangeline from _call_sc_evangeline_1
    call ms_lithium from _call_ms_lithium_1
    
    e "Gabriel! Wake up!"
    show Eva mwahaha
    "My eyes barely open before my friend Évangeline goes down into her basement, her voice progressively fading away."
    sv "She was wearing her lab coat."
    show Eva at my_out
    
    if kitten:
        "I don't need Évangeline to entertain me. Her cat is perched on the arm of the couch."
        sv "Menu"
        $shuffle_menu()
        menu:
            "Pet Évangeline's cute little kitty?"
            "Yes!":
                "Her cat purrs loudly. What a nice little kitty!"
            "Oh no, I wouldn't dream of disturbing her cat!":
                "The cat's eyes blink once, twice, and then it promptly falls asleep. IT'S SO CUTE!"
        "I suddenly hear Évangeline calling for me. It doesn't seem to disturb her kitty."
    
    e "Throw me a hand AND that hand needs to have a ring that can conduct electricity."
    "Gross! I can see body parts behind the sofa."
    
    return

#Image Map sequence - pick a body part
label fr_corps:
    
    sv "Utiliser la flêche vers le haut ou la flêche vers le bas pour examiner les différents morceaux de corps."
    
    window hide None
    call screen body_parts
    window show None
    
    #Wrong body part
    if _return == "fail":
        $flagCount +=1
        
        call victoryLost from _call_victoryLost
        queue sound "Split_Splat.mp3"
        
        if flagCount == 1:
            e "Ahhhh! Ne me lance pas n'importe quoi qui te tombe sous la main! Il me faut une main avec une bague."
        if flagCount == 2:
            e "Non! Non! Non! Une main avec une bague! UNE MAIN AVEC UNE BAGUE!"
        if flagCount == 3:
            e "Je n'ai pas besoin de cette...chose."
        if flagCount >= 4:
            e "C'est très bien. Lance moi tous les morceaux de corps. Pourquoi pas. Continue comme ça!"
        
        jump fr_corps
    
    #Right body part
    if _return == "win":
        queue sound "Split_Splat.mp3"
        call victoryWon from _call_victoryWon
        
    #If we picked the wrong body part 
    if flagCount == 1:
        e "Bon, tu m'as toute éclaboussée avec le premier truc que tu m'as lancé, mais ce n'est pas grave, tu as réussi à trouver ce que je cherchais!"
        "Je dois avouer que ça ne me dérange pas beaucoup de ne pas être un expert dans le lancé DE MORCEAUX DE CORPS!!!"
    #If we picked the wrong body part
    elif flagCount > 1:
        e "Bon, tu m'as toute éclaboussée avec les trucs que tu m'as lancés, mais ce n'est pas grave, tu as réussi à trouver ce que je cherchais!"
        "Je dois avouer que ça ne me dérange pas beaucoup de ne pas être un expert dans le lancé DE MORCEAUX DE CORPS!!!"
    #If we picked the right body part on the first try
    else:
        e "Wow, merci, c'était rapide ça!"
        "Peut-être que je suis prêt pour une carrière en tant qu'assistant boucher?"

    g "Tu sais Évangeline, tes instructions n'étaient pas vraiment assez précises. Je cherchais {i}juste{/i} une main, et 
       finalement j'ai dû te lancer un bras au complet!"
    e "Sérieusement? Wow, tu ne devais pas porter attention lorsque la bibliothécaire nous a expliqué comment faire nos recherches la semaine dernière."
    g "La... bibliothécaire? Je suis en train de te lancer des morceaux de corps en plein milieu d'une attaque de zombies et tu veux parler de la bibliothécaire?"
    e "Pourquoi pas? C'est un meilleur sujet de conversation que ce je suis en train de faire."
    e "Tu te souviens? La bibliothécaire est venue dans notre cours expliquer des stratégies de recherche pour notre projet."
    "J'ignore les sons bizarres provenant de la cave pour penser de nouveau à la visite de la bibliothécaire."
    
    return
    
#Image Map sequence - pick a body part
label en_corps:
    
    sv "Use the up or down arrow keys on the keyboard to sort through the different body parts."    
    window hide None
    call screen body_parts
    window show None
    
    
    #Wrong body part
    if _return == "fail":
        $flagCount +=1
        
        call victoryLost from _call_victoryLost_1
        queue sound "Split_Splat.mp3"
        
        if flagCount == 1:
            e "Ahhhh! Don't just throw me the first thing you find! I need a hand with a ring!"
        if flagCount == 2:
            e "No! Wrong! A hand with a ring! A HAND WITH A RING!"
        if flagCount == 3:
            e "I don't need this...thing."
        if flagCount >= 4:
            e "That's great. Just throw me ALL the body parts you find. Why not? Keep going!"
        
        jump en_corps
    
    #Right body part
    if _return == "win":
        queue sound "Split_Splat.mp3"
        call victoryWon from _call_victoryWon_1
        
    #If we picked the wrong body part 
    if flagCount == 1:
        e "You found what I needed, so I guess it doesn't matter that you spattered me with that first thing you threw at me!"
        "I'm not especially bothered not to be an expert at THROWING BODY PARTS!!!"
    #If we picked the wrong body part
    elif flagCount > 1:
        e "You found what I needed, so I guess it doesn't matter that you spattered me with all the other things you threw at me!"
        "I'm not especially bothered not to be an expert at THROWING BODY PARTS!!!"
    #If we picked the right body part on the first try
    else:
        e "Wow, thanks, that was fast!"
        "I might be ready for a career as an assistant butcher?"

    g "Your instructions were too vague. I was searching for a hand, but I ended up having to throw down an entire arm!"
    e "Seriously? Wow, you must not have been paying attention when the librarian explained how to do better searches last week."
    g "The...librarian? I'm throwing body parts at you in the middle of a zombie attack and you want to talk about the librarian?"
    e "Why not? Better than talking about what I'm doing right now."
    e "Didn't the librarian also go to your class to talk about search strategies?"
    "I ignore the strange noises coming from the basement to think about the librarian's visit."
    
    return
    
label fr_phone:
    call sc_evangeline_alone from _call_sc_evangeline_alone
    show Eva at my_out_init
    g "Alors lorsque je t'ai lancé une main encore attachée après un bras..."
    g "...c'est comme si je te lançais un livre au complet pour que tu puisse lire le chapitre qui va le mieux t'aider?"
    e "Exactement!"
    g "Wow...un lien TERRIBLEMENT faible."
    
    show Eva determ at center with move
    e "Ça t'a au moins distrait un peu."
    sv "Évangeline apparaît brusquement devant moi."
    g "GAH!"
    e "Oops, excuse moi, je ne voulais pas te faire peur."
    e "La réception est meilleure ici que dans le sous-sol."
    g "Je suis désolé de t'apprendre ça...On ne peut pas appeler ou texter, le réseau mobile a flanché très vite après le début de l'évènement. "
    g "Je n'arrive même pas à me connecter à l'internet! On sait que c'est grave lorsqu'on n'arrive pas à accéder à l'internet!"
    e "Ma mère a une ligne téléphonique dans son bureau. Fais-moi une faveur? Laisse moi savoir si tu arrives à rejoindre un médecin?"
    g "Tu est blessée?"
    
    show Eva pensive
    e "Non, non. Je suis en train de combiner deux... morceaux ensemble et j'aimerais l'opinion d'un expert."
    e "On n'a pas énormément de cours d'anatomie lorsqu'on se spécialise en chimie!"
    
    show Eva at my_out
    e "Je retourne travailler en bas merci en avance!"
    sv "Évangeline descend au sous-sol."
    
    call sc_office from _call_sc_office
    "Je suis allé voir dans le bureau de sa mère."
    if kitten:
        "Son minou m'a suivit, et s'est installé à mes pieds."
    "Ne pouvant pas faire une petite recherche rapide sur internet, j'ai dû trouver un bottin téléphonique — un livre qui contient pleins de numéros de téléphone."
    "Il était très poussiéreux."
    g "Voyons voir...{=word}médecin{/=word}...{=word}médecin{/=word}..."
    g "Évangeline, il n'y a pas de {=word}médecins{/=word} dans le bottin téléphonique?"
    e "Franchement Gabriel! N'oublies pas que la bibliothécaire nous a enseigné une technique très utile pour ce genre de situation!"
    
    stop music fadeout 0.5
    call sc_class from _call_sc_class
    play music "Enter the party.mp3" fadeout 0.5
    b "Lorsqu'on prépare une recherche, c'est très important de --"
    
    call ms_lithium_fast from _call_ms_lithium_fast
    sv "J'interrompt mes propres souvenirs. De retour dans le bureau."
    scene bg creepyOffice with Fade(0.1, 0.0, 0.5, color="#fff")
    g "Ah non! Je n'ai pas besoin de me souvenir de la visite de la bibliothécaire pour savoir trouver un numéro dans le bottin!"
    g "Je n'ai qu'à trouver une alternative au mot {=word}médecin{/=word}."
    e "Des synonymes! Comme nous \a expliqué la bibliothécaire!"
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "Tourner le bottin à la bonne page pour..."
        "Docteur":
            "En cherchant {=word}docteur{/=word} plutôt que {=word}médecin{/=word}, j'ai trouvé plusieurs numéros prometteurs."
        "Hôpital":
            "Je ne veux pas appeler les urgences, mais j'ai trouvé quelques numéros prometteurs d'{=word}hôpitaux{/=word} à essayer."
        "Clinique médicale":
            "Je ne veux pas appeler les urgences, mais j'ai trouvé quelques numéros prometteurs de {=word}cliniques médicales{/=word} à essayer."
        "Santé":
            "Un autre mot aurait peut-être mieux fonctionné, mais j'ai réussi à trouver quelques numéros intéressants à essayer."
    
    play sound "Busy_Signal.mp3"
    "J'ai essayé tous les numéros trouvés. Ça sonne occupé, ou bien personne ne répond, ou la ligne est déconnectée."
    g "Désolé Évangeline, je n'arrive pas à rejoindre personne."
    e "Ce n'est pas très rassurant. Mais c'est correct, je vais faire de mon mieux par moi-même!"
    
    return
    
label en_phone:
    call sc_evangeline_alone from _call_sc_evangeline_alone_1
    show Eva at my_out_init
    g "So when I threw you a hand still attached to its arm...that was as if I was throwing you an entire book because you needed a chapter in the book?"
    e "Exactly!"
    g "Wow...that's really stretching the metaphor."
    
    show Eva determ at center with move
    e "At least, it kept you distracted."
    sv "Évangeline suddenly pops back in the room."
    g "GAH!"
    e "Oops, sorry, didn't mean to startle you."
    e "We get better reception here than in the basement."
    g "I'm sorry to have to be the one to tell you this... but we can't text or call anyone, mobile and data went down soon after the arrival of our undead guests."
    g "Even the internet is down! The internet! You know things are bad when we lose internet access!"
    e "My mom has a landline in her office. Could you try to see if you could get a doctor on the phone for me?"
    g "Are you hurt?"
    
    show Eva pensive
    e "No, not at all. I'm trying to combine two different...pieces together and I would love the opinion of an expert."
    e "Specializing in chemistry means that I haven't been taking many anatomy classes."
    
    show Eva at my_out
    e "I'll get back to work downstairs thanks you're a big help!"
    sv "She goes down the steps."
    
    call sc_office from _call_sc_office_1
    "I go to her mom's office to find the landline."
    if kitten:
        "Her kitty follows me and curls up near my feet."
    "With the internet being down, I look around for an alternative. I find a phone book — a book that contains tons of phone numbers from back when people couldn't put their contacts in their phones."
    "It's a bit dusty."
    g "Let's see...{=word}doctor's office{/=word}...{=word}doctor's office{/=word}..."
    g "Évangeline, I can't find '{=word}doctor's office{/=word}' in the phone book?"
    e "Really Gabriel! Don't forget that the librarian taught us a very useful technique to deal with exactly this kind of situation!"
    
    stop music fadeout 0.5
    call sc_class from _call_sc_class_1
    play music "Enter the party.mp3" fadeout 0.5
    b "Before starting your search, it's very important to --"
    
    call ms_lithium_fast from _call_ms_lithium_fast_1
    sv "I interrupt the flashback. Back in the office."
    scene bg creepyOffice with Fade(0.1, 0.0, 0.5, color="#fff")
    g "No! I don't need to remember the librarian's visit just to find a number in the phone book."
    g "I just need to find an alternative to the words {=word}doctor's office{/=word}."
    e "A synonym! Like the librarian explained!"
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "Find the right page in the phone book for..."
        "Medical practitioner":
            "I don't know why there isn't anything under {=word}doctor{/=word} or {=word}doctor's office{/=word} in this phone book, but I do find the phone numbers of a few doctors by searching for {=word}medical practitioners{/=word} instead."
        "Hospital":
            "I don't want to tie up any emergency lines, but I do find a few phone numbers for some local {=word}hospitals{/=word}."
        "Medical clinic":
            "Yes! There's no entry for {=word}doctor's offices{/=word}, but this phone book has lots of promising phone numbers under {=word}medical clinics{/=word}."
        "Health":
            "A different search term might have worked better, but I still manage to find a few promising phone numbers to call."
    
    play sound "Busy_Signal.mp3"
    "I try all the numbers. Every single time, no one picks up, or the line is busy, or the line is disconnected."
    g "Sorry Évangeline, I can't seem to reach anyone."
    e "That's a bad sign. But it's okay, I'll do my best to figure things out by myself!"
    
    return
    
label fr_visit_transition:
    call sc_evangeline_alone from _call_sc_evangeline_alone_2
    show Eva pensive at my_out_init
    show Creature neutral at my_out_init_buffer
    e "Bon, je pense que je suis prête à essayer!"
    show Eva pensive at center
    show Creature neutral at right
    with move
    "Elle monte me voir...accompagnée d'un truc épouvantable!"
    sv "Une espèce de créature formée par des morceaux de corps cousus ensemble."
    e "Prévoit-on un orage aujourd'hui?"
    show Eva determ
    e "J'aurais besoin d'un courant électrique puissant pour essayer d'animer...ma création."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    c "..."
    sv "Un autre moment de silence. Cliquez deux fois pour continuer."
    g "..."
    show Eva determ
    e "Pour combattre des zombies, quoi de mieux qu'un monstre fabriqué à partir des morceaux de leurs victimes?"
    g "Difficile de vérifier sans internet, mais je pense qu'on prévoyait une belle journée ensoleillée pour aujourd'hui."
    e "Quel dommage!"
    show Eva mwahaha
    e "Mais ce n'est pas grave, j'ai un autre plan."
    e "On va aller emprunter le réanimateur cardiaque d'un ami." 
    g "Il habite loin? Je n'aime pas beaucoup l'idée de me promener en plein milieu d'une attaque de zombies!"
    show Eva pensive
    e "C'est vrai que ce n'est pas très sécuritaire, alors moi je vais rester ici pour mieux protéger ma création."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    
    call sc_black from _call_sc_black_2
    stop music fadeout 1
    "Quelques zombies se promenaient dans la rue, mais j'ai réussi à embarquer dans ma voiture sans attirer leur attention."
    call ms_end from _call_ms_end
    
    return
    
label en_visit_transition:
    call sc_evangeline_alone from _call_sc_evangeline_alone_3
    show Eva pensive at my_out_init
    show Creature neutral at my_out_init_buffer
    e "Well, I think I'm just about ready to try this out!"
    show Eva pensive at center
    show Creature neutral at right
    with move
    "She comes upstairs...dragging some monstrous-looking thing!"
    sv "It's a bunch of body parts sewn together into some sort of creature."
    e "Are we expecting any thunderstorms today?"
    show Eva determ
    e "I need a strong electrical current to try to animate my...creation."
    sv "A silent beat. Click twice to continue."
    c "..."
    sv "Another silent beat. Click twice to continue."
    g "..."
    show Eva determ
    e "For fighting zombies, what could work better than a monster created from the body parts of their victims?"
    g "With no internet access, I'm not 100\% sure, but I seem to remember that they were predicting a beautiful sunny day for us."
    e "That's too bad."
    show Eva mwahaha
    e "But thankfully, I have a backup plan."
    e "I have a friend that owns a defibrillator. He'll let us borrow it." 
    g "Does he live very far away? I don't love the idea of going out in the middle of a zombie attack!"
    show Eva pensive
    e "You're right, it could be risky. I'll stay here and protect my new creation."
    sv "A silent beat. Click twice to continue."
    g "..."
    
    call sc_black from _call_sc_black_3
    stop music fadeout 1
    "A few zombies were in the street, but I managed to get to my car without attracting their attention."
    call ms_end from _call_ms_end_1
    
    return