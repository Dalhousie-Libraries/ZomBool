label bil_ending:

    call sc_black from _call_sc_black_6
    $persistent.ending_achieved = True
    titleCard "Conclusion"
    
    if lang == "english":
        "There were zombies around Évangeline's house."
        "We lost the {i}Friend Satellite 1002 Yay{/i} when she used it to knock out a zombie that was coming for me."
    else:
        "Il y avait des zombies attroupés autour de la maison d'Évangeline."
        "On a perdu l'{i}Ami Satellite 1002 Yay{/i} lorsqu'elle l'a utilisé pour assomer un zombie qui s'en venait m'attaquer."
    
    if victory >= 10:
        jump bil_end_best
    elif victory >=8 and victory <10:
        jump bil_end_good
    elif victory >=5 and victory <8:
        jump bil_end_okay
    else:
        jump bil_end_worst
        
    return
    
label bil_end_worst:
    
    if lang == "english":
        "One of the zombies scratched me. I don't know how long I have before I transform..."
        "Based on one of my printouts, we discovered that zombies are afraid of salt, and that's the reason they don't go into the ocean."
        "Évangeline insisted on trying out an experiment. She went outside to throw salt on the mob of zombies, and then made a salt circle around herself."
        "She's waiting for me outside...the spot where I got scratched is burning, so I think I'll join her soon."
        "My face is wet. It tastes a bit like salt."
        "I can't help but think that if I only understood boolean searching better..."
        if kitten:
            "and maybe spent more of my life hugging kittens..."
        "...maybe we would have managed to make a difference!"
        
        titleCard "Ending 1 of 4{vspace=30}Salty Tears"
        
    else:
        "Un zombie m'a donné une longue égratinure. Je ne sais pas combien de temps qu'il me reste avant ma transformation..."
        "Un des articles disait que les zombies ont peur du sel et c'est pour ça qu'ils refusent de s'aventurer dans la mer."
        "Évangeline a insisté pour faire un test. Elle est sortie jeter du sel sur un troupeau de zombie puis a fait un cercle en sel autour d'elle même."
        "Elle m'attend dehors...ma plaie brûle alors je crois que je vais bientôt la rejoindre."
        "Mon visage est mouillé. Ça goûte un peu le sel."
        "Je ne peux pas m'empêcher de penser que si seulement j'avais mieux compris la recherche booléenne..."
        if kitten:
            "et passer plus de temps sur les choses importantes, comme passer du temps avec des chatons..."
        "...peut-être qu'on aurait réussi à faire une différence!"
        
        titleCard "Fin 1 de 4{vspace=30}Verser des larmes salées"
    return

label bil_end_okay:
    
    if lang == "english":
        "The articles I've printed are not giving us much hope."
        "Sure, there are some good suggestions on how to better fight zombies."
        "Lots of clever tactics to attack, and some well-thought-out ways to defend ourselves."
        "But we'll have to take our time to slowly reduce their numbers."
        "We can't make any mistakes."
        "I don't know how much longer humans can keep up the fight if we just reinforce the number of enemies when we die."
        "I'm already so tired...but we have no other choice...because my research didn't reveal any other choices."
        if kitten:
            "I'm going to pet Évangeline's cat now, before I go out again. It's one of the only things that brings me a sense of peace now."
        
        titleCard "Ending 2 of 4{vspace=30}Eternal Struggle."
        
    else:
        "Les articles que j'ai imprimés ne nous donnent pas beaucoup d'espoirs."
        "Oui, les suggestions que j'ai trouvées vont nous permettre de combattre les zombies plus efficacement."
        "Il y a beaucoup de tactiques pour les attaquer et des bonnes façcons de se protéger."
        "Mais on va devoir prendre notre temps pour lentement réduire le nombre de zombies."
        "On ne peut pas se permettre de comettre des erreurs."
        "Je ne sais pas comment longtemps les humains peuvent continuer à se battre si on vient renflouer les rangs ennemis lorsqu'on perd."
        "Je me sens déjà tellement fatigué...mais on n'a pas d'autres choix...parce que ma recherche n'a pas révélé d'autres choix."
        if kitten:
            "Je vais flatter le minou d'Évangeline avant qu'on reparte dehors. Dernièerement, c'est une des seules choses qui me rend heureux."
        
        titleCard "Fin 2 de 4{vspace=30}Lutte éternelle"
    
    return
    
