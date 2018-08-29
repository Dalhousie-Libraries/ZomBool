label fr_visit_Pharm:
    titleCard "Chapitre 1 de 2{vspace=30}Un cerveau en danger?"
    $chosenPath = "Pharmacy"
    
    stop music fadeout 3
    call sc_street from _call_sc_street_2
    "Je n'ai pas croisé beaucoup de zombies, mais je n'aime pas l'idée d'être séparé d'Évangeline."
    "Je ne connais même pas son ami... un étudiant d'art dramatique qui habite dans une résidence pour étudiants de la Faculté des arts?"
    "J'ai plus de chances de trouver ce dont j'ai besoin dans un hôpital...ou peut-être une pharmacie."
    
    call sc_pharm_vide from _call_sc_pharm_vide
    
    "Ça a l'air vide..."
    
    call ms_ossuary from _call_ms_ossuary_11
    show Pharma afraid at center with moveinright

    p "Bonjour!!!"
    sv "Un pharmacien apparaît devant moi. Il semble terrifié."
    "Ahhhhhh!"
    g "Euh, bonjour, je cherch-"
    show Pharma happy
    p "Je suis TELLEMENT CONTENT que tu peux me comprendre."
    show Pharma terrified
    p "Regarde ça! J'ai remarqué une égratinure sur mon bras. Ça vient de mon chat...ou d'un zombie?"
    g "Euh..."
    p "J'ai entendu dire que la capacité de raisonner est une des premières choses à disparaître lorsqu'on est affecté."
    show Pharma afraid
    p "Est-ce que je deviens progressivement plus stupide?"
    g "Euh.."
    show Pharma terrified
    p "EST-CE QUE JE VAIS DEVENIR UN STUPIDE ZOMBIE???"
    p "Faut tester! Tu dois m'aider!"
    g "Je ne sais pas si je peux t'aider! Je ne connais rien à la médecine ou aux médicaments."
    show Pharma happy
    p "Non, ne t'inquiète pas pour ça, on n'a pas de bons tests pour détecter le zombisme. Faut tester comment bien mon cerveau fonctionne!"
    
    if kitten:
        p "Vite, répond à ma question! Est-ce que tu aime les minous?"
        sv "Menu"
        $shuffle_menu()
        menu:
            "Est-ce que j'aime les minous?"
            "Oui!!!":
                p "Moi aussi!!!"
                p "...mais ça ne prouve rien."
            "Absolument!!":
                p "J'aime beaucoup les minous!"
                p "...mais ça ne prouve rien."
        
    p "Connais-tu les opérateurs booléens?"
    "Quelle question! Je ne peux pas m'empêcher de penser à la visite de la bibliothécaire..."
    
    return
    
label en_visit_Pharm:
    titleCard "Chapter 1 of 2{vspace=30}A brain in danger or a dangerous brain?"
    $chosenPath = "Pharmacy"
    
    stop music fadeout 3
    call sc_street from _call_sc_street_3
    "I don't come accross many zombies, but I hate being separated from Évangeline."
    "I don't even know her friend...a drama student that lives in a dorm for art students?"
    "I'll have better luck finding what we need in a hospital...or a pharmacy."
    
    call sc_pharm_vide from _call_sc_pharm_vide_1
    
    "It looks empty..."
    
    call ms_ossuary from _call_ms_ossuary_12
    show Pharma afraid at center with moveinright

    p "Hello!!!"
    sv "A pharmacist appears in front of me. He seems terrified."
    "Ahhhhhh!"
    g "Um, hi, I'm looki-"
    show Pharma happy
    p "I'm SO HAPPY you can actually understand me."
    show Pharma terrified
    p "Look at this! I have a scratch on my arm. Is it from my cat...or from a zombie?"
    g "Um..."
    p "I hear that higher brain functions are the first to go when you've been contaminated."
    show Pharma afraid
    p "Am I getting progressively stupider?"
    g "Um.."
    show Pharma terrified
    p "AM I GOING TO BECOME A STUPID ZOMBIE???"
    p "I have to know! You have to help!"
    g "I don't know if I can help! I don't know much about medical stuff or medicines."
    show Pharma happy
    p "That's fine, there's no good medical tests to detect zombism. We have to test how well my brain is working!"
    
    if kitten:
        p "Quick, answer my question! Do you like cats?"
        sv "Menu"
        $shuffle_menu()
        menu:
            "Do I like cats?"
            "Yes!!!":
                p "Me too!!!"
                p "...but that doesn't prove anything."
            "Absolutely!!":
                p "I really love cats!"
                p "...but that doesn't prove anything."
    
    p "Do you know about boolean operators?"
    "What a question! I can't help but think back to the librarian's visit..."
    
    return
                                                           
