import alphabet as a
import functions as f
import winsound
import time


text = ""  # text variable
morse = ""  # morse variable


# ---------------conversion----------------------

# International text into international morse code
def text_to_international_morse():
    global text
    text2 = []

    # find the morse letter corresponding to the letter of the text
    for letter in text:
        if letter in a.international_morse:
            letter = a.international_morse[letter]

        if letter == " ":
            letter = ""
        # add th morse letter to a list
        text2.append(letter)

    # join the list into a sting
    text = " ".join([str(elem) for elem in text2])
    return text


def international_morse_to_text():

    global morse
    morse2 = []

    for letter in morse:
        # to be sure to have the same characters
        letter = letter.replace("·", ".")
        # to be sure to have the same characters
        letter = letter.replace("−", "-")

        for new_letter, old_letter in a.international_morse.items():
            if letter == old_letter:
                letter = new_letter
                break

        # to preserve the space between words
        if letter == "":
            letter = " "

        # add the text letter into a list
        morse2.append(letter)

    # join the list into a string
    morse = "".join([str(elem) for elem in morse2])

    return morse


# hear the morse (beep sound)
def hear_morse():
    global text
    while True:
        # ask to hear or not
        hear_yn = input("Do you want to hear it? y/n: ")

        # if yes to hear the sound
        if hear_yn.lower() == "y":

            while True:

                for characters in text:
                    # long sounds
                    if characters == "-":
                        winsound.Beep(2000, 375)
                    # short sounds
                    elif characters == ".":
                        winsound.Beep(2000, 150)
                    # between words
                    else:
                        time.sleep(0.1)

                #hear the sound again?
                redo=input("Do you want to hear it again? y/n:")
                
                #we hear the sound again
                if redo.lower()=="y":
                    pass
                #we don't hear the sound again
                elif redo.lower()=="n":
                    break
                else:
                    break

            break

        # if we don't want to hear it
        elif hear_yn.lower() == "n":
            break

        else:
            break


# ------------------------------main------------------------------

while True:


    morse_or_text = f.enter_morse_or_text()  # choose to translate morse or text


    # if we choose to translate text into morse
    if morse_or_text == "t":

        # text to convert into morse
        text = input("Please enter your text to convert: ")
        text = text.upper()

        # convert text to morse
        text_to_international_morse()

        text = text.lower()
        print(f"\n {text} \n")

        # ask to hear the text or not
        hear_morse()


    # if we choose to translate morse into text
    elif morse_or_text == "m":

        morse = input("Please enter the morse to convert: ")
        translate_or_hear = f.translate_or_hear()

        # to translate morse into text
        if translate_or_hear == "t":

            morse = morse.split(" ")

            # covert morse to text
            international_morse_to_text()

            print(f"\n {morse} \n")

        # hear morse
        elif translate_or_hear == "h":
            while True:
                for characters in morse:
                    # long sounds
                    if characters == "-":
                        winsound.Beep(2000, 375)
                    # short sounds
                    elif characters == ".":
                        winsound.Beep(2000, 150)
                    # between words
                    else:
                        time.sleep(0.09)

                
                redo=input("Do you want to hear it again? y/n: ")
                    
                #we hear the sound again
                if redo.lower()=="y":
                    pass
                #we don't hear the sound again
                elif redo.lower()=="n":
                    break
                else:
                    break


    #quit or not
    again = input("\nquit? y/n: ")

    #don't quit
    if again.lower() == "n":
        pass
    #quit
    elif again.lower() == "y":
        print("bye")
        break

    else:
        print("bye")
        break