label bil_end_good:
    
    if lang == "english":
        "My research revealed that zombies are very sensitive to nature."
        "They rarely wander outside of cities, and they dislike plants."
        if kitten:
            "They might even be allergic to cat fur!"
        "We visited a florist to arm ourselves with flowers and we took apart Évangeline's lawn to better hide her door."
        "It's working! The zombies seem to freeze into place when we hit them directly with nature's fury."
        "There are no more zombies in our town. We've even liberated a path to the airport!"
        "We're going to teach our tactics to other cities."
        "I hope we manage to finish off the zombies before winter!"
        
        titleCard "Ending 3 of 4{vspace=30}Seeding hope"
        
    else:
        "Mes recherches ont révélé que les zombies sont très sensibles à la nature."
        "Ils s'aventurent rarement en dehors des villes et n'aiment pas les plantes."
        if kitten:
            "Ils sont peut-être même allergique au poil de chat!"
        "On est allé visiter un fleuriste pour s'armer de fleurs et on a tout défait le gazon d'Évangeline pour camoufler sa porte."
        "Ça a fonctionné! Les zombies semblent figer lorsqu'on les frappe directement avec le pouvoir de la nature."
        "Il ne reste plus de zombies dans notre ville. On a même accès à l'aéroport."
        "Nous allons répandre le message aux autres villes."
        "J'espère qu'on peut en finir avant qu'arrive l'hiver!"
        
        titleCard "Fin 3 de 4{vspace=30}Semer l'espoir"
    return
    
label bil_end_best:
    
    if lang == "english":
        "We built robots using the specifications provided in my search results."
        "They never get tired. Already, there are no more zombies in our town."
        "Évangeline had the idea to program some of the robots to build even more robots."
        "Soon, there will be more robots roaming the planet than zombies."
        "We wanted to help them fight, but the robots suggested we stay home and rest."
        if kitten:
            "They're so nice. It does feel good to be able to think about something else for a while. Spend lots of time snuggling with our kitties."
        else:
            "They're so nice. It does feel good to be able to think about something else for a while."
         
        titleCard "Ending 4 of 4{vspace=30}New allies!"
    
    else:
        "On a construit des robots en utilisant des spécifications obtenues par mes recherches."
        "Ils sont infatigables. Déjà il n'y a plus de zombies dans la ville."
        "Évangeline a eu l'idée de programmer certains robots pour qu'ils construisent d'autres robots."
        "Bientôt, il va y avoir plus de robots sur la planète que de zombies."
        "On voulait continuer à aider avec la lutte, mais les robots nous ont conseillés de rester chez nous pour qu'on puisse se reposer."
        if kitten:
            "Ils sont très gentils. Ça nous fait du bien de pouvoir se changer les idées. Passer beaucoup de temps avec nos minous."
        else:
            "Ils sont très gentils. Ça nous fait du bien de pouvoir se changer les idées."
         
        titleCard "Fin 4 de 4{vspace=30}Des nouveaux alliés!"
    return
    