label fr_Pharm_form:
    call ms_ossuary from _call_ms_ossuary_13
    call sc_pharm from _call_sc_pharm
    p "C'est vraiment magique la façon que tu peux créer une expression de recherche booléenne puis la réutiliser dans toutes les bases de données. Et dans 
       Google avec quelques modifications."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    g "..."
    show Pharma happy
    p "Je vais tester mon cerveau en remplissant un formulaire capable de trouver mon frère dans la base de données de clients de SportGo Sport."
    p "Sa couleur préférée est le {=word}bleu{/=word}."
    p "Il aime le {=word}badminton{/=word}, et le {=word}pickleball{/=word}, et le {=word}tennis{/=word}, et le {=word}ping-pong{/=word}."
    p "Il porte toujours des {=word}lunettes{/=word} et une {=word}casquette{/=word}."
    show Pharma afraid
    "Il griffone sur un morceau de papier."
    p "Tiens, construit un corrigé pour que je puisse comparer nos réponses."
    g "Je ne suis pas certain que c'est nécessaire de-"
    show Pharma terrified
    p "VITE, avant qu'il soit trop tard!!!"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    "..."
    
    return
    
label en_Pharm_form:
    call ms_ossuary from _call_ms_ossuary_14
    call sc_pharm from _call_sc_pharm_1
    p "It's magical how a boolean search expression can be recycled in all kinds of databases. Or in Google with some small modifications."
    sv "A silent beat. Click twice to continue."
    g "..."
    show Pharma happy
    p "I'm going to test my brain by filling out a form that can find my brother in the client database of SportsGo Sports."
    p "{=word}Blue{/=word} is his favorite color."
    p "He loves {=word}badminton{/=word}, and {=word}pickleball{/=word}, and {=word}tennis{/=word}, and {=word}ping-pong{/=word}."
    p "He always wears {=word}glasses{/=word} and has a {=word}goatee{/=word}."
    show Pharma afraid
    "He writes down something on a piece of paper."
    p "Here, make an answer sheet so that I can compare our answers."
    g "I'm not sure that it's necess-"
    show Pharma terrified
    p "Let's do this FAST, before it's too late!!!"
    sv "A silent beat. Click twice to continue."
    "..."
    
    return

label fr_Pharm_ch_Form:
    
    #Le pharmacien félicite la victoire
    if chMenu1 or chMenu2 or chMenu3:
        p "Ça a pris un peu de travail, mais on as réussi!"
    elif chMenu4:
        p "Wow, on as réussi sans gaspiller trop de formulaires!"
    else:
        p "Super! On comprend les deux la recherche booléenne!"
    
    call sc_pharm from _call_sc_pharm_2
    
    #Charlie redemande le formulaire
    if flagCount == 4:
        show Pharma terrified
        p "Mais ça a pris du temps. TELLEMENT DE TEMPS. Est-ce que c'est en train d'arriver? Je perds mon intelligence?"
    elif flagCount == 3:
        show Pharma terrified
        p "Mais pas aussi rapidement que je l'aurais voulu. JE PERDS LA BOULE???"
    elif flagCount == 2:
        show Pharma afraid
        p "Est-ce que mes explications étaient assez claires? Ça n'a pas été aussi rapide que je l'aurais voulu!"
        g "Oui, oui..."
    elif flagCount == 1:
        show Pharma relieved
        p "C'était un bon test de mes habilités!"
    else:
        show Pharma happy
        p "Du premier coup! DU PREMIER COUP!"
        show Pharma terrified
        p "Est-ce que c'était trop rapide?"
        
    p "AHHHHH!"
    show Pharma terrified
    p "Et je ne peux pas célébrer notre succès! À quoi je pensais? Il y a encore des problèmes avec le formulaire!!!"
    p "EST-CE QUE JE DEVIENS UN ZOMBIE???"
    g "Calme-toi, on va régler ça ensemble sur mon corrigé!"
    
    show Pharma relieved
    
    return
    
label en_Pharm_ch_Form:
    
    #Le pharmacien félicite la victoire
    if chMenu1 or chMenu2 or chMenu3:
        p "It took a bit of work, but we did it!"
    elif chMenu4:
        p "Wow, we achieved success without wasting too many forms!"
    else:
        p "Awesome! We {i}both{/i} understand boolean search expressions!"
    
    call sc_pharm from _call_sc_pharm_3
    
    #Charlie redemande le formulaire
    if flagCount == 4:
        show Pharma terrified
        p "But it took time. SO MUCH TIME. Is it happening? Am I losing it?"
    elif flagCount == 3:
        show Pharma terrified
        p "But this took longer than I would have expected. I'M LOSING IT???"
    elif flagCount == 2:
        show Pharma afraid
        p "Were my explanations clear enough? This took longer than I would have wanted!"
        g "Sure..."
    elif flagCount == 1:
        show Pharma relieved
        p "This was a good test of my abilities!"
    else:
        show Pharma happy
        p "The first try! ON THE FIRST TRY!"
        show Pharma terrified
        p "Was that {i}too{/i} fast?"
        
    p "AHHHHH!"
    show Pharma terrified
    p "What am I thinking? I can't celebrate our success at all! There's still problems with the form!!!"
    p "AM I TURNING INTO A ZOMBIE???"
    g "Calm down, we can fix that together on my answer sheet!"
    
    show Pharma relieved
    
    return

