#These are the bones for the form used in all versions of Chapter 1
label fr_ch_Form:
    scene form with dissolve
    sv "Menu"
    $shuffle_menu()
    menu:
        "Comment remplir le formulaire si on doit choisir un seul sport préféré?"
        "Badminton {=bool}ET{/=bool} pickleball {=bool}ET{/=bool} tennis {=bool}ET{/=bool} ping-pong \ \ {=bool}OU{/=bool} \ \ lunettes {=bool}ET{/=bool} casquette \ \ {=bool}OU{/=bool} \ \ bleu" if not chMenu1:
        #Badminton ET pickleball ET tennis ET ping-pong \ \ OU \ \ lunettes ET casquette \ \ OU \ \ bleu
            $chMenu1 = True
            call victoryLost from _call_victoryLost_25
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos2
            show sport3 at formPos3
            show sport4 at formPos4
            show facial1 at formPos5
            show facial2 at formPos6
            show color1 at formPos9
            with dissolve
            
            sv "Un tableau apparaît à l'écran. Un sport différent se trouve sur chaque colonne de la première ligne. La deuxième ligne contient 'lunette' sur la première colonne et 'casquette' sur la deuxième colonne."
            sv "'Bleu' se trouve sur la troisième ligne, première colonne."
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Wow, tu n'es même pas proche. Je ne pense pas que tu as bien saisi la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}."
                r "Ou comment le formulaire fonctionne. Une colonne devrait contenir seulement une idée, avec les synonymes de l'idée sur chaque ligne."
                r "Comme c'est là, si un étudiant dans la résidence porte des {=word}lunettes{/=word} et une {=word}casquette{/=word}, tu reçois son numéro de chambre même s'il aime le vert
                    et n'est pas intéressé par les sports. Tu vas recevoir pleins de numéros, ça ne va pas t'avancer."
                r "Je vais prendre Marthe comme exemple, elle porte souvent une {=word}casquette{/=word} et des {=word}lunettes{/=word}."
                r "Je commence par examiner chaque partie de ton expression de recherche. {=word}Badminton{/=word} {=bool}ET{/=bool} {=word}pickleball{/=word} {=bool}ET{/=bool} {=word}tennis{/=word} {=bool}ET{/=bool} {=word}ping-pong{/=word}?
                    Ça n'intéresse pas du tout Marthe. Ou bien {=word}lunettes{/=word} {=bool}ET{/=bool} {=word}casquette{/=word}? Oui, ça décrit Marthe. Ou encore {=word}bleu{/=word}? Nope."
                r "L'opérateur {=bool}OU{/=bool} veut dire que n'importe laquelle des options me font 'plaisir', alors je peux me contenter de la couleur ou bien des
                    vêtements pour donner un numéro de chambre. Tu vas avoir pleins de numéros!"
                r "Pour les sports, j'aurais besoin d'une personne qui a déclaré que ses sports préférés sont le {=word}badminton{/=word}, le {=word}pickleball{/=word}, le {=word}tennis{/=word}
                    ou le {=word}ping-pong{/=word}."
                r "Donc, ca ne fonctionne vraiment pas. Je vais te demander de remplir un autre formulaire."
                
            elif chosenPath == "Pharmacy":
                p "C'est rassurant! Je peux encore détecter que tu n'as pas bien saisi la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}."
                p "Ou comment le formulaire fonctionne — une colonne devrait contenir une seule idée, avec les synonymes de l'idée sur chaque ligne."
                p "Comme c'est là, si un client porte des {=word}lunettes{/=word} et une {=word}casquette{/=word}, tu le trouve même s'il aime le vert
                    et n'est pas intéressé par les sports. Tu vas trouver beaucoup de clients, ça va être trop long pour repérer mon frère."
                p "Je vais prendre Marthe comme exemple, elle porte souvent une {=word}casquette{/=word} et des {=word}lunettes{/=word}."
                p "Je commence par examiner chaque partie de ton expression de recherche. {=word}Badminton{/=word} {=bool}ET{/=bool} {=word}pickleball{/=word} {=bool}ET{/=bool} {=word}tennis{/=word} {=bool}ET{/=bool} {=word}ping-pong{/=word}?
                    Ça n'intéresse pas du tout Marthe. Ou bien {=word}lunettes{/=word} {=bool}ET{/=bool} {=word}casquette{/=word}? Oui, ça décrit Marthe. Ou encore {=word}bleu{/=word}? Non."
                p "L'opérateur {=bool}OU{/=bool} veut dire que n'importe laquelle des options me font 'plaisir', alors je peux me contenter de la couleur ou bien des
                    vêtements pour trouver un client. Tu vas trouver pleins de personnes!"
                p "Pour les sports, ça nous forcerait à trouver une personne qui a déclaré que ses sports préférés sont à la fois le {=word}badminton{/=word}, le {=word}pickleball{/=word}, le {=word}tennis{/=word}
                    et le {=word}ping-pong{/=word}."
                p "Donc, ca ne fonctionne vraiment pas. Je vais te demander de remplir un autre formulaire."
                p "Construis un bon corrigé pour moi!"
            
            else:
                b "Oh non...non... je n'ai pas dû bien expliquer la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}."
                b "Et le formulaire — une colonne devrait contenir une seule idée, avec différents synonymes sur chaque ligne."
                b "Comme c'est là, si un criminel dans la base de données porte des {=word}lunettes{/=word} et une {=word}casquette{/=word}, on va trouver son nom même s'il aime le vert
                    et n'est pas intéressé par les sports. Tu vas recevoir pleins de noms de criminels potentiels, ça ne va pas t'avancer."
                b "Je vais prendre Arsène comme exemple, il porte souvent une {=word}casquette{/=word} et des {=word}lunettes{/=word}."
                b "Je commence par examiner chaque partie de ton expression de recherche. {=word}badminton{/=word} {=bool}ET{/=bool} {=word}pickleball{/=word} {=bool}ET{/=bool} {=word}tennis{/=word} {=bool}ET{/=bool} {=word}ping-pong{/=word}?
                    Ça n'intéresse pas du tout Arsène. Ou bien {=word}lunettes{/=word} {=bool}ET{/=bool} {=word}casquette{/=word}? Oui, ça décrit Arsène. Ou encore {=word}bleu{/=word}? Non."
                b "L'opérateur {=bool}OU{/=bool} veut dire que n'importe laquelle des options peuvent suffir, alors la base de données peut se concentrer seulement sur la couleur ou bien des
                    vêtements pour identifier les suspects. Tu vas avoir pleins de noms!"
                b "Pour les sports, on veut une personne qui a déclaré que ses sports préférés sont un des sports suivants: {=word}badminton{/=word}, {=word}pickleball{/=word}, {=word}tennis{/=word}
                    ou {=word}ping-pong{/=word}."
                b "Donc, ca ne fonctionne vraiment pas. Remplis un autre formulaire, je sais que tu es capable!"
            
            jump fr_ch_Form
            
        "Badminton {=bool}ET{/=bool} pickleball {=bool}ET{/=bool} tennis {=bool}ET{/=bool} ping-pong \ \ {=bool}OU{/=bool} \ \ lunettes {=bool}ET{/=bool} casquette {=bool}ET{/=bool} bleu" if not chMenu2:
        #Badminton ET pickleball ET tennis ET ping-pong \ \ OU \ \ lunettes ET casquette ET bleu
            $chMenu2 = True
            call victoryLost from _call_victoryLost_26
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos2
            show sport3 at formPos3
            show sport4 at formPos4
            show facial1 at formPos5
            show facial2 at formPos6
            show color1 at formPos7
            with dissolve
            
            
            sv "Un tableau apparaît à l'écran. Un sport différent se trouve sur chaque colonne de la première ligne."
            sv "La deuxième ligne contient 'lunette' sur la première colonne, 'casquette' sur la deuxième colonne, et 'bleu' sur la troisième colonne."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Wow, quelle réponse terrible! Je ne pense pas que tu as bien saisi la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}."
                r "Et il ne faut pas oublier que dans le formulaire, chaque colonne devrait contenir seulement une idée. Avec les différentes lignes réservées pour les synonymes de cette idée."
                r "Comme tu as fait ça, je peux évaluer ton expression de recherche en deux temps.
                    On va prendre Peter comme exemple. Il a des {=word}lunettes{/=word}, porte souvent une {=word}casquette{/=word}, conduit une belle moto {=word}bleu{/=word}."
                r "Dans la première partie, tu demandes pour {=word}Badminton{/=word} {=bool}ET{/=bool} {=word}pickleball{/=word} {=bool}ET{/=bool} {=word}tennis{/=word} {=bool}ET{/=bool} {=word}ping-pong{/=word}."
                r "À la résidence, PERSONNE n'a choisi QUATRE sports préférés, alors cette première partie ne me sort aucun nom."
                r "{=bool}OU{/=bool}, tu me donnes un deuxième choix, alors j'examine la deuxième partie de l'expression."
                r "Tu veux {=word}lunettes{/=word} {=bool}ET{/=bool} {=word}casquette{/=word} {=bool}ET{/=bool} {=word}bleu{/=word}?"
                r "Ça décrit plusieurs personnes dans la résidence dont Peter."
                r "Ça ne me tente pas de fouiller très fort dans mon système, alors tu vas devoir être plus précis en précisant le sport préféré de Charlie."
                r "Tiens, j'ai un autre formulaire."
                
            elif chosenPath == "Pharmacy":
                p "Mon cerveau fonctionne encore assez pour voir que clairement, tu n'es pas sérieux."
                p "Ton formulaire me fait rire — chaque colonne devrait contenir seulement une idée, avec les différents synonymes d'une même idée sur chaque ligne de la colonne."
                p "Comme tu as fait ça, je peux évaluer ton expression de recherche en deux temps."
                p "On va prendre Peter comme exemple. Il a des {=word}lunettes{/=word}, porte souvent une {=word}casquette{/=word}, conduit une belle moto {=word}bleu{/=word}."
                p "Dans la première partie, tu demandes pour {=word}badminton{/=word} {=bool}ET{/=bool} {=word}pickleball{/=word} {=bool}ET{/=bool} {=word}tennis{/=word} {=bool}ET{/=bool} {=word}ping-pong{/=word}."
                p "PERSONNE n'a choisi QUATRE sports préférés, alors cette première partie ne sortirait aucun nom."
                p "{=bool}OU{/=bool}, tu me donnes un deuxième choix, alors j'examine la deuxième partie de l'expression."
                p "Tu veux {=word}lunettes{/=word} {=bool}ET{/=bool} {=word}casquette{/=word} {=bool}ET{/=bool} {=word}bleu{/=word}?"
                p "Ça décrit plusieurs personnes y comprit mon frère."
                p "Tu es drôle, mais la situation est grave!"
                p "Tiens, j'ai un autre formulaire."
                
            else:
                b "Non, non, ce n'est pas du tout la bonne réponse. Il faut saisir la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}."
                b "Chaque idée devrait être dans sa propre colonne. Et pour chaque idée, les lignes contiennent les différents synonymes de l'idée."
                b "Comme tu as fait ça, je peux évaluer ton expression de recherche en deux temps.
                    On va prendre Jack comme exemple. Il a des {=word}lunettes{/=word}, porte souvent une {=word}casquette{/=word}, conduit une belle moto {=word}bleu{/=word}."
                b "Dans la première partie, tu demandes pour {=word}badminton{/=word} {=bool}ET{/=bool} {=word}pickleball{/=word} {=bool}ET{/=bool} {=word}tennis{/=word} {=bool}ET{/=bool} {=word}ping-pong{/=word}."
                b "Dans la base de données, PERSONNE n'a identifié quatre sports préférés, alors cette première partie ne me trouve aucun nom."
                b "{=bool}OU{/=bool}, tu me donnes un deuxième choix, alors j'examine la deuxième partie de l'expression."
                b "Tu veux {=word}lunettes{/=word} {=bool}ET{/=bool} {=word}casquette{/=word} {=bool}ET{/=bool} {=word}bleu{/=word}?"
                b "Ça décrit plusieurs personnes dont notre suspect. Il faut un sport préféré pour réduire le nombre de possibilités."
                b "Tu peux faire beaucoup mieux. Je crois en toi! La classe crois en toi!"
                b "Tiens, j'ai un autre formulaire."
            
            jump fr_ch_Form
            
        "Badminton {=bool}OU{/=bool} pickleball {=bool}OU{/=bool} tennis {=bool}OU{/=bool} ping-pong \ \ {=bool}ET{/=bool} \ \ lunettes {=bool}OU{/=bool} casquette {=bool}OU{/=bool} bleu" if not chMenu3:
        #Badminton OU pickleball OU tennis OU ping-pong \ \ ET \ \ lunettes OU casquette OU bleu    
            $chMenu3 = True
            call victoryLost from _call_victoryLost_27
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos5
            show sport3 at formPos9
            show sport4 at formPos13
            show facial1 at formPos2
            show facial2 at formPos6
            show color1 at formPos10
            with dissolve
            
            sv "Un tableau apparaît à l'écran. La première colonne contient un sport différent sur chaque ligne."
            sv "La deuxième colonne contient 'lunette' sur la première ligne, 'casquette' sur la deuxième ligne, et 'bleu' sur la troisième ligne."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Wow, ta réponse n'est pas très bonne! Je ne pense pas que tu as bien saisi la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}."
                r "Ton formulaire n'est pas très beau — chaque concept devrait être dans sa propre colonne, les synonymes sur les différentes lignes d'un même concept."
                r "Dans la première partie de ton expression de recherche, tout va bien."
                r "Tu veux quelqu'un qui a comme sport préféré {=word}Badminton{/=word} {=bool}OU{/=bool} {=word}pickleball{/=word} {=bool}OU{/=bool} {=word}tennis{/=word} {=bool}OU{/=bool} {=word}ping-pong{/=word}?"
                r "C'est parfait, le sport préféré de Charlie se trouve définitivement parmis ces quatre options."
                r "Par contre, tu ne fais plus de sens dans la deuxième partie de ton expression de recherche."
                r "En plus du sport préféré de Charlie, tu veux {=word}lunettes{/=word} {=bool}OU{/=bool} {=word}casquette{/=word} {=bool}OU{/=bool} {=word}bleu{/=word}?"
                r "Franchement! Ça va décrire beaucoup trop de personnes! Si quelqu'un a comme sport préféré le {=word}badminton{/=word} et aime le {=word}bleu{/=word},
                    il va être trouvé par ton expression de recherche."
                r "Quelqu'un qui porte des {=word}lunettes{/=word} et joue au {=word}tennis{/=word}? On va également le repérer."
                r "On va repérer n'importe quelle personne qui adore le {=word}tennis{/=word}, en autant que cette personne porte des {=word}lunettes{/=word} ou a une {=word}casquette{/=word} ou aime le {=word}bleu{/=word}."
                r "Et c'est pareil pour les trois autres sports."
                r "Tu dois être plus exigent, et pour être plus exigent, on utilise le {=bool}ET{/=bool}..."
                r "Je me sens généreux, alors je vais recycler ton formulaire pour faire un papier mâché de notre recteur."
                r "Tu peux recommencer avec un autre formulaire."
            
            elif chosenPath == "Pharmacy":
                p "Wow, ta réponse n'est pas très bonne! Tu es gentil, tu fais un test pour voir comment je vais réagir?"
                p "Tu fais semblant d'avoir oublié que chaque concept va dans sa propre colonne, et les synonymes d'un concept vont sous le concept sur les différentes lignes?"
                p "Je vais t'expliquer mon raisonnement, et tu me diras si je suis proche!"
                p "Dans la première partie de ton expression de recherche, tout va bien."
                p "Tu veux quelqu'un qui a comme sport préféré {=word}badminton{/=word} {=bool}OU{/=bool} {=word}pickleball{/=word} {=bool}OU{/=bool} {=word}tennis{/=word} {=bool}OU{/=bool} {=word}ping-pong{/=word}?"
                p "C'est parfait, le sport préféré de mon frère se trouve définitivement parmis ces quatre options."
                p "Par contre, tu ne fais plus de sens dans la deuxième partie de ton expression de recherche."
                p "En plus du sport préféré de mon frère, tu veux {=word}lunettes{/=word} {=bool}OU{/=bool} {=word}casquette{/=word} {=bool}OU{/=bool} {=word}bleu{/=word}?"
                p "Ça va décrire beaucoup trop de personnes! Si quelqu'un a comme sport préféré le {=word}badminton{/=word} et aime le {=word}bleu{/=word},
                    il va être trouvé par ton expression de recherche."
                p "Quelqu'un qui porte des {=word}lunettes{/=word} et joue au {=word}tennis{/=word}? On va également le repérer."
                p "On va repérer n'importe qui adore le {=word}tennis{/=word}, en autant qu'il porte de {=word}lunettes{/=word} ou bien qu'il a une {=word}casquette{/=word} ou qu'il aime le {=word}bleu{/=word}."
                p "Et c'est pareil pour les trois autres sports."
                p "On dois être plus exigent, et pour être plus exigent, on utilise le {=bool}ET{/=bool}..."
                p "Alors? Je suis proche? DIS-MOI QUE JE SUIS PROCHE!!!"
                "Je n'ai pas eu le temps de rien dire qu'il m'a glissé un autre formulaire entre les mains!"
            
            else:
                b "Aw, je suis désolée. Il manque encore des nuances dans la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}."
                b "Il ne faut pas oublier que dans le formulaire, chaque concept va dans son propre colonne. Et les lignes sous un concept sont réservé pour les synonymes du concept."
                b "Dans la première partie de ton expression de recherche, tout va bien."
                b "Tu veux quelqu'un qui a comme sport préféré {=word}badminton{/=word} {=bool}OU{/=bool} {=word}pickleball{/=word} {=bool}OU{/=bool} {=word}tennis{/=word} {=bool}OU{/=bool} {=word}ping-pong{/=word}?"
                b "C'est parfait, le sport préféré de notre ignoble criminel se trouve définitivement parmis ces quatre options."
                b "Par contre, la deuxième partie de ton expression de recherche est problématique."
                b "En plus du sport préféré de Charlie, tu veux {=word}lunettes{/=word} {=bool}OU{/=bool} {=word}casquette{/=word} {=bool}OU{/=bool} {=word}bleu{/=word}?"
                b "Ça va décrire beaucoup trop de personnes! Si quelqu'un a comme sport préféré le {=word}badminton{/=word} et aime le {=word}bleu{/=word},
                    il va être trouvé par ton expression de recherche."
                b "Quelqu'un qui porte des {=word}lunettes{/=word} et joue au {=word}tennis{/=word}? On va également le repérer."
                b "On va repérer n'importe quel criminel qui adore le {=word}tennis{/=word}, en autant qu'il porte de {=word}lunettes{/=word} ou bien qu'il a une {=word}casquette{/=word} ou qu'il aime le {=word}bleu{/=word}."
                b "Et c'est pareil pour les trois autres sports."
                b "On doit être plus sévère, et pour être plus sévère, on utilise le {=bool}ET{/=bool}..."
                b "Je vais recycler ta réponse — c'est bon pour l'environnement — et te donner la chance de continuer avec un autre formulaire."
            
            jump fr_ch_Form
            
        "Badminton {=bool}OU{/=bool} pickleball {=bool}OU{/=bool} tennis {=bool}OU{/=bool} ping-pong \ \ {=bool}ET{/=bool} \ \ lunettes {=bool}OU{/=bool} casquette \ \ {=bool}ET{/=bool} \ \ bleu" if not chMenu4:
        #Badminton OU pickleball OU tennis OU ping-pong \ \ ET \ \ lunettes OU casquette \ \ ET \ \ bleu
            $chMenu4 = True
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos5
            show sport3 at formPos9
            show sport4 at formPos13
            show facial1 at formPos2
            show facial2 at formPos6
            show color1 at formPos3
            with dissolve
            
            sv "Un tableau apparaît à l'écran. La première colonne contient un sport différent sur chaque ligne."
            sv "La deuxième colonne contient 'lunette' sur la première ligne, et 'casquette' sur la deuxième ligne. La première ligne de la troisième colonne contient 'bleu'."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Hmmm, tu as presque la bonne réponse! Tu as peut-être bien saisi la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}?"
                r "La première partie de ton expression de recherche booléenne est parfaite."
                r "Tu veux {=word}badminton{/=word} {=bool}OU{/=bool} {=word}pickleball{/=word} {=bool}OU{/=bool} {=word}tennis{/=word} {=bool}OU{/=bool} {=word}ping-pong{/=word} comme sport préféré?"
                r "C'est parfait, une de ces quatre options comprend le sport préféré de Charlie."
                r "Et il aime définitivement le {=word}bleu{/=word}."
                r "Vraiment, la seule chose qui dérange un peu, c'est la partie centrale : {=word}lunettes{/=word} {=bool}OU{/=bool} {=word}casquette{/=word}?"
                r "J'ai déjà admiré Charlie de loin. Il porte toujours ses {=word}lunettes{/=word} et je ne l'ai jamais vu sans sa {=word}casquette{/=word}."
                r "Peut-être qu'il perd déjà ses cheveux?"
                r "En tout cas, tu as besoin de dire qu'il porte à la fois ses {=word}lunettes{/=word} et sa {=word}casquette{/=word}."
                r "Même si tu voulais dire qu'il porte seulement occasionnellement sa {=word}casquette{/=word}, ton expression serait incorrecte
                    parce qu'elle sous-entend qu'il pourrait porter une {=word}casquette{/=word} au lieu de ses {=word}lunettes{/=word}."
                r "Je vais donc faire une avion de papier avec ton formulaire."
                r "Tu peux remplir un autre formulaire."
                
            elif chosenPath == "Pharmacy":
                p "C'est tellement proche! Nos réponses sont presques identiques!"
                p "La première partie de ton expression de recherche booléenne est parfaite."
                p "Tu veux {=word}badminton{/=word} {=bool}OU{/=bool} {=word}pickleball{/=word} {=bool}OU{/=bool} {=word}tennis{/=word} {=bool}OU{/=bool} {=word}ping-pong{/=word} comme sport préféré?"
                p "C'est parfait, une de ces quatre options comprend le sport préféré de mon frère."
                p "Et il aime définitivement le {=word}bleu{/=word}."
                p "Vraiment, la seule chose qui dérange un peu, c'est la partie centrale : {=word}lunettes{/=word} {=bool}OU{/=bool} {=word}casquette{/=word}?"
                p "Mon frère porte toujours ses {=word}lunettes{/=word} et je ne l'ai jamais vu sans sa {=word}casquette{/=word}."
                p "Peut-être qu'il perd déjà ses cheveux?"
                p "En tout cas, tu as besoin de dire qu'il porte à la fois ses {=word}lunettes{/=word} et sa {=word}casquette{/=word}."
                p "Je vais être vraiment, VRAIMENT certain que mon sens de raisonnement est intact."
                r "Tu peux remplir un autre formulaire?"
                
            else:
                b "Bravo! Tu as presque la bonne réponse! Tu as peut-être bien saisi la différence entre {=bool}OU{/=bool} et {=bool}ET{/=bool}?"
                b "La première partie de ton expression de recherche booléenne est parfaite."
                b "Tu veux {=word}badminton{/=word} {=bool}OU{/=bool} {=word}pickleball{/=word} {=bool}OU{/=bool} {=word}tennis{/=word} {=bool}OU{/=bool} {=word}ping-pong{/=word} comme sport préféré?"
                b "C'est parfait, une de ces quatre options comprend le sport préféré du criminel."
                b "Et il aime définitivement le {=word}bleu{/=word}."
                b "Vraiment, la seule chose qui pourrait être améliorée, c'est la partie centrale : {=word}lunettes{/=word} {=bool}OU{/=bool} {=word}casquette{/=word}?"
                b "Selon les témoins, le criminel portait ses {=word}lunettes{/=word} et une {=word}casquette{/=word}."
                b "Peut-être qu'il perd déjà ses cheveux?"
                b "On va mettre cette réponse de côté, mais tu as vraiment presque réussi!"
            
            jump fr_ch_Form
        
        "Badminton {=bool}OU{/=bool} pickleball {=bool}OU{/=bool} tennis {=bool}OU{/=bool} ping-pong \ \ {=bool}ET{/=bool} \ \ lunettes {=bool}ET{/=bool} casquette {=bool}ET{/=bool} \ \ bleu":
        #Badminton OU pickleball OU tennis OU ping-pong \ \ ET \ \ lunettes ET casquette ET \ \ bleu
            call victoryWon from _call_victoryWon_12
            show sport1 at formPos1
            show sport2 at formPos5
            show sport3 at formPos9
            show sport4 at formPos13
            show facial1 at formPos2
            show facial2 at formPos3
            show color1 at formPos4
            with dissolve

            sv "Un tableau apparaît à l'écran. La première colonne contient un sport différent sur chaque ligne."
            sv "La première ligne contient un sport sur la première colonne, 'lunette' sur la deuxième colonne, 'casquette' sur la troisième colonne, et 'bleu' sur la quatrième colonne."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            "Je pense que je suis proche!"
    return

