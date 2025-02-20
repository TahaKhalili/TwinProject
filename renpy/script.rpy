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
        text "Social Life [socialLife]"
screen fitnessDisplay():
    frame:
        xalign 0.05
        yalign 0.20
        text "Fitness [fitness]"

define j = Character("Jeremy", color = "#08f114")
define t = Character("Taha", color = "#ea0909")
define z = Character("Zach", color = "#3215ec")

# Variables
default cleanliness = 0
default academics = 0
default socialLife = 0
default fitness = 0


# The game starts here.

label start:

    show screen cleanlinessDisplay
    show screen academicsDisplay
    show screen socialLifeDisplay
    show screen fitnessDisplay
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show taha

    # These display lines of dialogue.

    j "You've created a new Ren'Py game."

    j "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "Helo Taha wash his dishes": 
            jump washDishes
        "Help Jeremy study for Orgo":
            jump studyOrgo

label washDishes:
    t "This is boring."
    $ cleanliness += 10


label studyOrgo:
    j "This is very confusing"
    # This ends the game.

    return
