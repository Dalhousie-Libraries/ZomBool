label fr_visit_Sport:
    titleCard "Chapitre 1 de 2{vspace=30}Mieux vaut une arme pour se protéger?"
    $chosenPath = "Sport"
    
    stop music fadeout 3
    call sc_street from _call_sc_street
    "Les zombies me rendent très nerveux. Avant d'aller trouver l'ami d'Évangeline, j'aimerais trouver une arme pour mieux me protéger."
    "Je ne sais pas où aller pour trouver de quoi qui peut faire du vrai dommage, mais je sais où se trouve le {i}Sportgo Sport{/i} le plus près!"
    
    call sc_sportsGo_vide from _call_sc_sportsGo_vide
    
    "Ouf, il y avait un troupeau de zombies dehors et j'ai dû les contourner avant d'arriver à entrer."
    "C'est bien éclairé...mais sauf pour les rayons avec du linge, ça semble vide!" 
    s "C'est toi chérie?"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    call ms_ossuary from _call_ms_ossuary
    show Proprio unhappy at center with moveinright
    s "...DEHORS!"
    sv "La propriétaire du magasin de sport semble costaude."
    g "Euh, d'accord, mais c'est plein de zombies. Je veux acheter un bat de baseball, ou peut-être une raquette."
    s "Pour m'assomer avant de voler ce qui reste de mon stock? Non merci, ça ne m'intéresse pas. Au revoir!"
    g "Euh..."
    s "Tu as du sang sur ta face qui te vient de tes dernières victimes!"
    "...c'est vrai que j'ai lancé des morceaux de corps un peu partout ce matin."
    show Proprio satisfaction
    s "Moi, je n'ai pas de problème à me défendre si il le faut. Mais j'attends ma nièce et elle est très sensible."
    g "Je ne suis pas... je suis juste un étudiant."
    "Je m'essuie le visage."
    g "Ça c'était les victimes d'un zombie."
    show Proprio drill
    s "Prouve-le!"
    sv "Gabriel ne sait pas comment réagir. Cliquer deux fois pour continuer"
    g "?!"
    s "Prouve que tu es un étudiant. Je respecte les étudiants, ils travaillent fort. C'est quoi la dernière chose qu'ils t'ont enseigné à l'école?"
    
    "J'ai commencé à lui raconter la visite de la bibliothécaire."   
    
    return
    
label en_visit_Sport:
    titleCard "Chapter 1 of 2{vspace=30}Better protection with a weapon?"
    $chosenPath = "Sport"
    
    stop music fadeout 3
    call sc_street from _call_sc_street_1
    "The zombies are making me really nervous. Before finding Évangeline's friend, I need to find some sort of weapon I can use to protect myself."
    "I don't know where to go to find something that could make some real damage, but I do know where the nearest {i}Sportsgo Sports{/i} is located!"
    
    call sc_sportsGo_vide from _call_sc_sportsGo_vide_1
    
    "There's a zombie mob outside. I weave my way past them to get in."
    "The store is well lit...except for the clothes racks, it's fairly empty!" 
    s "Is that you honey?"
    sv "A silent beat. Click twice to continue."
    g "..."
    call ms_ossuary from _call_ms_ossuary_1
    show Proprio unhappy at center with moveinright
    s "...LEAVE!"
    sv "The sports store owner seems really strong."
    g "Um, sure, but there's a lot of zombies out there. Can I buy a baseball bat first, or maybe a tennis racquet?"
    s "So you can knock me out before stealing everything that's left of my stock? I don't think so! No thanks, go away!"
    g "Um..."
    s "There's still blood on your face from your last victims!"
    "...I did throw some body parts around earlier today."
    show Proprio satisfaction
    s "Me, I have no problems defending myself as needed. But I'm waiting for my niece and she's very sensitive."
    g "I'm not...I'm just a student."
    "I wipe my face."
    g "This came from victims of a zombie."
    show Proprio drill
    s "Prove it!"
    sv "Gabriel doesn't know how to react. Click twice to continue."
    g "?!"
    s "Prove that you're a student. I respect students, they work hard. What's the last thing they taught you in school?"
    
    "I can't think of anything else. I tell her about the librarian's visit."   
    
    return
                                                           