#These are the bones for the form used in all versions of Chapter 1
label en_ch_Form:
    scene form with dissolve
    sv "Menu"
    $shuffle_menu()
    menu:
        "How to fill out the form if you can only pick one favorite sport?"
        "Badminton {=bool}AND{/=bool} pickleball {=bool}AND{/=bool} tennis {=bool}AND{/=bool} ping-pong \ \ {=bool}OR{/=bool} \ \ glasses {=bool}AND{/=bool} goatee \ \ {=bool}OR{/=bool} \ \ blue" if not chMenu1:
        #Badminton AND pickleball AND tennis AND ping-pong \ \ OR \ \ glasses AND goatee \ \ OR \ \ blue
            $chMenu1 = True
            call victoryLost from _call_victoryLost_28
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos2
            show sport3 at formPos3
            show sport4 at formPos4
            show facial1 at formPos5
            show facial2 at formPos6
            show color1 at formPos9
            with dissolve
            
            sv "A table appears on the screen. A different sport is on every column of the first row. The second row contains 'glasses' on the first column and 'goatee' on the second column."
            sv "'Blue' is on the third row, first column."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Whoa, not even close. I don't think you really get the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool}."
                r "Or even how the form works — one idea per column, the different words to express the idea on different rows."
                r "Right now, if a student here wears {=word}glasses{/=word} and a {=word}goatee{/=word}, you'll find their room number even 
                   if they like green and aren't interested in sports. You'll get a ton of people to sort through."
                r "Let's use Maxim as an example, he has a great {=word}goatee{/=word} and wears {=word}glasses{/=word}."
                r "We start by looking at the first part of your search expression. {=word}Badminton{/=word} {=bool}AND{/=bool} {=word}pickleball{/=word} {=bool}AND{/=bool} {=word}tennis{/=word} {=bool}AND{/=bool} {=word}ping-pong{/=word}?
                    That's of very little interest to Maxim. Or {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word}? Sure, that describes Maxim. Ou {=word}blue{/=word} as a favorite color? Nope."
                r "The {=bool}OR{/=bool} boolean operator means that any of these options will make us happy, so the way you've set it up, we can pick students with only their favorite color or
                    facial features to find a room number. You're going to have a lot of numbers!"
                r "For sports, you would find someone that has {=word}badminton{/=word}, {=word}pickleball{/=word}, {=word}tennis{/=word}
                    AND {=word}ping-pong{/=word} as a favorite sport. Four favorite sports!"
                r "So your search expression really doesn't work. Please fill out another form."
                
            elif chosenPath == "Pharmacy":
                p "That's reassuring! I'm still functionning well enough that I can tell that you haven't grasped the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool}."
                p "Or how the form even works — it's one idea per column, the different words to express one idea are placed on different rows."
                p "Right now, if a client wears {=word}glasses{/=word} and has a {=word}goatee{/=word}, you'll find him even if he likes green
                    and isn't interested in sports. You'll find lots of clients, so it's going to be tricky to spot my brother."
                p "I'll use Ferguson as an example. He has a terrible {=word}goatee{/=word} and wears {=word}glasses{/=word}."
                p "Let's look at each segment of your boolean search expression. {=word}Badminton{/=word} {=bool}AND{/=bool} {=word}pickleball{/=word} {=bool}AND{/=bool} {=word}tennis{/=word} {=bool}AND{/=bool} {=word}ping-pong{/=word}?
                    That doesn't interest Ferguson at all. Or {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word}? Sure, that does describe Ferguson. Or {=word}blue{/=word}? No."
                p "The {=bool}OR{/=bool} boolean operators means that any of these options would make us happy, so we can go by colors or by facial characteristics to find a client. You're
                   going to find lots of people!"
                p "For sports, we would need to find someone that has {=word}badminton{/=word}, {=word}pickleball{/=word}, {=word}tennis{/=word}
                    and {=word}ping-pong{/=word} as a favorite sport. Four favorite sports!"
                p "So your search expression doesn't really work. You'll have to fill out a new form."
                p "Create a great answer sheet for me!"
            
            else:
                b "Oh no...no... I can't have explained the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool} very well."
                b "Or how the form works — each column represents a different idea. Within an idea, each row is a different word that can be used to express that idea."
                b "Right now, if a criminal in the database wears {=word}glasses{/=word} and has a {=word}goatee{/=word}, we'll find his name even if he likes green and 
                   isn't interested in sports. You'll find tons of names of criminals, that's not going to help much."
                b "I'll use Arsène as an example. He often wears {=word}glasses{/=word} and sometimes disguises himself with a {=word}goatee{/=word} ."
                b "I start by evaluating each part of your search expression. {=word}Badminton{/=word} {=bool}AND{/=bool} {=word}pickleball{/=word} {=bool}AND{/=bool} {=word}tennis{/=word} {=bool}AND{/=bool} {=word}ping-pong{/=word}?
                    They are of no interest to Arsène. Or {=word}glasses{/=word} {=bool}AND{/=bool} a {=word}goatee{/=word}? Yes, that does describe Arsène. Or {=word}blue{/=word} as a favorite color? No."
                b "The {=bool}OR{/=bool} boolean operator tells us that any of these options would satisfy our search expression, so the database can match just the color, or just the facial appearance to find a person.
                   You're going to get a lot of names!"
                b "For sports, we want a person that has one of the following sports as a favorite sport: {=word}badminton{/=word}, {=word}pickleball{/=word}, {=word}tennis{/=word}
                    or {=word}ping-pong{/=word}. Not all four sports at once!"
                b "So your search expression doesn't really work. Fill out another form, I know you can get it this time!"
            
            jump en_ch_Form
            
        "Badminton {=bool}AND{/=bool} pickleball {=bool}AND{/=bool} tennis {=bool}AND{/=bool} ping-pong \ \ {=bool}OR{/=bool} \ \ glasses {=bool}AND{/=bool} goatee {=bool}AND{/=bool} blue" if not chMenu2:
        #Badminton AND pickleball AND tennis AND ping-pong \ \ OR \ \ glasses AND goatee AND blue
            $chMenu2 = True
            call victoryLost from _call_victoryLost_29
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos2
            show sport3 at formPos3
            show sport4 at formPos4
            show facial1 at formPos5
            show facial2 at formPos6
            show color1 at formPos7
            with dissolve
            
            
            sv "A table appears on the screen. A different sport is on every column of the first row."
            sv "In the second row, 'glasses' is in the first column, 'goatee' in the second column, 'blue' in the third column."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Wow, what a terrible answer! I don't think you've grasped the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool}."
                r "And don't forget that each column should contain one concept, with synonyms going on different rows."
                r "Right now, we could validate your search expression two ways. Let's use Peter as an example.
                   He often wears {=word}glasses{/=word}, sports a {=word}goatee{/=word}, and drives a shiny {=word}blue{/=word} motorcycle."
                r "In the first part of the search expression, you ask for {=word}Badminton{/=word} {=bool}AND{/=bool} {=word}pickleball{/=word} {=bool}AND{/=bool} {=word}tennis{/=word} {=bool}AND{/=bool} {=word}ping-pong{/=word}."
                r "Absolutly NO ONE at this dorm has chosen FOUR favorite sports, so this part of the boolean expression wouldn't match with a single name."
                r "{=bool}OR{/=bool}, you're giving us a second alternative, so I'll look at the second part of the search expression."
                r "You want {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word} {=bool}AND{/=bool} {=word}blue{/=word}?"
                r "That describes several people in this dorm, including Peter."
                r "We don't want to have to look at too many names, so you're going to have to be more specific by adding in Charlie's favorite sport."
                r "Here, I have another blank form."
                
            elif chosenPath == "Pharmacy":
                p "My brain still works well enough to see that you're clearly joking."
                p "Each column is supposed to contain only ONE idea, with the different synonyms for the idea distributed on rows."
                p "As it is, I can validate your search expression in two different ways."
                p "Let's use my friend Peter as an example. He has {=word}glasses{/=word}, sports a {=word}goatee{/=word}, and drives a beautiful {=word}blue{/=word} motorcycle."
                p "In the first part of the search expression, you ask for {=word}badminton{/=word} {=bool}AND{/=bool} {=word}pickleball{/=word} {=bool}AND{/=bool} {=word}tennis{/=word} {=bool}AND{/=bool} {=word}ping-pong{/=word}."
                p "Absolutely no one has put down FOUR favorite sports, so this first part of the search expression won't locate anyone."
                p "{=bool}OR{/=bool}, you're giving us a second alternative, so I'll look at the second part of the search expression."
                p "You want {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word} {=bool}AND{/=bool} {=word}blue{/=word}?"
                p "That describes several people, including my brother."
                p "You're making some sort of fun joke, but this is a serious situation!"
                p "Here, I've got another form."
                
            else:
                b "Oh no, that's not at all the right answer. You need to understand the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool}."
                b "And know that each column represents a concept, and each row within a column shows a different synonym of that same concept."
                b "As it is, I can validate your search expressions two ways.
                    We'll use Jack as an example. He wears {=word}glasses{/=word}, has a {=word}goatee{/=word}, and drives a beautiful blue {=word}car{/=word}."
                b "In the first part of the search expression, you ask for {=word}badminton{/=word} {=bool}AND{/=bool} {=word}pickleball{/=word} {=bool}AND{/=bool} {=word}tennis{/=word} {=bool}AND{/=bool} {=word}ping-pong{/=word}."
                b "In the database, NO ONE has entered four favorite sports, so this part of the search expression wouldn't locate any names."
                b "{=bool}OR{/=bool}, you're giving the database a second alternative, so we can examine the second part of your search expression."
                b "You want {=word}glasses{/=word} {=bool}AND{/=bool} {=word}goatee{/=word} {=bool}AND{/=bool} {=word}blue{/=word}?"
                b "That describes many people in addition to our suspect. Including Jack. We need the suspect's favorite sport to reduce the list of possibilities."
                b "I know you can do better. I believe in you! The class believes in you!"
                b "Here's another form for you to use to try again."
            
            jump en_ch_Form
            
        "Badminton {=bool}OR{/=bool} pickleball {=bool}OR{/=bool} tennis {=bool}OR{/=bool} ping-pong \ \ {=bool}AND{/=bool} \ \ glasses {=bool}OR{/=bool} goatee {=bool}OR{/=bool} blue" if not chMenu3:
        #Badminton OR pickleball OR tennis OR ping-pong \ \ AND \ \ glasses OR goatee OR blue    
            $chMenu3 = True
            call victoryLost from _call_victoryLost_30
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos5
            show sport3 at formPos9
            show sport4 at formPos13
            show facial1 at formPos2
            show facial2 at formPos6
            show color1 at formPos10
            with dissolve
            
            sv "A table appears on the screen. The first column contains a different sport on each row."
            sv "The second column has 'glasses' in the first row, 'goatee' on the second row, and 'blue' on the third row."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Wow, your answer isn't very good! I don't think you understand the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool}."
                r "And you HAVE to put each idea in its own column, with synonyms being on rows within a same column."
                r "Everything is fine in the first part of your search expression."
                r "You want someone that has {=word}Badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} {=word}ping-pong{/=word} as a favorite sport?"
                r "That's perfect, Charlie's favorite sport is definitely one of these four options."
                r "But then, you stop making sense in the second part of the search expression."
                r "On top of Charlie's favorite sport, you want either {=word}glasses{/=word} {=bool}OR{/=bool} {=word}goatee{/=word} {=bool}OR{/=bool} {=word}blue{/=word}?"
                r "Really?! That describes way too many people. If someone has {=word}badminton{/=word} as a favorite sport and likes the color {=word}blue{/=word},
                    we'll find him using your search expression."
                r "Someone wearing {=word}glasses{/=word} who likes to play {=word}tennis{/=word}? We'll also find them."
                r "We'll find any person that has {=word}tennis{/=word} as a favorite sport, as long as they also wear {=word}glasses{/=word} or have a {=word}goatee{/=word} or likes the color {=word}blue{/=word}."
                r "And the same goes for the other three sports."
                r "You need to add more criterias to be more specific, and to add more criterias, we use the {=bool}AND{/=bool} boolean operator..."
                r "I'm feeling fairly generous, so I'll let you recycle your form for an art piece we're creating for the dean."
                r "You can try again with a different form."
            
            elif chosenPath == "Pharmacy":
                p "Wow, your answer isn't very good! You're testing me to see how I'll react? That's so thoughtful!"
                p "I'll explain my reasoning, and you can tell me if I'm close!"
                p "You haven't organized everything by placing each idea in a column, and the different synonyms of a same idea on the rows."
                p "Everything is fine in the first part of your search expression."
                p "You want someone that has {=word}Badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} {=word}ping-pong{/=word} as a favorite sport?"
                p "That's perfect, my brother's favorite sport is definitely among these four options."
                p "But then, the second part of your search expression doesn't make much sense."
                p "On top of my brother's favorite sport, you want either {=word}glasses{/=word} {=bool}OR{/=bool} {=word}goatee{/=word} {=bool}OR{/=bool} {=word}blue{/=word}?"
                p "That describes a lot of people! If someone has {=word}badminton{/=word} as a favorite sport and likes the color {=word}blue{/=word},
                    they'll be found by your search expression."
                p "Someone wearing {=word}glasses{/=word} who likes to play {=word}tennis{/=word}? We'll also find them."
                p "We'll find anyone that has {=word}tennis{/=word} as a favorite sport, as long as they also wear {=word}glasses{/=word} or have a {=word}goatee{/=word}, or like the color {=word}blue{/=word}."
                p "And the same goes for the three other sports."
                p "We need to add more criterias to be more specific, and to add more criterias, we use the {=bool}AND{/=bool} boolean operator..."
                p "So? Am I close? TELL ME THAT I'M CLOSE!!!"
                "I don't have time to say anything before he puts another form in my hands!"
            
            else:
                b "Aw, I'm so sorry. You're still missing some nuances in the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool}."
                b "You can see that the structure of your form is a bit off — every column should contain an idea, and rows should contain alternate synonyms of that idea."
                b "In the first part of your boolean search expression, everything is great."
                b "You're looking for someone that has {=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} {=word}ping-pong{/=word} as a favorite sport?"
                b "That's perfect! The favorite sport of the heartless criminal is definitely one of those four options."
                b "But the second part of your boolean search expression is problematic."
                b "In addition to the criminal's favorite sport, you're requesting {=word}glasses{/=word} {=bool}OR{/=bool} {=word}goatee{/=word} {=bool}OR{/=bool} {=word}blue{/=word}?"
                b "That describes a lot of people! If someone has {=word}badminton{/=word} as a favorite sport and likes {=word}blue{/=word},
                    your search expression will locate them."
                b "We would also find someone wearing {=word}glasses{/=word} who loves to play {=word}tennis{/=word}."
                b "In fact, we'll find any criminal that has {=word}tennis{/=word} as a favorite sport, as long as they wear {=word}glasses{/=word} or have a {=word}goatee{/=word} or like the color {=word}blue{/=word}."
                b "And the same goes for the three other sports."
                b "You have to add more criterias to be more specific, and to add more criterias, we use the {=bool}AND{/=bool} boolean operator..."
                b "I'll recycle this form — it's good for the environment — and give you the chance to try again with a nice clean form."
            
            jump en_ch_Form
            
        "Badminton {=bool}OR{/=bool} pickleball {=bool}OR{/=bool} tennis {=bool}OR{/=bool} ping-pong \ \ {=bool}AND{/=bool} \ \ glasses {=bool}OR{/=bool} goatee \ \ {=bool}AND{/=bool} \ \ blue" if not chMenu4:
        #Badminton OR pickleball OR tennis OR ping-pong \ \ AND \ \ glasses OR goatee \ \ AND \ \ blue
            $chMenu4 = True
            $flagCount +=1
            
            show sport1 at formPos1
            show sport2 at formPos5
            show sport3 at formPos9
            show sport4 at formPos13
            show facial1 at formPos2
            show facial2 at formPos6
            show color1 at formPos3
            with dissolve
            
            sv "A table appears on the screen. The first column contains a different sport on each row."
            sv "The second column has 'glasses' in the first row, and 'goatee' on the second row. 'Blue' is on the first row of the third column."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            if chosenPath == "Charlie":
                r "Hmmm, that's almost the right answer! Is it possible that you actually understand the subtleties between {=bool}OR{/=bool} and {=bool}AND{/=bool}?"
                r "The first part of your boolean search expression is perfect! Just perfect!"
                r "You want {=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} {=word}ping-pong{/=word} as a favorite sport?"
                r "That's perfect, one of these four options definitely includes Charlie's favorite sport."
                r "And he does like {=word}blue{/=word}."
                r "Really, the only thing that's not quite right is the central part of your search statement: {=word}glasses{/=word} {=bool}OR{/=bool} {=word}goatee{/=word}?"
                r "Charlie ALWAYS wears his {=word}glasses{/=word}, and I don't think he's ever going to shave off that {=word}goatee{/=word}."
                r "{size=-3}He dyes it interesting colors sometimes...{/size}"
                r "Even if you were trying to imply that he only sometimes wears glasses, the search expression doesn't work 
                   because it would grab anyone that wears glasses but doesn't have a goatee."
                r "In any event, you need to tell me that he wears {=word}glasses{/=word} and has a {=word}goatee{/=word}."
                r "I'm going to create a paper airplane with your form. You can fill out another one."
                
            elif chosenPath == "Pharmacy":
                p "They're so close! Our answers are almost identical!"
                p "The first segment in your search expression is perfect."
                p "You want {=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} {=word}ping-pong{/=word} as a favorite sport?"
                p "One of these four options definitely includes my brother's favorite sport."
                p "And he does enjoy the color {=word}blue{/=word}."
                p "Really, the only thing that's not quite right is the central part of your search expression: {=word}glasses{/=word} {=bool}OR{/=bool} {=word}goatee{/=word}?"
                p "My brother ALWAYS wears his {=word}glasses{/=word} and I've never seen him without a {=word}goatee{/=word}."
                p "Even if you were trying to imply that he only sometimes wears glasses, the search expression doesn't work 
                   because it would grab anyone that wears glasses but doesn't have a goatee."
                p "You really want a search expression that says that he wears {=word}glasses{/=word} and a {=word}goatee{/=word}."
                p "I want to be really, REALLY sure that my brain is working okay. Could you fill out another form?"
                
            else:
                b "Congrats! That's almost a perfect answer! You clearly understand the difference between {=bool}OR{/=bool} and {=bool}AND{/=bool}?"
                b "The first part of your search expression is perfect."
                b "You want {=word}badminton{/=word} {=bool}OR{/=bool} {=word}pickleball{/=word} {=bool}OR{/=bool} {=word}tennis{/=word} {=bool}OR{/=bool} {=word}ping-pong{/=word} as a favorite sport?"
                b "That's perfect, one of these four options is definitely the criminal's favorite sport."
                b "And he does like to steal {=word}blue{/=word} jewellery."
                b "Really, the only thing that could be improved is the central part of your search expression: {=word}glasses{/=word} {=bool}OR{/=bool} {=word}goatee{/=word}?"
                b "According to witnesses, the criminal was wearing {=word}glasses{/=word} and had a {=word}goatee{/=word}. Both of these things are true!"
                b "We're going to put this form aside, but you really are almost there!"
            
            jump en_ch_Form
        
        "Badminton {=bool}OR{/=bool} pickleball {=bool}OR{/=bool} tennis {=bool}OR{/=bool} ping-pong {=bool}AND{/=bool} glasses {=bool}AND{/=bool} goatee {=bool}AND{/=bool} blue":
        #Badminton OR pickleball OR tennis OR ping-pong \ \ AND \ \ glasses AND goatee AND \ \ blue
            call victoryWon from _call_victoryWon_13
            show sport1 at formPos1
            show sport2 at formPos5
            show sport3 at formPos9
            show sport4 at formPos13
            show facial1 at formPos2
            show facial2 at formPos3
            show color1 at formPos4
            
            
            sv "A table appears on the screen. The first column contains a different sport on each row."
            sv "In the first row, the first column contains a sport, 'glasses' is in the second column, 'goatee' is in the third column, and 'blue' is in the fourth column."
            
            window hide
            $renpy.pause(3.0)
            window show
            
            "I have a good feeling..."
    return

