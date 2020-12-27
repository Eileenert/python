import functions as f
import random
import tkinter as tk


class Interface(tk.Frame):

    """main window"""

    def __init__(self, window, **kwargs):
        tk.Frame.__init__(self, window, width=750, height=575, **kwargs)
        self.pack(fill=tk.BOTH)

        self.place = f.random_place()  # the place

        self.players_number = 0  # number of players
        self.spies = 0  # number of spies
        self.villager = 0  # number of villager
        self.spies_or_villager = ""  # if the player is a spy or a villager

        # ask if we want to see the rules
        self.message = tk.Label(self, text="Do you want to see the rules")
        self.message.pack()

        self.no_button = tk.Button(  # no button
            self, text="No", fg="red", command=self.nbr_player)
        self.no_button.pack(side="left")

        self.yes_button = tk.Button(  # yes button
            self, text="Yes", fg="green", command=self.display_rules)
        self.yes_button.pack(side="right")

        self.next_button = tk.Button(  # next button
            self, text="Next", fg="red", command=self.nbr_player)

        self.var_text_entry = tk.StringVar()  # variable with entry_line text
        self.entry_line = tk.Entry(
            self, textvariable=self.var_text_entry)  # entry line

        # enter button
        self.enter_button = tk.Button(
            self, text="Enter", fg="red", command=self.verify_nbr_player)

        # next player button
        self.next_player_button = tk.Button(
            self, text="Next Player", fg="blue", command=self.next_player)
        self.text_or_white = "text"

        self.number_of_card = 0

    def display_rules(self):
        """If we click on the Yes button to see the rules"""

        self.message["text"] = f.rules  # modify the text
        self.no_button.pack_forget()  # remove button no
        self.yes_button.pack_forget()  # remove button yes

        self.next_button.pack()  # add the next button

    def nbr_player(self):
        """ If next_button or no_button is clicked

        We enter the number of player 
        """

        self.next_button.pack_forget()  # remove button next
        self.yes_button.pack_forget()  # remove button yes
        self.no_button.pack_forget()  # remove button no

        # modify the text
        self.message["text"] = "Please enter the number of players"
        self.entry_line.pack()  # add an entry line
        self.enter_button.pack(side="bottom")  # add a enter button

    def verify_nbr_player(self):
        """We verify that the number of player is correct"""
        try:
            self.players_number = int(self.var_text_entry.get())

            if self.players_number <= 3:  # verify the number of players
                raise ValueError

        except ValueError:
            self.message["text"] = "You must be at least 4 to play \nPlease enter a correct number"

        else:
            self.game()

    def game(self):
        self.entry_line.pack_forget()   # remove entry_line
        self.enter_button.pack_forget()  # remove enter button

        self.message["text"] = ""
        self.next_player_button.pack()

    def next_player(self):

        if self.number_of_card == self.players_number:
            self.destroy()

        # choose if the player is a spy or a villager
        if self.spies != 2 and self.villager != self.players_number-2:
            self.spies_or_villager = random.choice(["villager", "spy"])

        # there can only be 2 spies
        elif self.spies == 2:
            self.spies_or_villager = "villager"

        # the number of villagers is limited to the number of players minus the two spies
        elif self.villager == self.players_number-2:
            self.spies_or_villager = "spy"

        # choose between a white card or role
        if self.text_or_white == "white":
            self.message["text"] = ""
            self.text_or_white = "text"

        elif self.text_or_white == "text":

            # if the player is a villager we display his card and place
            if self.spies_or_villager == "villager":
                self.message["text"] = f"{self.place} \nYou are a villager \n"
                self.villager += 1

            # if the player is a spy we display his card
            elif self.spies_or_villager == "spy":
                self.message["text"] = f"\nYou are a spy \n"
                self.spies += 1

            self.text_or_white = "white"

            self.number_of_card += 1


if __name__ == '__main__':
    # we create our interface
    window = tk.Tk()

    window.geometry('700x300')
    window.resizable(0, 0)

    interface = Interface(window)

    interface.mainloop()
    interface.destroy()