label fr_Sport_form:
    call ms_ossuary from _call_ms_ossuary_2
    call sc_sportsGo from _call_sc_sportsGo
    g "...et donc, les expressions booléennes sont des formules magiques qui permettent d'effectuer des recherches efficaces et qui fonctionnent dans pratiquement toutes les bases de données sauf qu'il 
       faut faire des modifications pour Google."
    show Proprio satisfaction
    s "D'accord, ton histoire ennuyante m'a convaincue. Tu es un étudiant. Mais il ne me reste plus beaucoup d'équipement en stock et faut avouer que tu n'est pas très costaud!"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    show Proprio drill
    s "Je ne veux pas te donner un bat de criquet juste pour le voir dans les mains d'un zombie 2 minutes plus tard!"
    g "Ça fait quand même plusieurs --"
    s "DONC! Tu vas me prouver que tu peux prendre soin de toi-même en arrêtant un zombie juste avec un coup de poing."
    "Euh...si je fais ça, je vais probablement me faire bouffer par un zombie. C'est une TRÈS MAUVAISE IDÉE."
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "Accepter d'essayer de battre un zombie avec un seul coup de poing.":
            jump bil_SportEnding
        "Proposer une alternative.":
            pass
    g "Et si à la place, je te raconte comment composé je peux rester même pendant une situation stressante?"
    show Proprio satisfaction
    s "On verra. Tu peux certainement t'essayer."
    
    call ms_party from _call_ms_party_7
    call sc_class from _call_sc_class_11
    "La journée avait mal commencée. Un quiz SURPRISE?! Des tests de l'alarme à feu qu'on doit ignorer, malgré le son perçant? Le chauffage incontrolable
        qui a monté la température dans la salle de classe à 35 degré celcius?"
    b "Je suis désolée! Votre professeur a insisté pour qu'on fasse quand même un petit test. Mais vous pouvez vous réessayer jusqu'à ce que vous trouvez les bonnes réponses."
    show Librarian intense
    b "Le scénario est le suivant: Vous êtes un détective qui enquête sur un vol de bijouterie."
    b "Après avoir vérifié les caméras de sécurité et parlé aux quelques témoins, vous dressez le portrait suivant du suspect:"
    show Librarian neutral
    b "Sa couleur préféré est le {=word}bleu{/=word}."
    b "Il a utilisé une raquette de {=word}badminton{/=word}, ou {=word}pickleball{/=word}, ou {=word}tennis{/=word}, ou {=word}ping-pong{/=word} pour entrer dans la bijouterie — une de ces options doit être son sport préféré."
    b "Il portait des {=word}lunettes{/=word} et une {=word}casquette{/=word} la journée qu'il a commit le crime."
    b "Vous devez utiliser un formulaire pour entrer ces informations dans une base de données ultra-secrète qui va fournir une liste des suspects qui correspondent à cette description."

    return
    
label en_Sport_form:
    call ms_ossuary from _call_ms_ossuary_3
    call sc_sportsGo from _call_sc_sportsGo_1
    g "...and so, boolean search expressions are magic formulas that allow us to do really effective searches that work in almost all databases except 
       we need to make some small modifications in Google."
    show Proprio satisfaction
    s "Alright, fine, your boring story convinced me. You're a student. But I don't have a lot of equipment left in stock and you have to admit you're not the most in shape person!"
    sv "A silent beat. Click twice to continue."
    g "..."
    show Proprio drill
    s "I don't want to give you a cricket bat only to see it in the hands of a zombie 2 minutes later!"
    g "Oh, but --"
    s "SO! You're going to show that you can take care of yourself by stopping a zombie using just one punch."
    "Um...if I do this, I'm definitely getting bit by a zombie. This is a VERY BAD IDEA."
    
    sv "Menu"
    $shuffle_menu()
    menu:
        "Agree to stop a zombie with just one punch.":
            jump bil_SportEnding
        "Suggest an alternative.":
            pass
    g "What if instead of doing that, I tell you about a time where I stayed cool and collected in a stressful situation?"
    show Proprio satisfaction
    s "We'll see. You can certainly try."
    
    call ms_party from _call_ms_party_8
    call sc_class from _call_sc_class_12
    "The day had started terribly. A SURPRISE quiz? Fire alarm tests we had to ignore, despite the screeching sound? The air conditioning dying, 
        boosting the temperature in the classroom to 35 degrees celcius?"
    b "I'm so sorry! Your professor insisted that we still do a little test. But you can try over and over again until you find the right answers."
    show Librarian intense
    b "The scenario is the following: you're a detective who is investigating a jewel theft."
    b "After checking security cameras and talking to a few witnesses, you learn a few things about the suspect."
    show Librarian neutral
    b "His favorite color is {=word}blue{/=word}."
    b "He used a {=word}badminton{/=word}, or {=word}pickleball{/=word}, or {=word}tennis{/=word}, or {=word}ping-pong{/=word} racket to get inside the jewelery store — one of these options must be his favorite sport."
    b "He was wearing {=word}glasses{/=word} and had a {=word}goatee{/=word} the day he committed the crime."
    b "You must use a form to enter this information in a super secret database that will spit out a list of suspects that fit that description."

    return

