#Evangeline standing in the middle of her house
label sc_evangeline:
    
    if lang == "english":
        sv "Évangeline stands in the middle of a creepy looking living room."
    else:
        sv "Évangeline est au milieu d'un salon. L'atmosphère est lourde."
    
    if companion:
        if lang == "english":
            sv "My recruit is also standing in the room."
        else:
            sv "Ma nouvelle recrue se trouve également dans la pièce."
        if chosenPath == "Charlie":
            scene bg creepyRoom
            show Reception neutral at credPos6
            show Eva pensive at credPos2
            with dissolve
        elif chosenPath == "Pharmacy":
            scene bg creepyRoom
            show Pharma relieved at credPos6
            show Eva pensive at credPos2
            with dissolve
        else:
            scene bg creepyRoom
            show Proprio satisfaction at credPos6
            show Eva pensive at credPos2
            with dissolve
    else:
        scene bg creepyRoom
        show Eva pensive
        with dissolve
    
    return
    
#Flashback to the house with Evangeline standing in the middle
label sc_evangeline_flash:
    
    if lang == "english":
        sv "I flash back to the creepy living room. Évangeline stands in the middle of the room."
    else:
        sv "Je pense de nouveau à Évangeline, debout dans le milieu de son salon épeurant."
    show bg creepyRoomFlashback
    show Eva flashback at center
    hide Reception
    with Fade(0.1, 0.0, 0.5, color="#fff")
    #show Reception happy:
        #alpha 0.5
    
    return

#In the middle of the house with no Evangeline
label sc_evangeline_alone:
    
    if lang == "english":
        sv "In a creepy living room."
    else:
        sv "Dans un salon. L'atmosphère est lourde."
    scene bg creepyRoom with dissolve
    
    return
    
#Office in Evangeline's home
label sc_office:
    
    if lang == "english":
        sv "In a tiny office in Évangeline's house."
    else:
        sv "Dans un petit bureau dans la maison d'Évangeline."
    scene bg creepyOffice with dissolve
    
    return

#Librarian standing in the middle of her classroom
label sc_class:
    
    if lang == "english":
        sv "The librarian stands in the front of a classroom filled with students."
    else:
        sv "La bibliothécaire est debout dans une salle de classe remplie d'étudiants."
    scene bg classroom 
    show Librarian neutral
    with dissolve
    
    return
    
#The reception of Charlie's building
label sc_Charlie_main:
    
    if lang == "english":
        sv "A receptionist stands behind the dorm's reception desk."
    else:
        sv "Un réceptionniste est debout derrière le bureau de réception."
        
    scene bg receptionCharlie
    show Reception neutral
    with dissolve
    
    return
    
#The corridor looking at Charlie's room
label sc_Charlie_corridor:
    
    if lang == "english":
        sv "In an empty corridor filled with doors leading to dorm rooms."
    else:
        sv "Dans un corridor vide remplit de portes menant vers des chambres." 
    scene bg roomCharlie with dissolve
    return

#The pharmacy - with pharmacist
label sc_pharm:
    
    if lang == "english":
        sv "A frightened looking pharmacist is behind the counter of a pharmacy."
    else:
        sv "Un pharmacien effrayé se tient derrière son comptoir."
    scene bg pharmacy
    show Pharma afraid
    with dissolve
    return

#The pharmacy - empty
label sc_pharm_vide:
    if lang == "english":
        sv "In a pharmacy. The shelves are bare."
    else:
        sv "Dans une pharmacie. Les étagères sont vides. "
    scene bg pharmacy with dissolve
    return

#The SportsGo lobby - empty
label sc_sportsGo_vide:
    
    if lang == "english":
        sv "In a sports store."
    else:
        sv "Dans un magasin de sports."
    scene bg sportsGo with dissolve
    return

#The SportsGo lobby - with owner
label sc_sportsGo:
    
    if lang == "english":
        sv "The unhappy looking owner of the sports store stands in front of me."
    else:
        sv "La propriétaire du magasin de sport se tient debout devant moi. Elle semble mécontente."
    scene bg sportsGo
    show Proprio unhappy
    with dissolve
    return

#Street background
label sc_street:
    if lang == "english":
        sv "I'm travelling on an empty street."
    else:
        sv "Je me promène sur une rue vide."
    scene bg street with dissolve
    return

#Librarian standing in the middle of a bakery
label sc_bakery:
    
    if lang == "english":
        sv "I imagine a bakery filled with delicious smells. The librarian stands to the side."
    else:
        sv "J'imagine une patisserie. La bibliothécaire se tient debout sur le côté."
        
    scene bg bakery with dissolve
    show Librarian neutral at right with moveinbottom
    return

#Just a black screen with no sound
label sc_black:
    
    if lang == "english":
        sv "A blank screen."
    else:
        sv "Un écran vide."
    scene black with dissolve
    
    return
    
label sc_creaturejump:
    
    if lang == "english":
        sv "The creature moves up and down."
    else:
        sv "La créature monte et descend."
    show Creature neutral with moveinbottom:
        #xalign 1.0
        linear 0.3 yalign 0.2
        linear 0.1 yalign 1.0
        repeat 1
    return
    
#Empty electronics store
label sc_electro:
    
    if lang == "english":
        sv "In an electronics store."
    else:
        sv "Dans un magasin qui vend de l'électronique."
    scene bg electro with dissolve
    
    return
    
#Used as background music for the prologue
label ms_lithium:
    
    stop music fadeout 1
    play music "Lithium.mp3" fadeout 1
    queue music "Lithium.mp3"
    
    return
    
#Used as background music for the prologue
label ms_lithium_fast:
    
    stop music fadeout 0.8
    play music "Lithium.mp3" fadeout 0.8
    queue music "Lithium.mp3"
    
    return

#Used as background music for the librarian
label ms_party:
    
    stop music fadeout 1
    play music "Enter the Party.mp3" fadeout 1
    queue music "Enter the Party.mp3"
    
    return
    
#Used as background music for important chapter transitions
label ms_end:
    
    stop music fadeout 1
    play music "End of War.mp3" fadeout 1
    queue music "End of War.mp3"
    
    return

#Used as background music for chapter 1
label ms_ossuary:
    
    stop music fadeout 1
    play music "Ossuary 5.mp3" fadeout 0.5
    queue music "Ossuary 5.mp3"
    
    return

#Used for Charlie's corridor
label ms_unpromised:
    
    stop music fadeout 1
    play music "unpromised.mp3" fadeout 1
    queue music "unpromised.mp3"
    
    return
    
#Main music for Chapter 2
label ms_machine:
    
    stop music fadeout 1
    play music "The Machine Thinks.mp3" fadeout 1
    queue music "The Machine Thinks.mp3"
    
    return
    