#Sets up the Venn diagram sequence
label fr_Venn_Setup:
    
    $entry1 = myList[0]
    $entry2 = myList[1]
    $entry3 = myList[2]
    
    sv "Un diagramme Venn apparaît à l'écran: deux cercles superimposés. Une partie d'un cercle à la gauche, une intersection où les deux cercles sont superimposés, et une partie d'un cercle à la droite."
    sv "Le premier mot se trouve sur le cercle de gauche, le deuxième mot sur le cercle de droite."
    
    #"" is the placeholder for the right choices in the list
    $vennList = (("","La tablette fait un petit BEEP.", "Ça ne fonctionne pas.", "Ce n'est pas le bon choix."),
        ("Je me pose des sérieuses questions à propos de mes choix de vie.", "", "Je n'ai pas choisi la bonne option.", "La porte refuse de se déverouiller."),
        ("Ooops, mon doit a glissé, ce n'est clairement pas la bonne réponse.", "BEEP BEEP BEEP BEEP", "SÉRIEUSEMENT? Ce n'est pas la bonne option?"),
        ("Non. Pourquoi j'ai pensé que ça pourrait fonctionner?", "Ce n'est pas ça.", "", "Je vais DÉMOLIR la place avant de repartir."))
    
    #Menu text in fr_Venn_choice
    if chosenPath == "Sport":
        $vennMenuList = ("Frapper le bon bouton pour allumer le cercle de gauche!","Frapper le bon bouton pour allumer le cercle de droite.","Allumer les deux cercles avec beaucoup de force.","Allumer l'intersection avec précision.")
    else:
        $vennMenuList = ("Allumer le cercle de gauche.","Allumer le cercle de droite.","Allumer les deux cercles.","Allumer l'intersection.")
    
    call fr_Venn1 from _call_fr_Venn1
    call fr_Venn2 from _call_fr_Venn2
    call fr_Venn3 from _call_fr_Venn3
    call fr_Venn4 from _call_fr_Venn4

    hide Venn0

    return
    