label fr_Pharm_ch_Form2:

    if not (chMenu1 and chMenu2 and chMenu3):
        sv "Menu"
    $shuffle_menu()
    menu:
        "Que veux-tu réparer?"
        "Problèmes avec la langue!" if not chMenu1:
            $chMenu1 = True
            
            g "Un problème avec la langue?"
            p "Absolument."
            g "Tu est certain? On a tout écrit en français, et on a bien épellé les mots de nos recherches."
            show Pharma happy
            p "Non, non, non! On ne doit pas traduire les opérateurs booléens."
            p "{=bool}ET{/=bool} devrait être {=bool}AND{/=bool}. {=bool}OU{/=bool} devrait être {=bool}OR{/=bool}."
            g "Mais on est tous des francophones ici! Et c'est ce qui est écrit sur le formulaire pour nous aider à construire notre expression de recherche!"
            show Pharma afraid
            p "Ce n'est pas grave. La plupart des bases de données {i}y compris les bases de données francophones{/i} fonctionnent avec les opérateurs
                {=bool}AND{/=bool} et {=bool}OR{/=bool}."
            p "Le nombre d'exceptions est tellement minuscule que c'est mieux de s'habituer à utiliser les opérateurs booléens {=bool}AND{/=bool} et {=bool}OR{/=bool}."
            p "Mais ce n'est pas tout..."
            show Pharma terrified
            p "Il faut aussi tenir en compte...euh...j'oublie. J'OUBLIE!"
            "Maintenant qu'il le mentionne, je me souviens vaguement d'une explication de la bibliothécaire."
            
            call fr_langue from _call_fr_langue_1
            call ms_ossuary from _call_ms_ossuary_15
            call sc_pharm from _call_sc_pharm_4
            
            show Pharma relieved
            g "Bon! On remplis un nouveau formulaire?"
            p "Corrige tes opérateurs booléens."
            show Pharma afraid
            p "On va s'essayer avec les mots clés en anglais parce que j'ai trop peur de constater que mon vocabulaire a diminué."
            
            if chMenu2 and chMenu3:
                g "D'accord, ça fait du sens. Et je pense qu'on a enfin terminé!."
                show Pharma relieved
            elif chMenu2 or chMenu3:
                g "Je ne veux pas être obligé de refaire 100 fois le travail."
                g "Quel est le dernier problème avec le formulaire?"
            else:
                g "Bon, quoi d'autre faut-il changer avec le formulaire?"

            show Pharma relieved
            jump fr_Pharm_ch_Form2
       
        "Absence de parenthèses!" if not chMenu2:
            $chMenu2 = True
            
            g "Des parenthèses? On va ajouter des parenthèses à l'expression de recherche booléenne?"
            show Pharma happy
            p "Oui!"
            g "Où? Comment? Pourquoi?"
            p "JE SAIS! JE SAIS L'EXPLICATION! C'est comme pour l'ordre des opérateurs en mathématique."
            p "Pour ne pas mélanger l'ordinateur, il faut lui dire quoi faire en premier en mettant les parenthèses au bon endroit."
            if not chMenu1:
                "On doit chercher des synonymes avec {=bool}OU{/=bool} avant d'ajouter des mots avec {=bool}ET{/=bool}."
            else:
                "On doit chercher des synonymes avec {=bool}OR{/=bool} avant d'ajouter des mots avec {=bool}AND{/=bool}."
            g "Alors je mets des parenthèses pour entourer..."
            show Pharma afraid
            p "Tous les sports, toutes les couleurs, tout le linge."
            p "Si plusieurs mots sont utilisés pour un même concept, le concept se fait entourer de parenthèses, 
               pour qu'on sache que c'est un même grand concept peu importe le nombre de mots utilisés pour l'exprimer."
            show Pharma happy
            g "Wow! Je pense que je comprends!"
            
            sv "Menu"
            $unshuffle_menu()
            menu:
                "J'ai réellement compris l'utilisation de parenthèses dans la recherche booléenne?"
                "Oui":
                    pass
                "Non":
                    g "...mais je ne comprends pas à 100\%"
                    show Pharma afraid
                    p "C'est correct! Je peux t'expliqer d'une autre façon!"
                    g "Ta mémoire semble vraiment intacte, c'est un bon signe!"
                    show Pharma relieved
                    
                    if not chMenu1:
                        p "Si je vais à une animalerie et j'achète un {=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word} {=bool}ET{/=bool} {=word}laisse{/=word}"
                        p "Avec quoi je vais sortir de l'animalerie?"
                        sv "Gabriel ne connaît pas la réponse. Cliquer deux fois pour continuer."
                        g "???"
                        show Pharma afraid
                        sv "Mode voix pharmacien. Chien OU ouvre parenthese chat ET laisse ferme parenthese."
                        p "{=word}chien{/=word} {=bool}OU{/=bool} ({=word}chat{/=word} {=bool}ET{/=bool} {=word}laisse{/=word})"
                        p "Je vais avoir un {=word}chien{/=word}. Ou bien je vais avoir un {=word}chat{/=word} et une {=word}laisse{/=word}?"
                        sv "Mode voix pharmacien. Ouvre parenthèse chien OU chat ferme parenthèse. Et laisse."
                        p "({=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word}) {=bool}ET{/=bool} {=word}laisse{/=word}"
                        p "Je vais avoir un {=word}chien{/=word} ou un {=word}chat{/=word}. Et je vais toujours sortir de l'animalerie avec une {=word}laisse{/=word}!"
                        sv "Un moment de silence. Cliquez deux fois pour continuer."
                        g "..."
                        show Pharma terrified
                        p "Tu as l'air encore plus mélangé!"
                        g "Oui. Désolé!"
                        p "La règle est simple. Mets des parenthèses pour entourer tous les synonymes d'un concept."
                        p "Si tu as des {=bool}OU{/=bool}, tu dois entourer tous les mots reliés par des {=bool}OU{/=bool} par des parenthèses."
                        sv "Mode voix pharmacien. Ouvre parenthèse chien OU chat ferme parenthèse ET laisse."
                        p "({=word}chien{/=word} {=bool}OU{/=bool} {=word}chat{/=word}) {=bool}ET{/=bool} {=word}laisse{/=word}"
                        sv "Mode voix pharmacien. Ouvre parenthèse école OU université ferme parenthèese. ET ouvre parenthèse réussite OU succèes ferme parenthèse."
                        p "({=word}ecole{/=word} {=bool}OU{/=bool} {=word}université{/=word}) {=bool}ET{/=bool} ({=word}réussite{/=word} {=bool}OU{/=bool} {=word}succès{/=word})"
                        g "Je pense que j'ai compris! Merci!"
                    else:
                        p "Si je vais à une animalerie et j'achète un {=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word} {=bool}AND{/=bool} {=word}laisse{/=word}"
                        p "Avec quoi je vais sortir de l'animalerie?"
                        sv "Gabriel ne connaît pas la réponse. Cliquer deux fois pour continuer."
                        g "???"
                        show Pharma afraid
                        sv "Mode voix pharmacien. Chien OR ouvre parenthese chat AND laisse ferme parenthese... Je vais avoir un chien. Ou bien je vais avoir unc hat et une laisse?"
                        p "{=word}chien{/=word} {=bool}OR{/=bool} ({=word}chat{/=word} {=bool}AND{/=bool} {=word}laisse{/=word})... Je vais avoir un {=word}chien{/=word}. Ou bien je vais avoir un {=word}chat{/=word} et une {=word}laisse{/=word}?"
                        sv "Mode voix pharmacien. Ouvre parenthèse chien OR chat ferme parenthèse. AND laisse... Je vais avoir un chien ou un chat. Et je vais toujours sortir de l'animalerie avec une laisse?"
                        p "({=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word}) {=bool}AND{/=bool} {=word}laisse{/=word}... Je vais avoir un {=word}chien{/=word} ou un {=word}chat{/=word}. Et je vais toujours sortir de l'animalerie avec une {=word}laisse{/=word}!"
                        sv "Un moment de silence. Cliquez deux fois pour continuer."
                        g "..."
                        show Pharma terrified
                        p "Tu as l'air encore plus mélangé!"
                        p "Oui. Désolé!"
                        p "La règle est simple. Mets des parenthèses pour entourer tous les synonymes d'un concept."
                        p "Si tu as des {=bool}OR{/=bool}, tu dois entourer tous les mots reliés par des {=bool}OR{/=bool} par des parenthèses."
                        sv "Mode voix pharmacien. Ouvre parenthèse chien OU chat ferme parenthèse ET laisse."
                        p "({=word}chien{/=word} {=bool}OR{/=bool} {=word}chat{/=word}) {=bool}AND{/=bool} {=word}laisse{/=word}"
                        sv "Mode voix Pharmacien. Ouvre parenthèse école OU université ferme parenthèese. ET ouvre parenthèse réussite OU succèes ferme parenthèse."
                        p "({=word}ecole{/=word} {=bool}OR{/=bool} {=word}université{/=word}) {=bool}AND{/=bool} ({=word}réussite{/=word} {=bool}OR{/=bool} {=word}succès{/=word} {=bool}OR{/=bool} {=word}success{/=word})"
                        g "Je pense que j'ai compris! Merci!"

            if chMenu1 and chMenu3:
                g "Bon, je vais corriger mon formulaire!"
            else:
                g "Avant de corriger le formulaire, j'aimerais en savoir plus à propos des autres 'problèmes' que tu crois avoir décelés."
                
            jump fr_Pharm_ch_Form2
        
        "Nom?" if not chMenu3:
            $chMenu3 = True
            
            show Pharma afraid
            p "Tu as oublié de t'identifier sur le formulaire."
            g "Mais je fais le corrigé?!"
            show Pharma terrified
            p "Oh non, tu as raison, TU AS RAISON!"
            
            jump fr_Pharm_ch_Form2
        
    "Le pharmacien a réparé son formulaire puis on a comparé avec mon corrigé, qui comprenait maintenant l'expression de recherche booléenne suivante:"
    sv "Mode voix narration. Ouvre parenthèse badminton OR pickleball OR tennis OR ping-pong ferme parenthèse. AND ouvre parenthèse lunette OR glasses ferme parenthèse.
        AND ouvre parenthèse casquette OR baseball cap ferme parenthèse. AND ouvre parenthèse bleu OR blue ferme parenthèse."
    "({=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} 
     {=word}ping-pong{/=word}) {=bool}AND{/=bool} ({=word}lunettes{/=word} {=bool}OR{/=bool} {=word}glasses{/=word}) {=bool}AND{/=bool} ({=word}casquette{/=word} {=bool}OR{/=bool} {=word}baseball cap{/=word}) {=bool}AND{/=bool} ({=word}bleu{/=word} {=bool}OR{/=bool} {=word}blue{/=word})"
    show Pharma happy
    p "SUPER! C'EST EXACTEMENT COMME MA PROPRE RÉPONSE!"
    show Pharma relieved
    p "On l'a prouvé! Je ne suis pas en train de devenir un zombie!"
    "Je ne vais certainement pas le décourager..."
        
    return
    

