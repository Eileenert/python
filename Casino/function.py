# file with functions for ZCasino.py
from pathlib import Path
import os
import pickle
# ------------------------------------------------------------------------------------
# data variable
moneyAmount = "moneyAmount"

# ------------------------------------------------------------------------------------------
# recover the user and money


def recover_username():  # to reover the username
    username = input("\nType your name: ")
    # We put the first letter in upper case the others in lower case
    username = username.capitalize()
    # The username must be at least 3 characters minimum, number and letters exclusively
    if not username.isalnum() or len(username) < 3:
        print("\nThe username is not valid")
        recover_username()
    else:
        return username


def recover_money():
    path_money = Path(moneyAmount)
    if path_money.exists():  # the file exist
        # we get it back
        with path_money.open("rb") as mA:
            my_depickler = pickle.Unpickler(mA)
            money = my_depickler.load()
    else:  # The file doesn't exist
        money = {}

    return money

# ----------------------------------------------------------------------------------------


def chooseNumber():  # Bet a correct number
    global bet_number
    bet_number = input("Bet a number between 0 and 10: ")
    try:  # verify if the input is a valid number between 0 and 10
        bet_number = int(bet_number)
        if bet_number < 0 or 10 < bet_number:
            raise ValueError
    except ValueError:
        print("Please retry")
        chooseNumber()

    return bet_number