label fr_Sport_ch_Form:           
    #La bibliothécaire félicite la victory
    call sc_class from _call_sc_class_13
    show Librarian smiling
    if chMenu1 or chMenu2 or chMenu3:
        b "Bravo! Ça a pris un peu de travail, mais tu as réussi!"
    elif chMenu4:
        b "Wow, tu as réussi! Félicitation!"
    else:
        b "Super! Tu as vraiment bien compris la recherche booléenne!"
    
    call ms_ossuary from _call_ms_ossuary_4
    call sc_sportsGo from _call_sc_sportsGo_2
    #Conclusion de la réussite
    if flagCount == 4:
        g "Tu vois? Dans une situation stressante, j'ai persévéré et réussi mon quiz."
    elif flagCount == 3:
        g "Avec un peu de travail, j'ai donc réussi mon quiz en ignorant les stresseurs."
    elif flagCount == 2:
        g "J'ai bien performé malgré des conditions désagréables."
    elif flagCount == 1:
        g "Tu vois? J'ai à peine hésité avant de super bien réussir le quiz."
    else:
        g "Tu vois? Rien ne peux m'arrêter!"
    
    g "Et j'ai rapidement réglé les derniers petits problèmes avec mon formulaire."
    s "Oh non, arrête, c'est trop ennuyant!"
    call ms_party from _call_ms_party_9
    call sc_class from _call_sc_class_14

    show Librarian smiling
    b "Super! Il ne reste que des derniers petits problèmes que tu pourrais choisir de réparer."
    s "{size=+5}Tu m'entends? C'est beau! Tu peux arrêter de m'expliquer! Allo?{/size}"
    b "Les problèmes avec ton formulaire sont la langue utilisée pour la recherche, le nom, et les parenthèses."
    return
    
label en_Sport_ch_Form:           
    #La bibliothécaire félicite la victory
    call sc_class from _call_sc_class_15
    show Librarian smiling
    if chMenu1 or chMenu2 or chMenu3:
        b "Contratulations! It took a bit of work, but you did it!"
    elif chMenu4:
        b "Wow, you did it! Congratulations!"
    else:
        b "Excellent! You really understand boolean operators!"
    
    call ms_ossuary from _call_ms_ossuary_5
    call sc_sportsGo from _call_sc_sportsGo_3
    #Conclusion de la réussite
    if flagCount == 4:
        g "You see? Despite the stress of everything going on, I persevered and passed my quiz."
    elif flagCount == 3:
        g "With a bit of work, I completed my quiz while ignoring all external stressors."
    elif flagCount == 2:
        g "I performed well despite deplorable conditions."
    elif flagCount == 1:
        g "You see? I barely hesitated before crushing the quiz."
    else:
        g "You see? No amount of stress can stop me!"
    
    g "And I quickly fixed some last little problems with my form."
    s "Oh no, please stop, I'm so bored!"
    call ms_party from _call_ms_party_10
    call sc_class from _call_sc_class_16

    show Librarian smiling
    b "Great! You only have a few little modifications to make before your search expression is perfect."
    s "{size=+5}Can you hear me? It's fine! You can stop explaining! Hello???{/size}"
    b "Problems with your formula include capitals, brackets, and names."
    return
    