label en_Pharm_ch_Form2:

    if not (chMenu1 and chMenu2 and chMenu3):
        sv "Menu"
    $shuffle_menu()
    menu:
        "What do you want to fix?"
        "Capitals!" if not chMenu1:
            $chMenu1 = True
            
            g "What's wrong with my capitals?"
            show Pharma afraid
            p "Actually, nothing's wrong! But I'm not going insane! Probably!"
            sv "A silent beat. Click twice to continue."
            g "..."
            show Pharma terrified
            p "I just want to make sure that my explanation about why we capitalize {=bool}AND{/=bool} and {=bool}OR{/=bool} makes sense."
            g "Um, I already know this, but go ahead. Why do we capitalize '{=bool}And{/=bool}' and '{=bool}Or{/=bool}'?"
            p "So that the computer doesn't search for the {i}words{/i} '{=bool}or{/=bool}' and '{=bool}and{/=bool}'!"
            g "Yep, that makes sense! The librarian told us in class. We're using the boolean operators {=bool}AND{/=bool} and {=bool}OR{/=bool}. 
               They're not the {i}words{/i} 'and' and 'or', they're operators. Just like in math, where we have '+' and '-'."
            show Pharma relieved
            

            if chMenu2 and chMenu3:
                g "So we're done?"
            elif chMenu2 or chMenu3:
                g "So that was easy! What's left on the list now?"
            else:
                g "So is anything actually wrong with the form? What's next?"

            show Pharma happy
            jump en_Pharm_ch_Form2
       
        "Brackets!" if not chMenu2:
            $chMenu2 = True
            
            g "Brackets? You want me to add brackets to my boolean search expression?"
            show Pharma happy
            p "Yes!"
            g "Where? How? Why?"
            p "I KNOW! I KNOW THE EXPLANATION! It's exactly the same as the priority of operations in math."
            p "So we don't confuse the computer, we have to tell it what operation to do first by putting brackets — parentheses actually — in the right spots."
            p "We have to search synonyms with {=bool}OR{/=bool} before adding concepts with {=bool}AND{/=bool}."
            g "So we have to put parentheses around..."
            show Pharma afraid
            p "All the sports. And if we had more than one, the colors, the accessories, and the facial distinctions."
            p "If more than one word is used to express it, every idea gets tenderly embraced by parentheses, so that we know 
               that all the different words are part of one big idea."
            g "Wow, that makes so much sense!"
            show Pharma happy
            
            sv "Menu"
            $unshuffle_menu()
            menu:
                "I understand the use of parentheses in boolean searches?"
                "Yep!":
                    pass
                "Nope!":
                    g "...but I don't understand 100\%."
                    show Pharma afraid
                    p "That's fine! I can explain it some other way!"
                    g "That's actually a good sign that your brain is working okay!"
                    show Pharma relieved

                    p "If I run out to my local animal shelter and buy a {=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word} {=bool}AND{/=bool} {=word}collar{/=word}."
                    p "What will I have with me when I come out of the animal shelter?"
                    sv "Gabriel doesn't know the answer. Click twice to continue."
                    g "???"
                    show Pharma afraid
                    sv "Self-voiced Pharmacist. Dog OR open parentheses cat AND collar close parentheses. I'll have a {=word}dog{/=word}. Or the other alternative is that I'll have a {=word}cat{/=word} and a {=word}collar{/=word}?"
                    p "{=word}dog{/=word} {=bool}OR{/=bool} ({=word}cat{/=word} {=bool}AND{/=bool} {=word}collar{/=word})... I'll have a {=word}dog{/=word}. Or the other alternative is that I'll have a {=word}cat{/=word} and a {=word}collar{/=word}?"
                    sv "Self-voiced Pharmacist. Open parentheses Dog OR cat close parentheses AND collar. I'll have a {=word}dog{/=word} or a {=word}cat{/=word}. And I'll always come out of the shelter with a {=word}collar{/=word} for it!"
                    p "({=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word}) {=bool}AND{/=bool} {=word}collar{/=word}... I'll have a {=word}dog{/=word} or a {=word}cat{/=word}. And I'll always come out of the shelter with a {=word}collar{/=word} for it!"
                    sv "A silent beat. Click twice to continue."
                    p "..."
                    show Pharma terrified
                    p "Oh no, you look so confused!"
                    g "Yes. Sorry!"
                    p "It's simple. Put parentheses to bracket all synonyms of a concept."
                    p "If you have any {=bool}ORs{/=bool}, you should surround all words linked by {=bool}ORs{/=bool} with parentheses."
                    sv "Self-voiced Pharmacist. Open parentheses dog OR cat close parentheses AND collar."
                    p "({=word}dog{/=word} {=bool}OR{/=bool} {=word}cat{/=word}) {=bool}AND{/=bool} {=word}collar{/=word}"
                    sv "Self-voiced Pharmacist. Open parentheses school OR university close parentheses AND open parentheses success OR achievement OR accomplishment close parentheses."
                    p "(school {=bool}OR{/=bool} university) {=bool}AND{/=bool} (success {=bool}OR{/=bool} achievement {=bool}OR{/=bool} accomplishment)"
                    g "I think I get it now! Thanks!"
                    show Pharma happy

            if chMenu1 and chMenu3:
                g "Alright, I'm going to fix the answer key for good!"
            else:
                g "Before we fix the form, please tell me about the other problems you've identified."
                
            jump en_Pharm_ch_Form2
        
        "Name?" if not chMenu3:
            $chMenu3 = True
            
            show Pharma afraid
            p "You forgot to put your name on the form."
            g "But it's supposed to be an answer key?!"
            show Pharma terrified
            p "Oh no, you're right, YOU'RE RIGHT!"
            
            jump en_Pharm_ch_Form2
        
    "The pharmacist quickly fixes his form. We compare it with the answer sheet which now contains the following boolean search expression:"
    sv "Self-voiced narration. Open parentheses badminton OR pickeball OR tennis OR ping-pong close parentheses. AND glasses AND goatee AND blue."
    "({=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} 
     {=word}ping-pong{/=word}) {=bool}AND{/=bool} {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word} {=bool}AND{/=bool} {=word}blue{/=word}"
    show Pharma happy
    p "AMAZING! WE HAVE THE EXACT SAME ANSWERS!"
    show Pharma relieved
    p "We've proved it! I'm not becoming a zombie for sure!"
    "I certainly don't want to discourage him..."
        
    return

