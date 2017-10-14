# Dragon Realm
# A game by Kamryn Figuerres
# 10/7/2017

# import stuff
import random
import time

# Show Introduction
def show_intro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on site.''')
    print()


def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    return cave


def when_friendly():
    print("You can either try to steal his treasure or you can befriend him.")
    print("To steal his treasure press t. To befriend press b.")
    decision = input()
    if decision == "t":
        print()
        print("The treasure is hidden behind one of three rocks in the cave.")
        time.sleep(1)
        treasure = random.randint(1, 3)
        print("Choose a number between 1-3 to see if the treasure is there.")
        number = input()
        if number == treasure:
            print()
            print("You found the treasure!")
        else:
            print()
            print("Wrong choice! The dragon got mad and ate you ):")
    else:
        print()
        print("You're friends with the dragon!")


def fire_breathing():
    print()
    print("You can still escape!")
    print("To move left press 1 and to move right press 2 to try to avoid the fire.")
    choice = input()
    fire = random.randint(1, 2)
    print()
    if choice == fire:
        print("You went the wrong way and got burned!")
    else:
        print("You did it! You escaped the dragon!")


def check_cave(cave_chosen):
    print("You approach the cave slowly...")
    time.sleep(2)
    print("You go inside the cave and see...")
    print()
    time.sleep(2)

    friendly_dragon = random.randint(1, 2)

    if cave_chosen == str(friendly_dragon):
        print("A friendly dragon!")
        print()
        when_friendly()
        
    else:
        print("A fire breathing dragon who wants to eat you!")
        fire_breathing()

    


def play():
    stillPlaying = True
    while stillPlaying:
        show_intro()
        cave = choose_cave()
        check_cave(cave)
        print("Would you like to play again? (y to continue, q to quit)")
        choice = input()
        if choice == "q":
            stillPlaying = False
        

# Play the game!
play()
print("Thanks for playing dude!")