label fr_Sport_ch_Form2:
    if not (chMenu1 and chMenu2 and chMenu3):
        sv "Menu"
    $shuffle_menu()
    menu:
        "Que veux-tu réparer?"
        "Problèmes avec la langue!" if not chMenu1:
            $chMenu1 = True
            
            g "Un problème avec la langue?"
            show Librarian intense
            b "Absolument!"
            g "Mais j'ai tout écrit en français, et j'ai bien épellé les mots de ma recherche."
            b "Exactement!"
            g "Je ne comprends pas?!"
            b "On ne doit pas traduire les opérateurs booléens."
            b "{=bool}ET{/=bool} devrait être {=bool}AND{/=bool}. {=bool}OU{/=bool} devrait être {=bool}OR{/=bool}."
            g "Mais on est tous des francophones ici! Et c'est ce que vous avez mis sur le formulaire pour m'aider à construire ma phrase!"
            show Librarian neutral
            b "Ça fait partie du quiz. La plupart des bases de données {i}y compris les bases de données francophones{/i} fonctionnent avec les opérateurs
                {=bool}AND{/=bool} et {=bool}OR{/=bool}."
            b "Le nombre d'exceptions est tellement minuscule que c'est mieux de s'habituer à utiliser les opérateurs booléens {=bool}AND{/=bool} et {=bool}OR{/=bool}."
            b "Mais ce n'est pas tout...J'ai déjà expliqué tout ça à ta classe! Tu te souviens?"
            
            call fr_langue from _call_fr_langue
            
            g "J'ai bien compris. Je te remplis un nouveau formulaire?"
            b "Corrige tes opérateurs booléens."
            show Librarian smiling
            b "Pas besoin de traduire les mots clés pour ce quiz."

            if chMenu2 and chMenu3:
                g "Ouf, j'ai terminé!"
                show Librarian smiling
                b "Oui!"
            elif chMenu2 or chMenu3:
                g "Je ne veux pas être obligé de refaire 100 fois le travail."
                g "Quel est le dernier problème avec mon formulaire?"
            else:
                g "Bon, quoi d'autre faut-il changer avec le formulaire?"
                
            jump fr_Sport_ch_Form2
       
        "Absence de parenthèses!" if not chMenu2:
            $chMenu2 = True
            
            b "Il te manque seulement les parenthèses."
            g "Des parenthèses? Tu veux que j'ajoute des parenthèses à mon expression de recherche booléenne?"
            show Librarian smiling
            b "Oui!"
            g "Où? Comment? Pourquoi?"
            show Librarian intense
            b "C'est comme pour l'ordre des opérateurs en mathématique. Pour ne pas mélanger l'ordinateur, il faut lui dire quoi faire en premier."
            b "La recherche de synonymes a priorité."
            show Librarian neutral
            if not chMenu1:
                b "On doit chercher des synonymes avec {=bool}OU{/=bool} avant d'ajouter des concepts avec {=bool}ET{/=bool}."
            else:
                b "On doit chercher des synonymes avec {=bool}OR{/=bool} avant d'ajouter des concepts avec {=bool}AND{/=bool}."
            g "Alors je mets des parenthèses pour entourer...tous les sports, et toutes les couleurs? Des parenthèses pour chaque concepts!"
            show Librarian smiling
            b "Exactement! Si on utilise plus qu'un synonyme, chaque idée est encapsulée par des parenthèses pour dire que des mots différents sont utilisés pour exprimer une même idée."
            g "Wow! Je pense que je comprends!"
            
            sv "Menu"
            $unshuffle_menu()
            menu:
                "J'ai compris l'utilisation de parenthèses dans la recherche booléenne?"
                "Oui":
                    pass
                "Non":
                    show Librarian neutral
                    b "Tu dis que tu comprends, mais tu n'as pas l'air très convaincu."
                    sv "Un moment de silence. Cliquez deux fois pour continuer."
                    g "..."

                    if not chMenu1:
                        show Librarian intense
                        b "Si je vais à une animalerie et j'achète un {=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word} {=bool}ET{/=bool} {=word}laisse{/=word}"
                        b "Avec quoi je vais sortir de l'animalerie?"
                        sv "Gabriel ne sait pas la réponse. Cliquer deux fois pour continuer."
                        g "???"
                        sv "Mode voix bibliothécaire. Chien OU ouvre parenthese chat ET laisse ferme parenthese."
                        b "{=word}chien{/=word} {=bool}OU{/=bool} ({=word}chat{/=word} {=bool}ET{/=bool} {=word}laisse{/=word})"
                        b "Je vais avoir un {=word}chien{/=word}. Ou bien je vais avoir un {=word}chat{/=word} et une {=word}laisse{/=word}?"
                        sv "Mode voix bibliothécaire. Ouvre parenthèse chien OU chat ferme parenthèse. Et laisse."
                        b "({=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word}) {=bool}ET{/=bool} {=word}laisse{/=word}"
                        b "Je vais avoir un {=word}chien{/=word} ou un {=word}chat{/=word}. Et je vais toujours sortir de l'animalerie avec une {=word}laisse{/=word}!"
                        sv "Un moment de silence. Cliquez deux fois pour continuer."
                        g "..."
                        show Librarian neutral
                        b "Tu as l'air encore plus mélangé!"
                        g "Oui. Désolé!"
                        b "La règle est simple. Mets des parenthèses pour entourer tous les synonymes d'un concept."
                        b "Si tu as des {=bool}OU{/=bool}, tu dois entourer tous les mots reliés par des {=bool}OU{/=bool} par des parenthèses."
                        sv "Mode voix bibliothécaire. Ouvre parenthèse chien OU chat ferme parenthèse ET laisse."
                        b "({=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word}) {=bool}ET{/=bool} {=word}laisse{/=word}"
                        sv "Mode voix bibliothécaire. Ouvre parenthèse école OU université ferme parenthèese. ET ouvre parenthèse réussite OU succèes ferme parenthèse."
                        b "(ecole {=bool}OU{/=bool} université) {=bool}ET{/=bool} (réussite {=bool}OU{/=bool} succès)"
                        g "Je pense que j'ai compris! Merci!"
                    else:
                        show Librarian intense
                        b "Si je vais à une animalerie et j'achète un {=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word} {=bool}AND{/=bool} {=word}laisse{/=word}"
                        b "Avec quoi je vais sortir de l'animalerie?"
                        sv "Gabriel ne sait pas la réponse. Cliquer deux fois pour continuer."
                        g "???"
                        sv "Mode voix bibliothécaire. Chien OR ouvre parenthese chat AND laisse ferme parenthese... Je vais avoir un chien. Ou bien je vais avoir unc hat et une laisse?"
                        b "{=word}chien{/=word} {=bool}OR{/=bool} ({=word}chat{/=word} {=bool}AND{/=bool} {=word}laisse{/=word})... Je vais avoir un {=word}chien{/=word}. Ou bien je vais avoir un {=word}chat{/=word} et une {=word}laisse{/=word}?"
                        sv "Mode voix bibliothécaire. Ouvre parenthèse chien OR chat ferme parenthèse. AND laisse... Je vais avoir un chien ou un chat. Et je vais toujours sortir de l'animalerie avec une laisse?"
                        b "({=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word}) {=bool}AND{/=bool} {=word}laisse{/=word}... Je vais avoir un {=word}chien{/=word} ou un {=word}chat{/=word}. Et je vais toujours sortir de l'animalerie avec une {=word}laisse{/=word}!"
                        sv "Un moment de silence. Cliquez deux fois pour continuer."
                        g "..."
                        show Librarian neutral
                        b "Tu as l'air encore plus mélangé!"
                        g "Oui. Désolé!"
                        b "Oh non, c'est à moi de mieux expliquer. Mets des parenthèses pour entourer tous les synonymes d'un concept."
                        b "Si tu as des {=bool}OR{/=bool}, tu dois entourer tous les mots reliés par des {=bool}OR{/=bool} par des parenthèses."
                        sv "Mode voix bibliothécaire. Ouvre parenthèse chien OU chat ferme parenthèse ET laisse."
                        b "({=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word}) {=bool}AND{/=bool} {=word}laisse{/=word}"
                        sv "Mode voix bibliothécaire. Ouvre parenthèse école OU université ferme parenthèese. ET ouvre parenthèse réussite OU succèes ferme parenthèse."
                        b "(ecole {=bool}OR{/=bool} université) {=bool}AND{/=bool} (réussite {=bool}OR{/=bool} succès {=bool}OR{/=bool} success)"
                        g "Je pense que j'ai compris! Merci!"
            
            if chMenu1 and chMenu3:
                g "Bon, je vais corriger mon formulaire! Merci madame!"
            else:
                g "Cette fois-ci, avant de corriger le formulaire, j'aimerais en savoir plus à propos des autres problèmes que tu as décelés."
                
            jump fr_Sport_ch_Form2
        
        "Nom?" if not chMenu3:
            $chMenu3 = True
            
            show Librarian neutral
            b "Tu as oublié d'écrire ton nom sur le formulaire."
            s "..pas très impressionant."
            g "Oh non! Merci de me l'avoir signalé!"

            jump fr_Sport_ch_Form2
        
    g "Je sais maintenant quoi faire."
    "J'ai réussi à remplir rapidement le formulaire, et j'ai même ajouté des mots clés en anglais, ce qui m'a mené à l'expression de recherche booléenne suivante:"
    sv "Mode voix narration. Ouvre parenthèse badminton OR pickleball OR tennis OR ping-pong ferme parenthèse. AND ouvre parenthèse lunette OR glasses ferme parenthèse.
        AND ouvre parenthèse casquette OR baseball cap ferme parenthèse. AND ouvre parenthèse bleu OR blue ferme parenthèse."
    "({=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} 
     {=word}ping-pong{/=word}) {=bool}AND{/=bool} ({=word}lunettes{/=word} {=bool}OR{/=bool} {=word}glasses{/=word}) {=bool}AND{/=bool} ({=word}casquette{/=word} {=bool}OR{/=bool} {=word}baseball cap{/=word}) {=bool}AND{/=bool} ({=word}bleu{/=word} {=bool}OR{/=bool} {=word}blue{/=word})"
    show Librarian smiling
    b "Bravo! Tu as réussi! Et tu vas voir! Composer des expressions de recherche booléenne va être de plus en plus facile!"
    
    return
    