label fr_Pharm_safe:
    $safeIC = 2
    $safeCIB = 3
    $safeWord = "Pharmacie"
    g "Donc, je cherche-"
    show Pharma happy
    p "Laisse moi te remercier d'avoir DÉFINITIVEMENT prouvé que je ne suis pas un zombie."
    p "Tiens, lis ça pour moi, c'est le code, j'ai perdu mes lunettes!"
    
    "Selon la note, le mot de passe est 'Pharmacie' et il suffit d'entrer un code de 6 chiffres."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    "..."
    g "'Pharmacie'? Mais il faut 6 chiffres, pas 9 lettres?"
    show Pharma afraid
    p "C'est parce que...euh.."
    show Pharma terrified
    p "COMMENT J'AI RÉUSSI À OUBLIER ÇA? Mais c'est définitivement le code! Je ne comprends rien!?"
    
    sv "J'examine le mécanisme. C'est un clavier téléphonique. Les numéros sont associés avec des lettres."
    window hide
    scene bg safe with dissolve
    $renpy.pause(2.0)
    window show
    
    g "La petite étoile qui se trouve à côté de la position '0' est une astérix. Ça me rappèle des souvenirs de la visite de la Bibliothécaire!"
    
    call fr_troncature from _call_fr_troncature_1
    call ms_ossuary from _call_ms_ossuary_16
    call sc_pharm from _call_sc_pharm_5
    "Je sais comment procéder! Je ne dois pas oublier que le mot de passe est 'Pharmacie'."
    sv "Utiliser la flêche vers le haut et la flêche vers le bas pour naviguer sur les différents numéros du clavier électronique dans le prochain écran."
    sv "Après deux entrées incorrectes, 4 codes — 1 des codes est correct — pourront être sélectionné."
    call fr_load_safe from _call_fr_load_safe_2 #in pthJoint
    
    "Le coffre-fort est remplit de médicaments."
    show Pharma happy
    p "Tiens, ça pourrait t'être utile si tu te blesse."
    "Je ne discute pas et je ramasse quelques poignées de différentes pilules."
    show Pharma terrified
    p "Je ne peux pas croire que j'ai oublié le code. MON CERVEAU!"
    g "Comment souvent tu ouvres le coffre-fort?"
    show Pharma relieved
    p "Ah! C'est probablement la première fois!"
    p "Peut-être je suis correct? Peut-on faire un dernier test?"
    g "D'ACCORD, mais après, j'ai définitivement besoin que tu me donnes quelque chose.."
        
    return