#Sets up the Venn diagram sequence
label en_Venn_Setup:
    
    call sc_black from _call_sc_black_11
    
    $entry1 = myList[0]
    $entry2 = myList[1]
    $entry3 = myList[2]
    
    
    sv "A Venn diagram appears on the screen: two intersecting circles. Part of a circle on the left, a segment where the two circles intersect, part of a circle on the right."
    sv "The first word is on the left circle, the second word on the right circle."
    
    #"" is the placeholder for the right choices in the list
    if chosenPath == "Sport":
        $vennList = (("","It beeps.", "It doesn't work.", "That's not the right choice."),
            ("I'm asking myself some hard questions about my life choices.", "", "I didn't pick the right option.", "The thing doesn't light up."),
            ("Ooops, my finger slipped, this is clearly not what I meant to hit.", "BEEP BEEP BEEP BEEP", "SERIOUSLY? That's not the right option?"),
            ("No. Why did I think this would work?", "That's not it.", "", "I am going to DEMOLISH this thing before I go."))
    else:
        $vennList = (("","It beeps.", "It doesn't work.", "That's not the right choice."),
            ("I'm asking myself some hard questions about my life choices.", "", "I didn't pick the right option.", "The door stays locked."),
            ("Ooops, my finger slipped, this is clearly not the right answer.", "BEEP BEEP BEEP BEEP", "SERIOUSLY? That's not the right option?"),
            ("No. Why did I think this would work?", "That's not it.", "", "I am going to DEMOLISH this thing before I go."))
    
    #Menu text in fr_Venn_choice
    if chosenPath == "Sport":
        $vennMenuList = ("Hit the correct button to turn on the left circle!","Hit the correct button to turn on the right circle!","Turn on the two circles!","Turn on the area where the circles intersect.")
    else:
        $vennMenuList = ("Turn on the left circle.","Turn on the right circle.","Turn on both circles.","Turn on the area where the circles intersect.")
    
    call fr_Venn1 from _call_fr_Venn1_1
    call fr_Venn2 from _call_fr_Venn2_1
    call fr_Venn3 from _call_fr_Venn3_1
    call fr_Venn4 from _call_fr_Venn4_1

    hide Venn0

    return