label en_Sport_ch_Form2:
    if not (chMenu1 and chMenu2 and chMenu3):
        sv "Menu"
    $shuffle_menu()
    menu:
        "What do you want to fix?"
        "Capitals!" if not chMenu1:
            $chMenu1 = True
            
            g "What's wrong with my capitals?"
            show Librarian neutral
            b "Actually, nothing's wrong!"
            sv "A silent beat. Click twice to continue."
            g "..."
            show Librarian intense
            b "I just want to make sure you know why we capitalize {=bool}AND{/=bool} and  {=bool}OR{/=bool}. Think about it for a second."
            g "Is it so that the computer doesn't search for the {i}words{/i} 'or' and 'and'?"
            b "That's right! Great guess!"
            s "{size=+5}Alright, alright, are you done now?{/size}"
            
            if chMenu2 and chMenu3:
                g "So that's it?"
                show Librarian smiling
                b "Yes!"
            elif chMenu2 or chMenu3:
                g "That was easy! What's left to fix?"
                show Librarian smiling
            else:
                g "So is anything actually wrong with the form? What's next?"
                show Librarian smiling
                
            jump en_Sport_ch_Form2
       
        "Brackets!" if not chMenu2:
            $chMenu2 = True

            g "Brackets? You want me to add brackets to my boolean search expression?"
            show Librarian smiling
            b "Yes!"
            g "Where? How? Why?"
            show Librarian intense
            b "It's just like the order of operations in mathematics. To avoid confusing the computer, we tell it what operation to do first with brackets."
            show Librarian neutral
            b "Synonyms are a priority. We have to search synonyms with {=bool}OR{/=bool} before adding concepts with {=bool}AND{/=bool}."
            g "So I put parentheses around...all the sports, the colors, the accessories, and the facial distinctions?"
            show Librarian smiling
            b "Exactly! If more than one word is used to express a concept, they are surrounded in parentheses so that we know that the different words 
               are all part of one big idea."
            g "Wow! I think I get it!"
            
            sv "Menu"
            $unshuffle_menu()
            menu:
                "I understand the use of parentheses in boolean searches?"
                "Yep!":
                    pass
                "Nope!":
                    show Librarian neutral
                    b "You say you get it, but you don't look very convinced."
                    sv "A silent beat. Click twice to continue."
                    g "..."
                    show Librarian intense
                    b "If I go to a local animal shelter and buy a {=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word} {=bool}AND{/=bool} {=word}collar{/=word}"
                    b "What will I have with me when I come out of the animal shelter?"
                    sv "Gabriel doesn't know the answer. Click twice to continue."
                    g "???"
                    sv "Self-voiced Librarian. Dog OR open parentheses cat AND collar close parentheses. I'll have a {=word}dog{/=word}. Or the other alternative is that I'll have a {=word}cat{/=word} and a {=word}collar{/=word}?"
                    b "{=word}dog{/=word} {=bool}OR{/=bool} ({=word}cat{/=word} {=bool}AND{/=bool} {=word}collar{/=word})... I'll have a {=word}dog{/=word}. Or the other alternative is that I'll have a {=word}cat{/=word} and a {=word}collar{/=word}?"
                    sv "Self-voiced Librarian. Open parentheses Dog OR cat close parentheses AND collar. I'll have a {=word}dog{/=word} or a {=word}cat{/=word}. And I'll always come out of the shelter with a {=word}collar{/=word} for it!"
                    b "({=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word}) {=bool}AND{/=bool} {=word}collar{/=word}... I'll have a {=word}dog{/=word} or a {=word}cat{/=word}. And I'll always come out of the shelter with a {=word}collar{/=word} for it!"
                    sv "A silent beat. Click twice to continue."
                    g "..."
                    show Librarian neutral
                    
                    b "You look even more confused!"
                    g "Sorry!"
                    b "Oh no, don't apologize, I need to explain better. You put parentheses to bracket all synonyms of a concept."
                    b "If you have any {=bool}ORs{/=bool}, you should surround all words linked by {=bool}ORs{/=bool} with parentheses."
                    sv "Self-voiced Librarian. Open parentheses dog OR cat close parentheses AND collar."
                    b "({=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word}) {=bool}AND{/=bool} {=word}collar{/=word}"
                    sv "Self-voiced Librarian. Open parentheses school OR university close parentheses AND open parentheses success OR achievement OR accomplishment close parentheses."
                    b "(school {=bool}OR{/=bool} university) {=bool}AND{/=bool} (success {=bool}OR{/=bool} achievement {=bool}OR{/=bool} accomplishment)"
                    g "I think I get it now! Thanks!"

            if chMenu1 and chMenu3:
                g "Well, I'm going to fix my form! Thanks Miss!"
            else:
                g "Before I bother submitting a new form, I would like to know more about the other problems I should correct. What's next?"
                
            jump en_Sport_ch_Form2
        
        "Name?" if not chMenu3:
            $chMenu3 = True
            
            show Librarian neutral
            b "You forgot to put your name on the form."
            s "That's not very impressive."
            g "Oh no! Thanks for letting me know!"

            jump en_Sport_ch_Form2
        
    g "I know what to do now."
    "I quickly finish filling out the form, creating the following search expression:"
    sv "Self-voiced narration. Open parentheses badminton OR pickeball OR tennis OR ping-pong close parentheses. AND glasses AND goatee AND blue."
    "({=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} 
     {=word}ping-pong{/=word}) {=bool}AND{/=bool} {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word} {=bool}AND{/=bool} {=word}blue{/=word}"
    show Librarian smiling
    b "Congratulations! You got it! And you'll see! Creating boolean search expressions will get easier and easier!"
    
    return

