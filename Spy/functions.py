from random import choice
import os


#list of different places
place=["Parking","Home","Office","Airport","Bakery","Bank","Bar","Bookstore","Bus station","Café","Church","Cinema","Gym","School","Hospital","Hotel","Gallery","Jail","Library","Mall","Museum","Pharmacy","Police station","Post office","Park","Restaurant","Supermarket","Zoo"]


def see_rules():
    rules=input("Do you want to see the rules? (y/n): ")
    if rules.lower()=="y":      
        #rules
        print("""\nEach in turn you are going to receive your role (one person at a time must watch his role).
The villagers receive at the same time the place, which is the same for each one. 
There are 2 spies among you, you must unmask them. 
The spies do not receive the location and must convince the villagers that they know the location to not be unmask.
When you are ready, you must each vote 2 people you think are the spies\n""")
    elif rules.lower()=="n":
        pass
    else:       #if the user didn't choose y or n
        print("Please enter y or n")
        see_rules()




#choose the number of players
def numberPlayers():
    global nbr_players
    nbr_players=input("Please enter the number of players: ")   
    try:
        nbr_players= int(nbr_players)   #convert str into int

        if nbr_players<=3:  #verify the number of players
            print("You must be at least 4 to play")
            raise ValueError

    except ValueError:
        print("Please enter a correct number")
        numberPlayers()




    return nbr_players

#choose a lace randomly
def random_place():
    thePlace= choice(place)
    return thePlace

#spy person
def spy():
    return f"\nYou are a spy \n"

#villager person
def villager(thePlace):
    return f"{thePlace} \nYou are a villager \n"

