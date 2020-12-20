from random import randint
from math import ceil
import pickle
import function as f

def rules():  # rules
    seeRules = input("\nDo you want to see the rules? (y/n): ")
    if seeRules.lower() == "y":
        print("""\n
A winning number between 1 and 10 will be drawn randomly.
If you have bet the same number as the winning number you win triple the amount wagered
otherwise if the two numbers are both even or odd (so the same color) the gain is 50% of the amount wagered. 
If this is not the case you lose your bet. 
""")

    elif seeRules.lower() == "n":
        pass
    else:
        print("\nPlease enter y or n")
        rules()


rules()

user = f.recover_username()

money = f.recover_money()


if user not in money.keys():  # if the user don't have money, we add it
    money[user] = 1000  # 1000$ for begin


print(f"\nYou sit at a table with {money[user]}$")  # situation

while True:

    chooseNumber = f.chooseNumber()

    def chooseMoney():  # Bet a correct amount of money
        global bet_money
        bet_money = input(
            f"\nChoose an amount to bet, you have {money[user]}$ : ")
        try:  # verify that the input is a correct amount of money
            bet_money = int(bet_money)
            if bet_money <= 0 or money[user] < bet_money:
                raise ValueError
        except ValueError:
            print("\nPut a correct amount of money")
            chooseMoney()

    chooseMoney()

    x = randint(0, 10)
    print(f"\nThe random number is... {x}!")

    if x == f.bet_number:  # if the winning number is the same as the number bet
        money[user] += 3*bet_money
        print(f"\nWell done you won! Now you have {money[user]}$")

    elif x % 2 == f.bet_number % 2:  # pair number, so same color
        bet_money = ceil(bet_money*0.5)
        print(f"\nYou bet the right color, you get {bet_money}$.")
        money[user] += bet_money

    else:
        print("\nSorry it's not for this time you lose your bet")
        money[user] -= bet_money

    if money[user] <= 0:  # stop the partie if no money is left
        print("\nYou're ruined it's the end of the game.")
        money.pop(user)
        with open("moneyAmount", "wb") as mA:
            my_pickler = pickle.Pickler(mA)
            my_pickler.dump(money)
            mA.close()
        break
    else:  # choose to live or not
        print(f"\nYou have now {money[user]}$")
        leave = input("\nDo you want to leave the game? (y/n): ")
        if leave.lower() == "y":
            print("\nBye. This party will be saved.")
            with open("moneyAmount", "wb") as mA:  # saved the party
                my_pickler = pickle.Pickler(mA)
                my_pickler.dump(money)
                mA.close()
            break