label en_Pharm_safe:
    $safeIC = 2
    $safeCIB = 3
    $safeWord = "Pharmacy"
    g "So, I'm looking f-"
    show Pharma happy
    p "Thanks again for DEFINITELY proving that I'm not a zombie."
    p "Here, read this for me please, it's a code. I lost my glasses!"
    
    "The note says that the password is 'Pharmacy' and to enter a 6 digit code."
    sv "A silent beat. Click twice to continue."
    "..."
    g "'Pharmacy'? But you need 6 numbers, not 8 letters?"
    show Pharma afraid
    p "That's because..er..."
    show Pharma terrified
    p "I'VE COMPLETELY FORGOTTEN WHAT TO DO? But that's definitely the right code! I don't understand anything anymore!"
    
    sv "I examine the mechanism. It's a keypad. The numbers are associated with letters."
    window hide
    scene bg safe with dissolve
    $renpy.pause(2.0)
    window show
    
    call sc_pharm from _call_sc_pharm_6
    
    g "The little star besides the '0' is an asterix. It reminds me of the librarian's visit!"
    
    call en_troncature from _call_en_troncature_1
    call ms_ossuary from _call_ms_ossuary_17
    call sc_pharm from _call_sc_pharm_7
    "I know what to do! I have to remember that the password is 'Pharmacy'."
    
    sv "You will have to enter a code on the screen. Use the up or down arrow on the keyboard to select a different number on the keypad."
    sv "After two wrong attempts, a list of 4 possible codes will appear and can be selected on the screen. One of the codes will be the correct code."
    call fr_load_safe from _call_fr_load_safe_3 #in pthJoint
    
    "The locker is filled with medicine."
    show Pharma happy
    p "Here, these could be useful if you hurt yourself."
    "I don't argue and grab a few different kind of pills."
    show Pharma terrified
    p "I can't believe I forgot the code. MY BRAIN!"
    g "How often to you open the drug locker?"
    show Pharma relieved
    p "Ah! This is probably the first time!"
    p "Maybe I'm okay after all? Can we do one last test?"
    g "FINE, but I'm asking for something in return after.."
        
    return
    
