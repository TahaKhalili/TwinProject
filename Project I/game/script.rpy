# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

screen cleanlinessDisplay():
    frame:
        xalign 0.05
        yalign 0.05
        text "Cleanliness: [cleanliness]"
screen academicsDisplay():
    frame:
        xalign 0.05
        yalign 0.10
        text "Academics: [academics]"
screen socialLifeDisplay():
    frame:
        xalign 0.05
        yalign 0.15
        text "Social Life: [socialLife]"
screen fitnessDisplay():
    frame:
        xalign 0.05
        yalign 0.20
        text "Fitness: [fitness]"

define j = Character("Jeremy", color = "#08f114")
define t = Character("Taha", color = "#ea0909")
define z = Character("Zach", color = "#3215ec")

# Variables
default cleanliness = 5
default academics = 8
default socialLife = 4
default fitness = 6


# The game starts here.

label start:
    show screen cleanlinessDisplay
    show screen academicsDisplay
    show screen socialLifeDisplay
    show screen fitnessDisplay
    play music "music.mp3" loop
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "You enter the dorm room. This is the address you were given. The Nourse triple with their residents needing help for manage college life."

    show zach

    # These display lines of dialogue.

    z "YOOO welcome to our room, friend. I'm Zach. I play tennis and like to chill in the room."

    z "We've been off of our schedules and had been procrastinating a lot. We need help with our room's cleanliness, our academic work, our social life with friends, and our bodily and mental health."

    z "But first, I'll introduce you to my two roommates, Taha and Jeremy!"

    menu:
        "Meet Taha (+ bonous for fitness activities)":
            jump tahaIntro
        "Meet Jeremy ( + bonous for social life activities)":
            jump jeremyIntro

label tahaIntro:
    hide zach
    show taha
    t "Hey what's up! I'm Taha. I go to gym and like to play video games."
    t "I have been trying to bake some cookies and made a mess in the kitchen and lots of unwashed dishes. But I also have to catch lunch with my friends right about now."
    menu:
        "Tell him to wash the dishes first":
            $ cleanliness += 2
            jump kitchen
        "Tell him to catch lunch, dishes can wait":
            $ socialLife += 2
            $ cleanliness -= 1
            jump diningHall

label kitchen:
    scene kitchen
    show taha
    t "This is very boring..."
    t "But at least I won't get scolded by my RA for unwashed dishes. Let's go back and see who's in the room now."
    jump backToRoom1
    
label diningHall:
    scene dining hall
    show taha
    t "I'm so glad we came here! I get to see my friend Feraidon. He has been very busy these few weeks."
    t "By the way, I plan to head the gym after lunch. You should come too. But I should probably do some homework."
    menu:
        "Go to gym with Taha":
            $ fitness += 3
            $ academics -= 2
            jump gym1
        "Go back to the room":
            jump backToRoom1

label gym1:
    scene gym
    show taha
    t "This was a great workout. We should do this more often!"
    t "OK, we really have to go back to my room. I need to shower and catch up on homework!"
    jump backToRoom1


label jeremyIntro:
    hide zach
    show jeremy
    j "Hi my name is Jeremy. I like to hoop and hangout with friends."
    j "I have been studying a lot for my Orgo class but I feel like I could spend more time and do better. Otherwise I could go to Rec center to play basketball with my friend Theo."
    menu:
        "Help Jeremy study for Orgo":
            $ academics += 2
            jump orgoStudy
        "Go to basketball court with Jeremy":
            $ academics -= 2
            $ fitness += 1
            jump basketball

    # This ends the game.

label orgoStudy:
    show jeremy
    j "'Three hours later...'"
    j "Oh wow...This makes a lot more sense. Thank you so much."
    jump backToRoom1

label basketball:
    scene basketball
    show jeremy
    j "This was really fun. I got to catch up with my friend and feel much better."
    j "But not this Orgo work will haunt me even more. Anyways, I think I want to go visit Marcus and Christian in their dorm, see what they're up to and catch up."
    j "I will be back to the room after!"
    menu:
        "Go socialize with Jeremy's friends and go back to the room":
            $ socialLife += 3
            $ academics -= 2
            jump backToRoom1
        "Force Jeremy to go back to his room, it's about time he studied.":
            jump backToRoom1

label backToRoom1:
    scene room
    show jeremy:
        xalign 0.1
        yalign 0.99
    show zach
    show taha:
        xalign 0.9
        yalign 0.99
    j "It's Friday!!! As much as I would like to just have fun, let's plan our weekend smartly."
    menu:
        "Focus on studies":
            $ academics += 2
            $ socialLife -= 1
            jump study_session
        "Send them to workout":
            $ fitness += 2
            $ academics -= 1
            jump gym_session
        "Group cleaning session":
            $ cleanliness += 2
            $ fitness -= 1
            jump cleaning_session
        "Hangout with friends":
            $ socialLife += 2
            $ cleanliness -= 1
            jump social_session

label study_session:
    scene library
    show jeremy:
        xalign 0.1
        yalign 0.99
    show zach
    show taha:
        xalign 0.9
        yalign 0.99
    "The roommates spend the weekend buried in books, working hard on assignments"
    "Jeremy feels more confident for Orgo, but everyone is exhausted"

label gym_session:
    scene gym
    show jeremy:
        xalign 0.1
        yalign 0.99
    show zach
    show taha:
        xalign 0.9
        yalign 0.99
    "The roommates push themselives through intense workouts, feeling stronger and healthier"
    "However, Zach forgot about an important deadline, causing some stress"

label cleaning_session:
    scene room
    show jeremy:
        xalign 0.1
        yalign 0.99
    show zach
    show taha:
        xalign 0.9
        yalign 0.99
    "The dorm has never looked better! Everyone feels refreshed in the clean environment"
    "However, Taha regrets not hitting the gym"

label social_session:
    scene frat
    show jeremy:
        xalign 0.1
        yalign 0.99
    show zach
    show taha:
        xalign 0.9
        yalign 0.99
    "You all have a great time catching up with friends, making memories"
    "However, Jeremy realizes he barely touched his homework"
    return