#Top of all four fr_Venn
label fr_Venn_Setup_Top:
    show Venn0 at venTop
    show text "{=book}[entry1]{/=book}" at venWord
    return

#Hides and reactivates the label for Venn diagram
label fr_Venn_label:
    hide text
    show text "{=book}[entry1]{/=book}" at venWord
    return

#Activates when the wrong option is chosen in fr_Venn
label fr_Venn_Wrong:
    
    call victoryLost from _call_victoryLost_31
    $flag3 += 1
    
    #Show the solution picked by the user
    if flag2 == 0:
        show Venn2 at venTop
    elif flag2 == 1:
        show Venn3 at venTop
    elif flag2 == 2:
        show Venn4 at venTop
    else:
        show Venn1 at venTop
    
    call fr_Venn_label from _call_fr_Venn_label
    
    #Display a quick message about the mis5take
    $entry9 = vennList[flagCount][flag2]
    "[entry9]"
    
    #Remove the mistaken selection
    if flag2 == 0:
        hide Venn2
    elif flag2 == 1:
        hide Venn3
    elif flag2 == 2:
        hide Venn4
    else:
        hide Venn1
    
    #Go back and choose the right option
    if flagCount == 0:
        jump fr_Venn1
    elif flagCount == 1:
        jump fr_Venn2
    elif flagCount == 2:
        jump fr_Venn3
    else:
        jump fr_Venn4
    
    return