label fr_Venn_Pharm:
    
    show Pharma happy
    p "On va faire une course. Premier à tout allumer dans ce petit jeu électronique gagne."
    "Facile, je vais m'assurer de perdre..."
    show Pharma afraid
    p "Si tu fais trop d'erreur, je ne peux pas considérer le test valide."
    "Zut..."
    
    call choixMenu from _call_choixMenu_32
    call cleanMadGab from _call_cleanMadGab_10
    
    $myList = (('{b}Pharmacie                         Médicament{/b}', 'Pharmacie','Médicament'))

    call fr_Venn_Setup from _call_fr_Venn_Setup_1
    
    show Venn0 at venTop
    show text "{=book}[entry1]{/=book}" at venWord
    "Allumer les cerc-"
    
    p "J'ai réussi! J'AI RÉUSSI! J'ai gagné!"
    call sc_pharm from _call_sc_pharm_8
    show Pharma happy
    p "Je ne deviens pas un zombie!"
    
    return
    
label en_Venn_Pharm:
    
    show Pharma happy
    p "Let's race. First one to light up all the lights in this little electronic game I have correctly wins."
    "Easy, I'm going to make sure that I lose..."
    show Pharma afraid
    p "If you make too many mistakes, the test won't be valid."
    "Argh..."
    
    call choixMenu from _call_choixMenu_33
    call cleanMadGab from _call_cleanMadGab_11
    
    $myList = (('{b}Pharmacy                           Medicine{/b}', 'Pharmacy','Medicine'))
    call en_Venn_Setup from _call_en_Venn_Setup_1
    
    show Venn0 at venTop
    show text "{=book}[entry1]{/=book}" at venWord
    with dissolve
    "Light up the circ-"
    
    p "I'm done! I DID IT! I won!"
    call sc_pharm from _call_sc_pharm_9
    show Pharma happy
    p "I'm not turning into a zombie!"
    
    return
    
label fr_Pharm_reanim:
    g "Maintenant qu'on sait que tu ne deviens pas un zombie..."
    p "Oui?"
    g "Est-ce que je pourrais avoir un défibrillateur cardiaque?"
    show Pharma afraid
    p "Tu ne vas pas m'attaquer avec parce que tu as l'impression que j'aurais dû gagner beaucoup plus rapidement?"
    g "Euh...non..."
    show Pharma happy
    p "On en vend, et on en a derrière le comptoir au cas où un client aurait un malaise."
    "Les rayons sont...plutôt vides. Le pharmacien fouille un peu derrière son comptoir."
    p "Et voilà!"
    g "Merci!!!"
    
    "C'est le temps de repartir, mais j'hésite à abandonner le pharmacien."
    "Si je l'invite, va-t-il continuer à me ralentir avec des tests? Mais tout seul, il va recommencer à penser qu'il devient un zombie?"
    
    return
    
