# ----------------------functions for text_morse.py-----------------------------------


# function to choose if we convert text or morse
def enter_morse_or_text():

    while True:
        morse_or_text = input(
            "Press 'm' to write in morse or 't' to write in latin alphabet: ")

        if morse_or_text.lower() != "m" and morse_or_text.lower() != "t":
            print("Please enter 'm' or 't'")
        else:
            break

    return morse_or_text


# function to choose to translate or hear
def translate_or_hear():

    while True:
        t_o_h = input(
            "Press 't' to translate into latin alphabet or 'h' to hear it: ")

        if t_o_h.lower() != "t" and t_o_h.lower() != "h":
            print("Please enter 't' or 'h'")
        else:
            break

    return t_o_h