label fr_Sport_safe:
    $safeIC = 1
    $safeCIB = 2
    $safeWord = "Sportif"
    
    call ms_ossuary from _call_ms_ossuary_6
    call sc_sportsGo from _call_sc_sportsGo_4
    show Proprio unhappy
    s "Ton exemple d'une situation stressante, c'est de réussir un quiz?"
    s "Ton histoire ennuyante m'a au moins convaincue que tu es inoffensif."
    show Proprio drill
    s "Tu peux aller en arrière et sortir une arme de mon coffre-fort."
    
    scene bg safe with dissolve
    "Je suis allé en arrière."
    hide Proprio
    g "C'est quoi le code pour ouvrir le coffre-fort?"
    s "{size=-2}Sportif...faut 6 chiffres.{/size}"
    g "Sportif, c'est 7 lettres! Pas 6 chiffres!"
    s "{size=-2}Tu vas voir que tu vas réussir à ouvrir si tu as un cerveau!{/size}"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    
    sv "J'examine le mécanisme. C'est un clavier téléphonique. Les numéros sont associés avec des lettres."
    window hide
    $renpy.pause(2.0)
    window show
    
    "La petite étoile qui se trouve à la position '0' est une astérix. Ça me rappèle des souvenirs de la Bibliothécaire!"
    call fr_troncature from _call_fr_troncature
    
    call ms_ossuary from _call_ms_ossuary_7
    scene bg safe with dissolve
    "Je sais comment procéder pour épeller le mot 'Sportif' avec 6 chiffres!"
    sv "Utiliser la flêche vers le haut et la flêche vers le bas pour naviguer sur les différents numéros du clavier électronique dans le prochain écran."
    sv "Après deux entrées incorrectes, 4 codes — 1 des codes est correct — pourront être sélectionné."    
    call fr_load_safe from _call_fr_load_safe #in pthJoint
    call sc_sportsGo from _call_sc_sportsGo_5
    
    "Il contient des raquettes et un bat de baseball avec le logo de Sportgo Sport. Pourquoi mettre ça dans un coffre-fort?"
    g "Super! Merci pour le bat de baseball!"
        
    return
    
