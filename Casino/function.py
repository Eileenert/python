# file with functions for ZCasino.py
import os
import pickle
import random
import unittest
from unittest import mock
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
    try:
        with open(moneyAmount, "rb") as mA:  # We get the dictionary
            my_depickler = pickle.Unpickler(mA)
            # The dictionary which will contain all the names of the lists we created and their items
            money = my_depickler.load()
            mA.close()
    except: # The file doesn't exist
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

#--------------------------unittest-----------------------------------------

class functionTest(unittest.TestCase):

    def test_chooseNumber(self):    # test the chooseNumber function

        #the differents input we can have (all are strings)
        numberBetween_0_10=str(random.randrange(0,11))  # a number between 0-10
        nbr_less_0= "-5"        #a number less than 0
        nbr_bigger_10 = "11"    #a number greater than 10
        not_a_number= "this is not a number"    #not a number

        with mock.patch('builtins.input', return_value= numberBetween_0_10 ):  
            assert chooseNumber() == int(numberBetween_0_10)

        with mock.patch('builtins.input', return_value= nbr_less_0 ):
            self.assertRaises(ValueError)

        with mock.patch('builtins.input', return_value= nbr_bigger_10 ):
            self.assertRaises(ValueError)
        
        with mock.patch('builtins.input', return_value= not_a_number ):
            self.assertRaises(ValueError)

unittest.main()