#Reacts to the Venn label chosen by the user
label fr_Venn_Choice:
    
    $vennMenuOpt = vennMenuList[flagCount]
    
    sv "Menu"
    $unshuffle_menu()
    menu:
        "[vennMenuOpt]"
        "[entry2]":
            $flag2 = 0
            
            if lang == "english":
                sv "The entire left circle lights up, including the segment where it intersects with the right circle."
            else:
                sv "Le cercle de gauche entier s'allume, y compris le segment où le cercle de droite est superimposé."
            
            #If we're in the correct left Venn Venn1
            if flagCount == 0:
                call victoryWon from _call_victoryWon_14
                show Venn2 at venTop
                call fr_Venn_label from _call_fr_Venn_label_1
                if lang == "english":
                    "The left circle lights up correctly."
                else:
                    "Le diagramme s'allume correctement."
                hide Venn2
                hide text
                $victoryFlag = False
            #Anywhere else
            else:
                call fr_Venn_Wrong from _call_fr_Venn_Wrong
                
        "[entry3]":
            $flag2 = 1
            
            if lang == "english":
                sv "The entire right circle lights up, including the segment where it intersects with the left circle."
            else:
                sv "Le cercle de droite entier s'allume, y compris le segment où le cercle de gauche est superimposé."
    
            #If we're in the correct right Venn Venn2
            if flagCount == 1:
                call victoryWon from _call_victoryWon_15
                show Venn3 at venTop
                call fr_Venn_label from _call_fr_Venn_label_2
                if lang == "english":
                    "The right circle lights up correctly."
                else:
                    "Le diagramme s'allume correctement."
                hide Venn3
                hide text
                $victoryFlag = False
            else:
                call fr_Venn_Wrong from _call_fr_Venn_Wrong_1
                
        "[entry2] {=bool}AND{/=bool} [entry3]":
            $flag2 = 2
            
            if lang == "english":
                sv "The intersection containing both the left and the right circle lights up."
            else:
                sv "L'intersection où est superimposée le cercle de gauche et le cercle de droite s'allume."

             #If we're in the correct AND Venn Venn4
            if flagCount == 3:
                call victoryWon from _call_victoryWon_16
                show Venn4 at venTop
                call fr_Venn_label from _call_fr_Venn_label_3
                if lang == "english":
                    "That's right, the {=bool}AND{/=bool} boolean operator reduces the number of results."
                else:
                    "C'est vrai, le {=bool}AND{/=bool} réduit le nombre de résultats."
                hide Venn4
                hide text
                $victoryFlag = False
            else:
                call fr_Venn_Wrong from _call_fr_Venn_Wrong_2
            
        "[entry2] {=bool}OR{/=bool} [entry3]":
            $flag2 = 3
            
            if lang == "english":
                sv "Both circles, including the intersection, light up."
            else:
                sv "Les deux cercles s'allument, y compris à l'intersection où les cercles sont superimposés."

            #If we're in the correct OR Venn Venn3
            if flagCount == 2:
                call victoryWon from _call_victoryWon_17
                show Venn1 at venTop
                call fr_Venn_label from _call_fr_Venn_label_4
                if lang == "english":
                    "That works! That's right, the {=bool}OR{/=bool} boolean operator increases the number of results."
                else:
                    "Ça fonctionne!"
                    "Je ne dois pas oublier que le {=bool}OR{/=bool} augmente le nombre de résultats."
                hide Venn1
                hide text
                $victoryFlag = False
            else:
                call fr_Venn_Wrong from _call_fr_Venn_Wrong_3
    return

#Left Venn
label fr_Venn1:
    $flagCount = 0

    call fr_Venn_Setup_Top from _call_fr_Venn_Setup_Top
    call fr_Venn_Choice from _call_fr_Venn_Choice
    
    return
    
#Right Venn
label fr_Venn2:
    
    $flagCount = 1
    call fr_Venn_Setup_Top from _call_fr_Venn_Setup_Top_1
    call fr_Venn_Choice from _call_fr_Venn_Choice_1
    
    return

#OR Venn for both
label fr_Venn3:
        
    $flagCount = 2
    call fr_Venn_Setup_Top from _call_fr_Venn_Setup_Top_2
    call fr_Venn_Choice from _call_fr_Venn_Choice_2

    return

#AND Venn for intersection
label fr_Venn4:
    
    $flagCount = 3
    call fr_Venn_Setup_Top from _call_fr_Venn_Setup_Top_3
    call fr_Venn_Choice from _call_fr_Venn_Choice_3

    return
    
#Loading the safe screen
label fr_load_safe:
    
    window hide None
    call screen unlock_safe
    window show None
    
    #Grab the number clicked by the user
    $safeNumb = _return
    call fr_load_safe_list from _call_fr_load_safe_list
    
    return

#loading the safe list and checking if we are done
label fr_load_safe_list:
    
    #If we're not on the first number, add the comma or space before adding the number or letter
    if len(myWordString) != 0:
        $myWordString += " "
    
    if len(mySafeString) !=0:
        $mySafeString += ","
    
    #Put the new number in the temporary string
    $mySafeString += safeNumb
    
    #If the number is the correct number, put it in a temporary string, otherwise put in "?"
    if safeNumb == safeButtonLists[safeIC][safeCIB][len(mySafeString)-1]:
        $myWordString += safeWord[len(myIteration)-1]
    else:
        $myWordString += "?"
        
    $myIteration += " " #Serves as index to grab the right letter
            
    #Check if we are done collecting numbers
    if len(mySafeString) == len(safeButtonLists[safeIC][safeCIB]):
        jump fr_safe_check_list
    else:
        jump fr_load_safe
        
    return

