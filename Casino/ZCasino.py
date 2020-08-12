import os
from random import randint
from math import ceil
import pickle


def new_game():
    global money
    global my_pickler
    global my_depickler
    global newGame
    global mA

    newGame=input("If you want to start a new game press \"n\" .To recover your previous game press \"p\": " )
    if newGame.lower()=="n":
        with open("moneyAmount","wb") as mA:
            my_pickler= pickle.Pickler(mA)
        money=1000
    elif newGame.lower()=="p":
        try:
            with open("moneyAmount", "rb") as mA:
                my_depickler= pickle.Unpickler(mA)
                money= my_depickler.load()
                print(money)
                mA.close()
        except:
            print("You don't have any previous game")
            new_game()
    else:
        print("Please enter \"n\" or \"p\"")
        new_game()
            

def rules():
    seeRules=input("Do you want to see the rules? (y/n): ")
    if seeRules.lower()== "y":
        print("""
A winning number between 1 and 10 will be drawn randomly.
If you have bet the same number as the winning number you win triple the amount wagered
otherwise if the two numbers are both even or odd (so the same color) the gain is 50% of the amount wagered. 
If this is not the case you lose your bet. 
""")
        new_game()
    elif seeRules.lower()== "n":
        new_game()
    else:
        print("Please enter y or n")
        rules()
    


rules()        


print(f"You sit at a table with {money}$")

while True:

    def chooseNumber():  # Bet a correct number
        global bet_number
        bet_number = input("Bet a number between 0 and 10: ")
        try:
            bet_number = int(bet_number)
            if bet_number < 0 or 10 < bet_number:
                raise ValueError
        except ValueError:
            print("Please retry")
            chooseNumber()

    chooseNumber()

    def chooseMoney():  # Bet a correct amount of money
        global bet_money
        bet_money = input(f"Choose an amount to bet, you have {money}$ : ")
        try:
            bet_money = int(bet_money)
            if bet_money <= 0 or money < bet_money:
                raise ValueError
        except ValueError:
            print("Put a correct amount of money")
            chooseMoney()

    chooseMoney()

    x = randint(0, 10)
    print(f"The random number is... {x}!")

    if x == bet_number:
        money += 3*bet_money
        print(f"Well done you won! Now you have {money}$")

    elif x % 2 == bet_number % 2:  # pair number, so same color
        bet_money = ceil(bet_money*0.5)
        print(f"You bet the right color, you get {bet_money}$.")
        money += bet_money

    else:
        print("Sorry it's not for this time you lose your bet")
        money -= bet_money

    if money <= 0:  # stop the partie if no money is left
        print("You're ruined it's the end of the game. This party will not be saved.")
        with open("moneyAmount","wb") as mA:
            my_pickler= pickle.Pickler(mA)
        break
    else:
        print(f"You have now {money}$")
        leave = input("Do you want to leave the game? (y/n): ")
        if leave.lower() == "y":
            print("Bye. This party will be saved.")
            with open("moneyAmount","wb") as mA:
                my_pickler= pickle.Pickler(mA)
                my_pickler.dump(money)
                mA.close()
            break

os.system("pause")