label en_Pharm_reanim:
    g "Now that we know you're not becoming a zombie..."
    p "Yes?"
    g "Could I have a cardiac defibrillator?"
    show Pharma afraid
    p "You're not planning on attacking me with it because I should have won that game faster than I did?"
    g "Um...no..."
    show Pharma happy
    p "We sell some, and we also have some behind the counter in case something were to happen to a client."
    "The shelves are...pretty empty. The pharmacist looks behind his counter."
    p "There it is!"
    g "Thanks!!!"
    
    "It's time to go, but I hesitate to leave the pharmacist."
    "If I invite him along, will he keep slowing me down with more tests? But on his own, will he start thinking he's becoming a zombie again?"
    
    return
    
label fr_Pharm_invitation:
    $companion = True
    g "Je ne pense pas que tu devrais être laissé tout seul."
    show Pharma terrified
    p "Parce que tu pense que je suis un zombie après tout?"
    g "Non, non, ce n'est pas ça, j'aimerais bien ta compagnie."
    show Pharma happy
    p "Merci! Ça fait un bout de temps que je me cherche une excuse pour partir."
    show Pharma afraid
    p "J'ai déjà dû défendre la pharmacie contre plusieurs vols armés depuis le début des troubles."
    sv "Gabriel est étonné. Cliquer deux fois pour continuer."
    "!!!"
    show Pharma terrified
    p "Mais je ne pouvais pas risquer exposer le monde à un possible zombie."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    "..."
    "J'espère que j'ai pris la bonne décision!"
    show Pharma happy
    p "Juste une seconde, je vais nous ramasser des provisions..."
    
    if flag3 >= 4:
        "Le pharmacien a rit nerveusement et a ramassé des bandages miniatures."
    elif flag3 == 3:
       "Le pharmacien a rit nerveusement et ramassé des boîtes de bandages."
    elif flag3 == 2:
        "Le pharmacien a sourit doucement et ramassé de l'argent, des boîtes de bandages, et des trucs contre les allergies."
    elif flag3 == 1:
        "Le pharmacien a sourit et ramassé une trousse d'urgence."
    else:
        "Le pharmacien a sourit et ramassé une trousse d'urgence et des drogues mystérieuses."
        
    "On est parti trouver Évangeline."

    
    return
    
label en_Pharm_invitation:
    $companion = True
    g "I don't think you should be left alone."
    show Pharma terrified
    p "Because you think I'm a zombie after all?"
    g "No, no, that's not it, I enjoy your company."
    show Pharma happy
    p "Thanks! I've been looking for an excuse to leave for a while now."
    show Pharma afraid
    p "I've already had to deal with several hold ups since the beginning of the troubles."
    sv "Gabriel is surprised. Click twice to continue."
    "!!!"
    show Pharma terrified
    p "But I couldn't risk unleashing a potential zombie on the world."
    sv "A silent beat. Click twice to continue."
    "..."
    "I hope this is the right decision!"
    show Pharma happy
    p "Just a second, I'm going to grab some more useful stuff from behind the counter..."
    
    if flag3 >= 4:
        "The pharmacist laughs nervously and grabs some miniature bandages."
    elif flag3 == 3:
       "The pharmacist laughs nervously and grabs boxes of bandages."
    elif flag3 == 2:
        "The pharmacist smiles calmly and grabs money, boxes of bandages, and anti-allergy tablets."
    elif flag3 == 1:
        "The pharmacist smiles and grabs a first aid kit."
    else:
        "The pharmacist smiles and grabs a first aid kit and some mysterious medicines."
        
    "We leave to find Évangeline."

    
    return
    
label fr_Pharm_aurevoir:
    g "Bon, je vais repartir."
    show Pharma relieved
    p "...au revoir. Oui. C'est probablement mieux comme ça?"
    show Pharma terrified
    p "Je ne veux pas être un fardeau si je me trompe..."
    show Pharma happy
    p "Bonne chance à toi aussi! JE NE VAIS JAMAIS T'OUBLIER!"
    
    "Après avoir remercié une dernière fois le pharmacien, je suis parti retrouver Évangeline."
    return
    
label en_Pharm_aurevoir:
    g "Well, I've got to go."
    show Pharma relieved
    p "...goodbye. Yes. It's probably better to say goodbye?"
    show Pharma terrified
    p "I don't want to be a burden if I'm wrong..."
    show Pharma happy
    p "Good luck to you! I'LL NEVER FORGET YOU!"
    
    "After thanking the pharmacist, I leave to find Évangeline."
    return
