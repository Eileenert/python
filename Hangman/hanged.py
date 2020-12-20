import data
import function as f

scores = f.recover_scores()  # we recover the scores of the game

user = f.recover_username()  # we recover the username

if user not in scores.keys():  # if the user don't have score, we add it
    scores[user] = 0  # 0 points for begin

continue_game = "y"  # our variable to know when to stop the game

while continue_game != "n":

    print(f"\nPlayer {user}: {scores[user]} point(s)")

    word_to_find = f.choose_word()
    letter_found = set()
    word_find = f.recover_hidden_word(word_to_find, letter_found)
    shot = data.nbr_shot

    while word_to_find != word_find and shot > 0:

        print(f"\nWord to find {word_find} ({shot} shot(s) left) ")
        letter = f.recover_letter()

        if letter in letter_found:  # the letter has already been choose
            print("\nYou have already found this letter")

        elif letter in word_to_find:  # The letter is in the word to find
            print("\nGood job!")

        else:
            shot -= 1
            print("\nThis letter is not in the word...")

        letter_found.add(letter)
        word_find = f.recover_hidden_word(word_to_find, letter_found)

    if word_to_find == word_find:
        print(f"\nCongratulations!!! You found the word {word_to_find}!")
        
    else:
        print(f"\nHanged...You lost. the word was {word_to_find}")

    scores[user] += shot  # we update the player's score

    continue_game = input("\nWould you like to continue the game? (y/n)")
    continue_game = continue_game.lower()

f.save_scores(scores)  # The game is finish we save the scores

print(f"\nYou finish the game with {scores[user]} points.")