#checking to see if the user selected the right numbers
label fr_safe_check_list:
    
    #Check to see if we have the right code
    if mySafeString == safeButtonLists[safeIC][safeCIB]:
        if lang == "english":
            "It beeps and opens! I did it!"
        else:
            "Un petit beep et ça s'ouvre! J'ai réussi!"
    else:
        #Check if * is at the end of the code
        if lang == "english":
            "Nothing happens. It looks like [mySafeString] isn't the right combination."
        else:
            "Rien ne se passe. On dirait que [mySafeString] n'est pas la bonne combinaison."
        
        if "*" in mySafeString:
            if lang == "english":
                "But I think I'm very close!"
            else:
                "Mais je pense que je suis très proche!"
            if mySafeString[-1] != "*":
                if lang == "english":
                    "The asterix should probably be at the end of the sequence..."
                else:
                    "L'astérix devrait probablement être entrée à la fin de la séquence..."
        else:
            if lang == "english":
                "I should probably use an asterix."
            else:
                "Je devrais probablement utiliser une astérix..."
        
        $flagCount += 1 #Keeps track of the number of attempts so that buttons are reveleaed after two attempts
        $mySafeString = ""
        $myWordString = ""
        $myIteration = "1"
        jump fr_load_safe
    return

#Ending to Chapter 1
label fr_ch1_ending:
    
    stop music fadeout 3
    call sc_street from _call_sc_street_6
    
    #If we brought a friend, change simple sentences accordingly - flag2 is the index to the list
    if companion:
        $flag2 = 1
    else:
        $flag2 = 0
        
    $myList = (("j'ai", "Laisse-moi", "t'", "Donne", "J'ai", "j'ai dû m'", "moi"),
        ("on a", "Laisse-nous", "vous ", "Donnez", "On a", "on a dû s'", "nous"))
    
    #Loading the list in variables for easier retrieval inside Renpy strings
    $entry1 = myList[flag2][0]
    $entry2 = myList[flag2][1]
    $entry3 = myList[flag2][2] 
    $entry4 = myList[flag2][3]
    $entry5 = myList[flag2][4]
    $entry6 = myList[flag2][5]
    $entry7 = myList[flag2][6]

    "J'ai eu l'impression de voir plus de zombies dans les rues en retournant chez elle."
    
    if kitten:
        "Dans une des rares rues vides de zombies, [entry6]arrêter quelques minutes."
        "Une chatte accompagnée de plusieurs petits chatons a lentement traversé la rue devant [entry7]"
    
    #And if we didn't go to Charlie, add a sentence saying that we tried
    if chosenPath <> "Charlie":
        "([entry5] passé par la résidence d'étudiant pour trouver Charlie, mais la résidence était envahie.)"

    "J'ai stationné la voiture chez Évangeline puis [entry1] essayé d'entrer. Elle avait barré sa porte! J'ai cogné plusieurs fois."
    
    if chosenPath == "Sport":
        g "Évangeline! [entry2] entrer! J'ai des armes pour mieux nous défendre!"
        e "Pas de défibrillateur cardiaque? Pas d'entrée dans la maison."
        g "T'es pas sérieuse! Ce n'est plus très sécuritaire dehors."
        e "Je veux au moins être certaine que c'est toi! Donne moi le nom d'un opérateur booléen."
        
    else:
        g "Évangeline! [entry2] entrer! J'ai le défibrillateur cardiaque!"
        e "Donne moi le nom d'un opérateur booléen et je vais [entry3]ouvrir la porte."
        g "T'es pas sérieuse!"
        e "Je veux être certaine que c'est toi!"
        
    g "Non! Pleins de gens connaissent les opérateurs booléens! Et tu es parfaitement capable de reconnaître ma voix!"
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    e "..."
    "Elle a ouvert la porte!"

    call ms_lithium from _call_ms_lithium_7
    call sc_evangeline from _call_sc_evangeline_2
    show Creature neutral at my_out_init_buffer 
    g "Ouf, ça fait du bien d'être en sécurité dans une maison!"
    
    #Get reaction to someone coming back, if there is someone
    if companion:
        show Eva determ
        
        if chosenPath == "Charlie":
            e "Tu as ramené un ami? C'est qui?"
            show Reception happy
            g "Euh, Évangeline, je te présente...euh...le réceptionniste de la résidence."
            show Reception neutral
            show Eva pensive
            sv "Un moment de silence. Cliquez deux fois pour continuer."
            r "..."
            e "Tu ne connais même pas son nom?!"
            r "Wilfred."
            show Eva satisfaction
            $reception_name = "Wilfred"
            show Reception stars
            r "Étudiant en arts visuels, spécialisation en natures mortes."
            
        elif chosenPath == "Pharmacy":
            show Pharma relieved
            e "Tu as ramené un ami? C'est qui?"
            g "Euh, Évangeline, je te présente...euh...un pharmacien."
            show Pharma terrified
            sv "Un moment de silence. Cliquez deux fois pour continuer."
            p "..."
            show Eva determ
            show Pharma afraid
            p "Joey"
            $pharmacist_name = "Joey"
            p "Je ne suis probablement pas en train de devenir un zombie..."
            show Eva mwahaha
            e "Dommage, ça serait intéressant à étudier!"
            show Pharma terrified

        else:
            show Proprio satisfaction
            e "Tu as ramené une amie? C'est qui?"
            g "Euh, Évangeline, je te présente...euh...la propriétaire d'un magasin d'articles de sport."
            show Proprio unhappy
            sv "Un moment de silence. Cliquez deux fois pour continuer."
            s "..."
            show Eva mwahaha 
            e "Tu ne connais même pas son nom?!"
            s "Viola."
            $sportsGo_name = "Viola"
            show Proprio happy
            s "Enchantée."
            show Proprio drill
            s "On devrait mettre nos ressources en commun pour se préparer à démolir les zombies un par un!"
            
            
    #If there is no one, Évangeline greets you
    else:
        show Eva satisfaction
        e "Contente de voir que tu es de retour!"
    
    show Eva pensive
    
    #Companion reactions
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
            
    e "Où est Charlie?"
    
    #Companion reactions
    if companion:
        if chosenPath == "Charlie":
            show Reception obssessed
        elif chosenPath == "Pharmacy":
            show Pharma afraid
        else:
            show Proprio unhappy
    
    #What happened to Charlie
    if chosenPath == "Charlie":
        g "Euh...il était...préoccupé par la situation. Je n'ai pas vraiment eu la chance de le rencontrer..."
    elif chosenPath == "Sport":
        g "Euh...il y avait trop de zombies à la résidence pour le retrouver. Charlie a probablement évacué ailleurs?"
    else:
        g "Euh... la résidence était envahie. Je n'ai pas vraiment eu la chance de le rencontrer."

     
    #Companion follow-up reactions
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
        elif chosenPath == "Pharmacy":
            show Pharma terrified
        else:
            show Proprio drill
    
    show Eva pensive
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    e "..."
    
    if chosenPath == "Sport":
        g "Et je n'ai pas trouvé un défibrillateur cardiaque."
        e "Bon, pas le choix, je vais utiliser le mien."
        g "QUOI! Tu as un défibrillateur cardiaque?"
        if companion:
            show Proprio unhappy
        e "J'espérais trouver un modèle plus récent. Quel dommage!"
        e "Mais je suppose qu'on peut utiliser les trucs que tu as rapporté pour se défendre."
    else:
        g "Ah! Mais j'ai ton défibrillateur cardiaque!"
        show Eva determ
        e "Super! On va l'essayer tout de suite!"
    
    sv "Évangeline part dans le sous-sol et ramasse la créature."
    #Placements of everyone for Creature attempts
    if companion:
        show Eva determ at center with move
        if chosenPath == "Charlie":
            show Reception neutral at left with move
        elif chosenPath == "Pharmacy":
            show Pharma afraid at leftAway with move
        else:
            show Proprio unhappy at left with move
    else:
        show Eva determ
            
            
    show Eva pensive at my_out_init with move

    show Eva pensive at center
    show Creature neutral at right
    with move
    
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    c "..."
    show Eva mwahaha
    
    #Companion reaction to creature
    if companion:
        if chosenPath == "Charlie":
            show Reception stars
            r "Wow! Quelle oeuvre magnifique! Un commentaire sur la futilité de se distancer des gens lorsqu'on partage
               tous éventuellement le même sort?"
            show Eva pensive
            e "Pas vraiment. C'est un robot biologique qui va nous défendre des zombies."
            show Reception passion
            r "Cool!"
            show Reception neutral
        
        elif chosenPath == "Pharmacy":
            show Pharma terrified
            p "QU'EST-CE QUE C'EST? Vous êtes MALADES!"
            show Eva determ
            e "C'est juste un robot biologique qui va lutter contre les zombies."
            show Pharma afraid
            p "C'est des morceaux de...personnes...cousus ensemble? CE N'EST PAS NORMAL! Si je deviens un zombie, vas-tu ajouter mes morceaux à cette horreur?"
            g "N'y pense pas trop fort! Tout est correct! C'est presque terminé!"
            
        else:
            s "C'est quoi cette horreur?"
            e "C'est un robot biologique qui va lutter contre les zombies."
            e "Je vais essayer de l'animer."
            show Proprio drill
            s "Comme il est laid! Si ça fonctionne, on va lui faire porter un casque."
            s "Ça va mieux le protéger."
    else:
        g "Brrr, ce truc est vraiment terrifiant."
        show Eva pensive
        e "Tu ne vas pas le trouver autant terrifiant lorsqu'il va combattre les zombies à notre place!"
        
    show Eva mwahaha
    "Évangeline a relié le défibrillateur cardiaque à sa création."
    "... rien ne se passe."
    show Eva determ
    e "Je pense qu'il faut un battement de coeur pour que la machine se déclenche. [entry4]-moi une seconde..."
    "Elle a joué avec des boutons. Cette fois, le défibrillateur a visiblement émit un choc."
    
    call sc_creaturejump from _call_sc_creaturejump
    show Eva mwahaha
    
    #Companion reaction to first zap
    if companion:
        if chosenPath == "Charlie":
            show Reception obssessed
        
        elif chosenPath == "Pharmacy":
            show Pharma relieved
            
        else:
            show Proprio unhappy
        
    e "Encore."
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    c "..."
    call sc_creaturejump from _call_sc_creaturejump_1
    
    e "Allez!"
    call sc_creaturejump from _call_sc_creaturejump_2
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    c "..."
    
    show Eva determ
    e "FONCTIONNE!"
    
    #Companion reaction to another zap
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
        
        elif chosenPath == "Pharmacy":
            show Pharma afraid
            
        else:
            show Proprio drill
    
    call sc_creaturejump from _call_sc_creaturejump_3
    sv "Un moment de silence. Cliquez deux fois pour continuer."
    c "..."
    
    show Eva pensive
    e "Bon, ça ne fonctionne pas. Je suis prête pour le plan b!"
    
    call ms_end from _call_ms_end_13
    g "Tu avais une autre idée?"
    
    return
    
