# This file contains useful functions for the hangman game
import data
from random import choice
import pickle
from pathlib import Path
import os
os.chdir("c:/Users/Pink/Documents/Code/python/Hangman")


# score management


def recover_scores():
    path_scores = Path(data.name_file_scores)
    if path_scores.exists():  # the file exist
        # we get it back
        with path_scores.open("rb") as file_scores:
            my_depickler = pickle.Unpickler(file_scores)
            scores = my_depickler.load()
    else:  # The file doesn't exist
        scores = {}

    return scores


def save_scores(scores):
    """This function is responsible for recording the scores in the file name_file_scores 
    It receives in parameter the dictionary of the scores to be save."""

    with open(data.name_file_scores, "wb") as file_scores:  # we overwrite the old scores
        my_pickler = pickle.Pickler(file_scores)
        my_pickler.dump(scores)


# functions managing the elements entered by the user

def recover_username():  # to reover the username
    username = input("\nType your name: ")
    # We put the first letter in upper case the others in lower case
    username = username.capitalize()
    # The username must be at least 3 characters minimum, number and letters exclusively
    if not username.isalnum() or len(username) < 3:
        print("\nThe username is not valid")
        return recover_username
    else:
        return username


def recover_letter():
    letter = input("\nType a letter: ")
    letter.lower()
    if len(letter) > 1 or not letter.isalpha():  # check if its a valid letter
        print("\nPlease enter a valid letter")
        return recover_letter()
    else:
        return letter

# Functions Hangman Game


def choose_word():  # choose a word randomly
    return choice(data.list_words)


def recover_hidden_word(full_word, letter_found):
    # we return the original world with * for the letter we didn't found
    hidden_word = ""
    for letter in full_word:
        if letter in letter_found:
            hidden_word += letter
        else:
            hidden_word += "*"

    return hidden_word