label en_Sport_safe:
    $safeIC = 3
    $safeCIB = 2
    $safeWord = "Achievement"
    
    call ms_ossuary from _call_ms_ossuary_8
    call sc_sportsGo from _call_sc_sportsGo_6
    show Proprio unhappy
    s "Your example of handling a stressful situation is working on a quiz?"
    s "Your boring story has at least convinced me that you're not dangerous."
    show Proprio drill
    s "You can go in the stock room and take out a weapon from the safe."
    
    scene bg safe with dissolve
    "I go in the back."
    g "What's the code for the safe?"
    s "{size=-2}Achievement...you need 6 numbers.{/size}"
    g "'Achievement' has 11 letters! Not 6 numbers!"
    s "{size=-2}You'll see that you can get the safe open if you have half a brain!{/size}"
    sv "A silent beat. Click twice to continue."
    g "..."
    
    sv "I examine the mechanism. It's a keypad. The numbers are associated with letters."
    window hide
    $renpy.pause(2.0)
    window show
    
    "The little asterix besides the '0' reminds me of the librarian's visit!"
    call en_troncature from _call_en_troncature
    
    call ms_ossuary from _call_ms_ossuary_9
    scene bg safe with dissolve
    "I know how to proceed to spell 'achievement' with 6 numbers!"
    sv "You will have to enter a code on the screen. Use the up or down arrow on the keyboard to select a different number on the keypad."
    sv "After two wrong attempts, a list of 4 possible codes will appear and can be selected on the screen. One of the codes will be the correct code."
    call fr_load_safe from _call_fr_load_safe_1 #in pthJoint
    call sc_sportsGo from _call_sc_sportsGo_7
    
    "The safe contains racquets and a baseball bat with the SportsGo Sports logo. Why put that in a safe?"
    g "Great! Thanks for the baseball bat!"
        
    return

label fr_Venn_Sport:

    show Proprio drill
    s "Avant de te laisser partir avec mon équipement, on va vérifier que tu sais comment l'utiliser."
    "Elle m'emmène à une machine étrange et me donne le bat de baseball."
    show Proprio happy
    s "Ça permet de vérifier ta vision et dextérité. Une pièce d'équipement standard!"
    s "Si j'ai bien compris, je peux te demander..."
    
    call choixMenu from _call_choixMenu
    call cleanMadGab from _call_cleanMadGab_2
    
    $myList = (('{b}  Sport                               Profit{/b}', 'Sport','Profit'))
    call fr_Venn_Setup from _call_fr_Venn_Setup
    call sc_sportsGo from _call_sc_sportsGo_8
    
    g "...j'ai réussi!"
    show Proprio satisfaction
    s "Bravo."
    "Un zombie frappe contre la porte et nous fait sursauter."
    g "S.v.p.?"
    show Proprio drill
    s "C'est bon, tu peux garder le bat de baseball. Et j'ai un casque que je peux te donner."
    "Un autre zombie frappe contre la porte pendant qu'elle trouve et me passe le casque."
    show Proprio happy
    s "Bonne chance!"

    g "Vient avec moi! Ce n'est pas sécuritaire d'être toute seule."
    show Proprio drill
    if kitten:
        s "Tu n'es pas le premier à me le demander, mais je veux attendre ma belle-fille et son chat."
    else:
        s "Tu n'es pas le premier à me le demander, mais je veux attendre ma belle-fille."
    
    return
    