#Ending to Chapter 1
label en_ch1_ending:
    
    stop music fadeout 3
    call sc_street from _call_sc_street_7
    
    #If we brought a friend, change simple sentences accordingly - flag2 is the index to the list
    if companion:
        $flag2 = 1
    else:
        $flag2 = 0
        
    $myList = (("I", "I", "Let me", "me"),
        ("We", "we", "Let us", "us"))
    
    #Loading the list in variables for easier retrieval inside Renpy strings
    $entry1 = myList[flag2][0]
    $entry2 = myList[flag2][2]
    $entry3 = myList[flag2][1]
    $entry4 = myList[flag2][3]

    "It feels like the number of zombies in the streets is increasing."
    
    if kitten:
        "In one of the rare empty streets, [entry3] stop for a few minutes."
        "A cat accompanied by several little kittens slowly crosses the street in front of [entry4]."
    
    #And if we didn't go to Charlie, add a sentence saying that we tried
    if chosenPath <> "Charlie":
        "([entry1] do stop by the student dorm to find Charlie, but the residence seems to be overrun.)"

    "I park the car at Évangeline's place, and then [entry3] try to go in. She's locked her door! I knock several times."
    
    if chosenPath == "Sport":
        g "Évangeline! [entry2] in! I have weapons we can use to defend ourselves!"
        e "No cardiac defibrillator? No entry!"
        g "Please don't say that, it's not very safe out here."
        e "How can I be sure that it's really you? Give me the name of a boolean operator!"
        
    else:
        g "Évangeline! [entry2] in! I have a cardiac defibrillator!"
        e "Give me the name of a boolean operator, and I'll open the door."
        g "You can't be serious!"
        e "I want to be sure that you're really you!"
        
    g "No! Plenty of people know about boolean operators. And you're perfectly capable of recognizing the sound of my voice!"
    sv "A silent beat. Click twice to continue."
    e "..."
    "She opens the door!"

    call ms_lithium from _call_ms_lithium_8
    call sc_evangeline from _call_sc_evangeline_3
    show Creature neutral at my_out_init_buffer 
    g "Feels good to be back behind locked doors!"
    
    #Get reaction to someone coming back, if there is someone
    if companion:
        show Eva determ
        
        if chosenPath == "Charlie":
            e "You brought a friend? Don't be rude, introduce us!"
            show Reception happy
            g "Um, Évangeline, this is...um...the receptionist at the dorm."
            show Reception neutral
            show Eva pensive
            sv "A silent beat. Click twice to continue."
            r "..."
            e "You don't even know his name?!"
            r "Wilfred."
            show Eva satisfaction
            $reception_name = "Wilfred"
            show Reception stars
            r "Visual art student, specialized in kinetic sculptures."
            
        elif chosenPath == "Pharmacy":
            show Pharma relieved
            e "Who's this?"
            g "Um, Évangeline, meet...a pharmacist."
            show Pharma terrified
            sv "A silent beat. Click twice to continue."
            p "..."
            show Eva determ
            show Pharma afraid
            p "Joey"
            $pharmacist_name = "Joey"
            p "I'm probably not changing into a zombie..."
            show Eva mwahaha
            e "Too bad, would have been interesting to witness!"
            show Pharma terrified

        else:
            show Proprio satisfaction
            e "Who is she?"
            g "Um, Évangeline, meet...the owner of a sports store."
            show Proprio unhappy
            sv "A silent beat. Click twice to continue."
            s "..."
            show Eva mwahaha 
            e "You don't even know her name?!"
            s "Viola."
            $sportsGo_name = "Viola"
            show Proprio happy
            s "Pleasure to meet you."
            show Proprio drill
            s "We should pool our resources and join together in the fight against the zombies!"
            
            
    #If there is no one, Évangeline greets you
    else:
        show Eva satisfaction
        e "Happy to see that you're back!"
    
    show Eva pensive
    
    #Companion reactions
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
            
    e "Where's Charlie?"
    
    #Companion reactions
    if companion:
        if chosenPath == "Charlie":
            show Reception obssessed
        elif chosenPath == "Pharmacy":
            show Pharma afraid
        else:
            show Proprio unhappy
    
    #What happened to Charlie
    if chosenPath == "Charlie":
        g "Um...he was...preoccupied by the situation. I didn't really have a chance to meet him..."
    elif chosenPath == "Sport":
        g "Um...there were too many zombies at the residence for us to try to meet him. Charlie probably evacuated somewhere else?"
    else:
        g "Um... the residence was overrun. I didn't get the chance to meet him."

     
    #Companion follow-up reactions
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
        elif chosenPath == "Pharmacy":
            show Pharma terrified
        else:
            show Proprio drill
    
    show Eva pensive
    sv "A silent beat. Click twice to continue."
    e "..."
    
    if chosenPath == "Sport":
        g "And I didn't find a cardiac defibrillator."
        e "Oh well, I guess we have no choice but to use mine."
        g "WHAT! You had a cardiac defibrillator this whole time?"
        if companion:
            show Proprio unhappy
        e "I was hoping for a more recent model. Oh well!"
        e "I suppose it's good that we can use this stuff you brought back to defend ourselves."
    else:
        g "Oh! But I do have your cardiac defibrillator!"
        show Eva determ
        e "Awesome! Let's try it out!"
    
    sv "Évangeline runs to the basement and brings back the creature."
    
    #Placements of everyone for Creature attempts
    if companion:
        show Eva determ at center with move
        if chosenPath == "Charlie":
            show Reception neutral at left with move
        elif chosenPath == "Pharmacy":
            show Pharma afraid at leftAway with move
        else:
            show Proprio unhappy at left with move
    else:
        show Eva determ
            
            
    show Eva pensive at my_out_init with move

    show Eva pensive at center
    show Creature neutral at right
    with move
    
    sv "A silent beat. Click twice to continue."
    c "..."
    show Eva mwahaha
    
    #Companion reaction to creature
    if companion:
        if chosenPath == "Charlie":
            show Reception stars
            r "Wow! What a beautiful work! A comment on the futility of distancing ourselves from other people when we'll all eventually
               suffer the same fate?"
            show Eva pensive
            e "Not really. This is a biological robot that will fight against the zombies for us."
            show Reception passion
            r "Cool!"
            show Reception neutral
        
        elif chosenPath == "Pharmacy":
            show Pharma terrified
            p "WHAT IS THAT THING? You guys are SICK!"
            show Eva determ
            e "It's a kind off biological robot that will fight the zombies for us."
            show Pharma afraid
            p "Are those pieces of...people...sewed together? THAT'S NOT NORMAL! If I become a zombie, are you just going to add a piece of me to that thing?"
            g "Don't think about it too much. Everything is okay. It's almost over!"
            
        else:
            s "What the heck is that thing?"
            e "It's a biological robot I've created to help fight the zombies."
            e "I just need to animate it."
            show Proprio drill
            s "Well if it works, we'll have to build some sort of mask for the ugly thing."
            s "It'll help protect it."
    else:
        g "Brrr, that thing is terrifying."
        show Eva pensive
        e "You won't complain about its looks once it starts beating up zombies for us!"
        
    show Eva mwahaha
    "Évangeline connects the cardiac defibrillator to her creation."
    "... nothing happens."
    show Eva determ
    e "Contrary to popular belief, I'm pretty sure these things need a heartbeat before they'll do anything. Give me a second..."
    "She opens the thing up and plays with some buttons. This time, the cardiac defibrillator visibly sparks."
    
    call sc_creaturejump from _call_sc_creaturejump_4
    show Eva mwahaha
    
    #Companion reaction to first zap
    if companion:
        if chosenPath == "Charlie":
            show Reception obssessed
        
        elif chosenPath == "Pharmacy":
            show Pharma relieved
            
        else:
            show Proprio unhappy
        
    e "Again."
    sv "A silent beat. Click twice to continue."
    c "..."
    call sc_creaturejump from _call_sc_creaturejump_5
    
    e "Come on!"
    call sc_creaturejump from _call_sc_creaturejump_6
    sv "A silent beat. Click twice to continue."
    c "..."
    
    show Eva determ
    e "WORK!"
    
    #Companion reaction to another zap
    if companion:
        if chosenPath == "Charlie":
            show Reception neutral
        
        elif chosenPath == "Pharmacy":
            show Pharma afraid
            
        else:
            show Proprio drill
    
    call sc_creaturejump from _call_sc_creaturejump_7
    sv "A silent beat. Click twice to continue."
    c "..."
    
    show Eva pensive
    e "Well, that's not going to work. Time for plan B!"
    
    call ms_end from _call_ms_end_14
    g "You have another idea?"
    
    return
    