label bil_credits:
        
        
    $game_lang = lang
    
    
    #Set scene for credits
    stop music fadeout 1
    call ms_end from _call_ms_end_4
    
    
    #Setup for background credits
    if lang == "english":
        $inL = 0
    else:
        $inL = 1
        
    $crS = ("{a=","}","{/a}")
    
    $crT = ["https://www.flickr.com/photos/nmoya/9889227654/", "Bakery in Lecce, Italy",
        "https://www.flickr.com/photos/nmoya/", "Nikolas Moya",
        "https://www.flickr.com/photos/annethelibrarian/7815875980/", "Cool tree shadows in the living room",
        "https://www.flickr.com/people/annethelibrarian/", "Anne Heathen",
        "https://www.flickr.com/photos/laurenmanning/2318943806/", "Classroom",
        "https://www.flickr.com/people/laurenmanning/", "Lauren Manning",
        "https://www.flickr.com/photos/ilamont/4297705965/", "Home office in converted closet",
        "http://www.in30minutes.com/", "In 30 Minutes Guides",
        "https://www.flickr.com/photos/shaneglobal/9493328567/", "Shane Global Group and Individual Reside",
        "https://www.flickr.com/people/shaneglobal/", "Shane Global Language Centres",
        "https://www.flickr.com/photos/roadsidepictures/3998508401/", "Skaggs Drug Store, 2003",
        "https://www.flickr.com/people/roadsidepictures/", "Roadsidepictures",
        "https://www.flickr.com/photos/i8ipod/12737288214/", "Sunset empty streets",
        "https://www.flickr.com/people/i8ipod/", "YLev",
        "https://www.flickr.com/photos/yewenyi/2898577300/", "Sydney",
        "https://www.flickr.com/people/yewenyi/e", "Yewenyi",
        "http://soundbible.com/1815-A-Tone.html", "A Tone Sound",
        "http://soundbible.com/1815-A-Tone.html", "His Self",
        "http://soundbible.com/2067-Blop.html#Blop%20Sound", "Blop",
        "http://soundbible.com/2067-Blop.html#Blop%20Sound", "Mark DiAngelo",
        "http://soundbible.com/1072-Busy-Signal.html", "Busy Signal Sound",
        "http://soundbible.com/1072-Busy-Signal.html", "Mike Koenig",
        "http://soundbible.com/105-Light-Bulb-Breaking.html", "Light Bulb Breaking Sound",
        "http://soundbible.com/105-Light-Bulb-Breaking.html", "Mike Koenig",
        "http://soundbible.com/1733-Spit-Splat.html", "Split Splat Sound",
        "http://soundbible.com/1733-Spit-Splat.html", "Mike Koenig",
        "http://www.newgrounds.com/audio/listen/541709", "End of War",
        "http://blueoceans.newgrounds.com/", "BlueOceans",
        "www.incompetech.com", "Kevin MacLeod"
        ]
    
    $crL = ((" by "," is licensed under ", "https://creativecommons.org/licenses/by/2.0/", "CC BY 2.0", "https://creativecommons.org/licenses/by-nc/2.0/", "CC BY-NC 2.0", "http://creativecommons.org/licenses/by/3.0/", "CC BY 3.0", "https://creativecommons.org/licenses/by-sa/3.0/", "CC BY-SA 3.0"),
        (" par ", " est sous la license "))
    

    #Background photo title text
    scene black with fade
    if lang == "english":
        titleCard "Credits"
    else:
        titleCard "Crédits"
        
    #Background photo title text
    scene black with fade

    show text "{size=+8}Julie Marcoux{/size}" at credit_text1 with moveintop
    
    show Librarian factorscale
    if lang == "english":
        "Executive producer, designer, music finder, kitten wrangler, programmer, art director: {b}Julie Marcoux{/b}"
    else:
        "Production, création, trouvaille de musique, domptage de minou, programmation, direction artistique: {b}Julie Marcoux{/b}"
    
    hide text
    
    show Librarian factorscale at credPos8 with move
    show Eva factorscale at credPos6 with moveinbottom
    show Pharma factorscale at credPos2 with moveinbottom
    show Creature factorscale at credPos4 with moveinbottom
    show Proprio factorscale at credPos7 with moveinbottom
    show Reception factorscale at credPos3 with moveinbottom
    show Employee factorscale at credPos1 with moveinbottom
    show Client factorscale at credPos5 with moveinbottom
    
    show text "{size=+8}Caroline Marcoux{/size}" at credit_text2 with moveinleft
    
    if lang == "english": 
        "Character art: {b}Caroline Marcoux{/b}."
    else:
        "Apparence des personnages: {b}Caroline Marcoux{/b}."
        
    hide text
    hide Creature with moveoutbottom
    hide Reception with moveoutbottom
    
    if lang == "english":
        "Special thanks for allowing us to borrow their likeness for character designs: {b}Pierre Goguen, Brandon Boone, Lindsay McNiff, Joyline Makani, 
         Sarah Stevenson, Julie Marcoux{/b}."
        "The characters might look like them, but they certainly don't act like them, thank goodness!"
    else:
        "Un merci spécial pour nous avoir laissé utiliser une photo d'eux pour l'apparence physique des personnages: {b}Pierre Goguen, Brandon Boone, Lindsay McNiff, Joyline Makani, 
         Sarah Stevenson, Julie Marcoux{/b}."
        "Heureusement, bien que le design des personnages est basé sur leur apparence, ils ne partagent pas les mêmes personalités!"
    

    #Background photo title text
    scene black with fade
    
    show image "bdParts_ground.jpg"
    show text "{size=+8}Jason Beaulieu{/size}" at credit_text3 with moveinleft
    
    if lang == "english":
        "Custom background art: {b}Jason Beaulieu{/b}."
    else:
        "Arrières-plans spéciaux: {b}Jason Beaulieu{/b}."
        
    #Background photo title text
    scene black
    if lang == "english":
        titleCard "Background Photos"
    else:
        titleCard "Photos d'arrière-plan"
    
    #Background photo credits
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][2] + crS[1] + crL[0][3] + crS[2]
    scene bg bakery
    '[superString].'
    
    scene bg creepyRoom
    with pixellate
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][2] + crS[1] + crL[0][3] + crS[2]
    '[superString].'
    
    scene bg classroom 
    with pixellate
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][2] + crS[1] + crL[0][3] + crS[2]
    '[superString].'
    
    scene bg creepyOffice
    with pixellate
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][2] + crS[1] + crL[0][3] + crS[2]
    '[superString].'

    scene bg receptionCharlie
    with pixellate
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][2] + crS[1] + crL[0][3] + crS[2]
    '[superString].'
    
    scene bg pharmacy
    with pixellate
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][4] + crS[1] + crL[0][5] + crS[2]
    '[superString].'

    scene bg street
    with pixellate
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][2] + crS[1] + crL[0][3] + crS[2]
    '[superString].'
    
    scene bg roomCharlie
    with pixellate
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][4] + crS[1] + crL[0][5] + crS[2]
    '[superString].'

    #Background photo title text
    scene black
    stop music fadeout 1
    if lang == "english":
        titleCard "Sounds"
    else:
        titleCard "Sons"
    
    show text "{size=+8}A Tone Sound!{/size}" at credit_text3 with moveinleft
    play sound "A_Tone.mp3"
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    show text "{size=+8}Blop!{/size}" at credit_text5 with moveinleft
    play sound "Blop.mp3"
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    show text "{size=+8}Busy Signal!{/size}" at credit_text3 with moveinleft
    play sound "Busy_Signal.mp3"
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    show text "{size=+8}Light Bulb Breaking Sound!{/size}" at credit_text5 with moveinleft
    play sound "Light_Bulb.mp3"
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    show text "{size=+8}Split Splat!{/size}" at credit_text3 with moveinleft
    play sound "Split_Splat.mp3"
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    #Background photo title text
    scene black
    if lang == "english":
        titleCard "Music"
    else:
        titleCard "Musique"
    
    call ms_end from _call_ms_end_5
    
    show Librarian smiling with moveinright:
        yalign 1.0
        choice:
            linear 1.0 xalign 0.5
        choice:
            linear 0.5 xalign 0.4
        choice:
            linear 1.0 xalign 0.4
        choice:
            linear 0.5 xalign 0.6
        choice:
            linear 1.0 xalign 0.6
        choice:
            linear 0.3 yalign 0.8
            linear 0.3 yalign 1.0
        choice:
            linear 0.5 yalign 0.7
            linear 0.3 yalign 1.0
        repeat
        
    $superString = '"' + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + '"' + crL[inL][0] + crS[0] + crT.pop(0) + crS[1] + crT.pop(0) + crS[2] + crL[inL][1] + crS[0] + crL[0][8] + crS[1] + crL[0][9] + crS[2]
    '[superString].'
    
    call ms_party from _call_ms_party_11
    
    show Eva mwahaha behind Librarian with moveinleft:
        yalign 1.0
        choice:
            linear 1.0 xalign 0.1
        choice:
            linear 0.5 xalign 0.3
        choice:
            linear 1.0 xalign 0.3
        choice:
            linear 0.5 xalign 0.2
        choice:
            linear 1.0 xalign 0.2
        choice:
            linear 1.0 xalign 0.5
        choice:
            linear 0.5 yalign 0.7
            linear 0.3 yalign 1.0
        repeat
            
    $superString = '"Enter the Party"' + crL[inL][0] + crS[0] + crT[0] + crS[1] + crT[1] + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    call ms_lithium from _call_ms_lithium_2
    
    show Reception stars behind Librarian with moveinright:
        yalign 1.0
        choice:
            linear 0.6 xalign 0.9
        choice:
            linear 0.5 xalign 0.7
        choice:
            linear 0.3 xalign 0.7
        choice:
            linear 0.6 xalign 0.8
        choice:
            linear 0.6 xalign 0.8
        choice:
            linear 0.6 xalign 0.2
        choice:
            linear 0.5 yalign 0.7
            linear 0.3 yalign 1.0
        repeat
    
    $superString = '"Lithium"' + crL[inL][0] + crS[0] + crT[0] + crS[1] + crT[1] + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    call ms_ossuary from _call_ms_ossuary_10
    
    hide Librarian
    hide Eva
    hide Reception
    
    show Employee determination with moveinleft:
        yalign 1.0
        choice:
            linear 1.0 xalign 0.5
        choice:
            linear 0.5 xalign 0.4
        choice:
            linear 1.0 xalign 0.4
        choice:
            linear 0.5 xalign 0.6
        choice:
            linear 1.0 xalign 0.6
        choice:
            linear 0.5 yalign 0.7
            linear 0.3 yalign 1.0
        repeat
    
    $superString = '"Ossuary 5 - Rest"' + crL[inL][0] + crS[0] + crT[0] + crS[1] + crT[1] + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'

    call ms_machine from _call_ms_machine_4
    
    show Proprio satisfaction behind Employee with moveinleft:
        yalign 1.0
        choice:
            linear 1.0 xalign 0.1
        choice:
            linear 0.5 xalign 0.3
        choice:
            linear 1.0 xalign 0.3
        choice:
            linear 0.5 xalign 0.2
        choice:
            linear 1.0 xalign 0.2
        choice:
            linear 1.0 xalign 0.5
        choice:
            linear 0.5 yalign 0.7
            linear 0.3 yalign 1.0
        repeat
    
    $superString = '"The Machine Thinks"' + crL[inL][0] + crS[0] + crT[0] + crS[1] + crT[1] + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'
    
    call ms_unpromised from _call_ms_unpromised
    
    show Client happy behind Employee with moveinright:
        yalign 1.0
        choice:
            linear 0.4 xalign 0.9
        choice:
            linear 0.5 xalign 0.7
        choice:
            linear 0.3 xalign 0.7
        choice:
            linear 0.6 xalign 0.8
        choice:
            linear 0.5 xalign 0.8
        choice:
            linear 0.4 xalign 0.2
        choice:
            linear 0.5 yalign 0.7
            linear 0.3 yalign 1.0
        repeat
    
    $superString = '"Unpromised"' + crL[inL][0] + crS[0] + crT[0] + crS[1] + crT[1] + crS[2] + crL[inL][1] + crS[0] + crL[0][6] + crS[1] + crL[0][7] + crS[2]
    '[superString].'

    
    #Background photo title text
    scene black
    stop music fadeout 1
    if lang == "english":
        titleCard "Special thanks to..."
    else:
        titleCard "Un merci spécial à..."
    
    call ms_end from _call_ms_end_6
    
    if lang == "english":
        show text "{size=+8}{b}A SPECIAL THANK YOU!{/b}{vspace=2}Playtesters:{vspace=2}Christine Cousins{vspace=2}Laura Little{vspace=2}Lindsay McNiff{vspace=2}Lindsay Warner{vspace=2}Lucy Kiester{vspace=2}Marlo MacKay{vspace=2}Pierre Goguen{/size}" at credit_text4 with moveintop
        "A special thank you goes to: my playtesters for their awesome suggestions: {b}Christine Cousins{/b}, {b}Laura Little{/b}, {b}Lindsay McNiff{/b}, {b}Lindsay Warner{/b}, {b}Lucy Kiester{/b}, {b}Marlo MacKay{/b}, and {b}Pierre Goguen{/b}."
    else:
        show text "{size=+8}{b}UN MERCI SPÉCIAL!{/b}{vspace=2}Testeurs{vspace=2}Christine Cousins{vspace=2}Laura Little{vspace=2}Lindsay McNiff{vspace=2}Lindsay Warner{vspace=2}Lucy Kiester{vspace=2}Marlo MacKay{vspace=2}Pierre Goguen{/size}" at credit_text4 with moveintop
        "Merci à: mes testeurs, pour les bonnes suggestions: {b}Christine Cousins{/b}, {b}Laura Little{/b}, {b}Lindsay McNiff{/b}, {b}Lindsay Warner{/b}, {b}Lucy Kiester{/b},{b}Marlo MacKay{/b}, et {b}Pierre Goguen{/b}."
    
    if lang == "english":
        show text "{size=+8}{b}A SPECIAL THANK YOU!{/b}{vspace=2}My lovely parents{vspace=2}Halifax transit buses{vspace=2}Pierre Goguen{vspace=2}Dalhousie University Libraries{/size}" at credit_text4 with moveintop
        "And a special thank you goes to: {b}my lovely parents{/b} for being lovely parents, the {b}Halifax transit buses{/b} for a smooth ride to work and back that gives me time to work on projects,  
         {b}Pierre Goguen{/b} for keeping this project secret for so long, and everyone at {b}Dalhousie University Libraries{/b} for their support."
    else:
        show text "{size=+8}{b}UN MERCI SPÉCIAL!{/b}{vspace=2}Mes supers parents{vspace=2}Le réseau d'autobus de Halifax{vspace=2}Pierre Goguen{vspace=2}Le réseau de bibliothèques de l'Université de Dalhousie{/size}" at credit_text4 with moveintop
        "Et merci à: {b}mes supers parents{/b} pour avoir été des supers parents, le {b}réseau d'autobus de Halifax{/b} qui me transporte au travail en douceur tout en me 
         laissant du temps pour travailler sur mes projets, {b}Pierre Goguen{/b} pour avoir gardé le secret tellement longtemps, 
         et tout le monde dans le {b}réseau de bibliothèques de Dalhousie{/b} pour leur support."
        
    hide text
        
    if lang == "english":
        titleCard "Created with Ren'py version 6.99.12.4."
    else:
        titleCard "Créé avec Ren'py version 6.99.12.4."
    
    #Thanks for playing
    scene black
    if lang == "english":
        titleCard "Thanks for playing!"
    else:
        titleCard "Merci d'avoir essayé ZomBool!"

    return