label en_Venn_Sport:

    show Proprio drill
    s "Before I let you leave the store with my stuff, we're going to check that you know how to use it."
    "She brings me to a strange machine and hands me the baseball bat."
    show Proprio happy
    s "This gizmo allows me to check your vision and dexterity. A standard piece of equipment!"
    s "If I remember how this thing is set up, I should ask you to..."
    
    call choixMenu from _call_choixMenu_1
    call cleanMadGab from _call_cleanMadGab_3
    
    $myList = (('{b}  Sport                               Profit{/b}', 'Sport','Profit'))
    call en_Venn_Setup from _call_en_Venn_Setup
    call sc_sportsGo from _call_sc_sportsGo_9
    
    g "...I did it!"
    show Proprio satisfaction
    s "Great."
    "A zombie stumbles near the door and startles us."
    g "Please, can I go?"
    show Proprio drill
    s "It's fine, you can keep the baseball bat. And I have a helmet you might be able to use."
    "Another zombie hits the door while she finds the helmet."
    show Proprio happy
    s "Well...good luck!"

    g "Come with me! It's not safe here for you all alone."
    show Proprio drill
    if kitten:
        s "You're not the first person to ask, but I need to wait for my daughter in law and her cat."
    else:
        s "You're not the first person to ask, but I need to wait for my daughter in law."
    
    return
    
label fr_Sport_invitation:
    $companion = True
    
    g "On peut laisser une note!"
    show Proprio unhappy
    "La propriétaire a l'air triste mais hoche la tête."
    s "Ça fait longtemps que je l'attends. Elle doit être coincée chez elle."
    "Je n'ose pas rien dire."
    
    if flag3 >= 4:
        "La propriétaire a silencieusement rammassé deux autres bats de baseball."
    elif flag3 == 3:
       "La propriétaire a silencieusement ramassé deux raquettes et trois bats de baseball."
    elif flag3 == 2:
        "La propriétaire a silencieusement rammassé plusieurs bats de baseball, des raquettes, et des casques."
    elif flag3 == 1:
        "La propriétaire a silencieusement rammassé des épées d'escrime, un arc et des flêches, des bats de baseball, et des casques."
        "Comment va-t-on transporter tout ça?"
    else:
        "La propriétaire a silencieusement rammassé des épées d'escrime, des arbalettes, des fusils de paintball, des casques, et un uniforme d'arbitre."
        "Comment va-t-on transporter tout ça?"
        
    "On est parti trouver Évangeline"
        
    return
    
label en_Sport_invitation:
    $companion = True
    
    g "We could leave a note!"
    show Proprio unhappy
    "The SportsGo Sports owner looks sad, but nods her head."
    s "I've been waiting such a long time. She must be stuck at her place."
    "I don't want to say anything."
    
    if flag3 >= 4:
        "The owner silently grabs two other baseball bats from the safe."
    elif flag3 == 3:
       "The owner silently grabs two tennis raquets and three baseball bats from the safe."
    elif flag3 == 2:
        "The owner silently grabs several baseball bats, all kinds of racquets, and helmets from the safe."
    elif flag3 == 1:
        "The owner silently grabs fencing swords, a bow and arrow, baseball bats, and helmets from somewhere in the stock room."
        "How are we going to carry all of this stuff?"
    else:
        "The owner silently grabs fencing swords, bows and arrows, paintball guns, helmets, and a referee uniform from the stock room."
        "How are we going to carry all of this stuff?"
        
    "We leave to find Évangeline."
        
    return
    
label fr_Sport_aurevoir:
    
    g "Je comprends. Si ma famille habitait ici...j'attendrais aussi longtemps que possible."
    g "On repassera te voir plus tard! Je veux te souhaiter bonne chance!"
    show Proprio drill
    s "Merci, mais ne t'inquiète pas pour moi. Je sais me défendre."
    g "Est-ce qu'il te reste de l'équipement?"
    s "Pour ceux prêt à répondre à mes questions!"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    "La propriétaire m'a donné des bats de baseballs supplémentaire."
    "Après l'avoir remerciée une dernière fois, je suis parti retrouver Évangeline."
    
    return
    
label en_Sport_aurevoir:
    
    g "I get it. If my family lived here...I would wait as long as I could. We'll swing by here some other time! Best of luck!"
    show Proprio drill
    s "Thanks, but don't worry about me. I know how to defend myself."
    g "Is there much equipment left?"
    s "There's always something for people that pass my interrogation and strict dexterity test!"
    sv "A silent beat. Click twice to continue."
    g "..."
    "The owner gives me a few extra baseball bats. After thanking her one last time, I leave to find Évangeline."
    
    return
    
label bil_SportEnding:
    
    $sports_early = 1
    
    if lang == "english":
        "And that's how I died. I tried to punch a zombie and it didn't work. What a sad and tragic story! What a terrible decision on my part!"
        "If only I could go back in time by clicking 'Back' and make a better choice!"
        "It's so sad!"
    else:
        "Et c'est comme ça que je suis mort. J'ai essayé d'assomer un zombie et ça n'a pas fonctionné. Quelle histoire triste et tragique! Quelle terrible décision de ma part!"
        "Si seulement je pouvais retourner dans le temps en cliquant 'retour', et faire un meilleur choix!"
        "C'est tellement triste!"
                
    return
    