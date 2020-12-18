from random import shuffle, choice
import unittest

VALUES = ["as", "2", "3", "4", "5", "6", "7", "8", "9",
          "10", "valet", "lady", "king"]  # usefull variable


SIGN = ["spade", "diamant", "heart", "clover"]
COLOR = {
    "spade": "black",
    "clover": "black",
    "diamant": "red",
    "heart": "red",
}


class Card:  # a card

    def __init__(self, values, sign):

        if values not in VALUES:
            # To be sure it s a right value
            raise ValueError(f"unknown value: {values}")

        if sign not in SIGN:  # To be sure it s a right sign
            raise ValueError(f"unknown sign: {sign}")

        self.values = values  # values of the card
        self.sign = sign  # sign of the card

    def __repr__(self):  # representation of the object
        return f"<Card(values='{self.values}', sign='{self.sign}')"

    def __str__(self):  # string output with print
        return f"{self.values} of {self.sign}"

    def __eq__(self, b):
        if self.values == b.values and self.sign == b.sign:
            return True
        else:
            return False

    @property
    def color(self):  # color of the card
        return COLOR[self.sign]


class Game52Cards:

    def __init__(self):
        self.cards = []  # card package

        for sign in SIGN:  # fill up the package
            for values in VALUES:
                self.cards.append(Card(values, sign))

    def __str__(self):  # string output with print
        return ", ".join([str(card) for card in self.cards])

    def __repr__(self):  # representation of the card package
        return f"{self.cards}"

    def __contains__(self, card):  # behind the in function
        return card in self.cards

    def __getitem__(self, index):  # When we want to get an item
        return self.cards[index]

    def __len__(self):  # Return the number of cars in the package
        return len(self.cards)

    def mix(self):  # mix the cards
        shuffle(self.cards)

    def draw(self):  # Pick a card
        if len(self.cards) == 0:
            raise ValueError("The game as no more cards.")
        return self.cards.pop(0)

    def append(self, card):  # Add a Card to the game
        if card not in self.cards:  # Verify that the card is not in the package already
            self.cards.append(card)
        else:
            print(f"{card} is already in")

    def sort(self):
        n = []  # temporary list
        for sign in SIGN:
            for values in VALUES:
                if Card(values, sign) in self.cards:  # verify that the card is in the package
                    # add the card to the temporary list
                    n.append(Card(values, sign))

        self.cards = n  # teh package take the temporary list which is ordered
        return self.cards

    def deleteAllCard(self):
        self.cards.clear()  # empties the list
        return self.cards


# -----------------unittest---------------------------

class Game52CardsTest(unittest.TestCase):

    def setUp(self):
        #initialization of tests
        self.false_package = []
        for sign in SIGN:  # fill up the false package
            for values in VALUES:
                self.false_package.append(Card(values, sign))

        self.real_package = Game52Cards()

        self.card = Card(choice(VALUES), choice(SIGN))

    def test_mix(self):  # test the mix function
        self.real_package.mix()

        self.assertNotEqual(self.real_package, self.false_package)

        for card in self.real_package:
            self.assertIn(card, self.false_package)
            self.false_package.remove(card)

    def test_draw(self):  # test the draw function
        self.real_package.draw()
        self.false_package.pop(0)

        for card in self.real_package:
            self.assertEqual(card, self.false_package[0])
            self.false_package.pop(0)

    def test_append(self):  # test the append function
        self.real_package.cards.clear()  # empties real package
        # so the card is not in the package
        self.assertNotIn(self.card, self.real_package)
        self.real_package.append(self.card)  # we put the card in the package
        # we verify that the card is in the package
        self.assertIn(self.card, self.real_package)

    def test_sort(self):  # test the sort function
        shuffle(self.real_package.cards)
        self.real_package.sort()

        for card in self.real_package:
            self.assertEqual(card, self.false_package[0])
            self.false_package.pop(0)

    def test_deleteAllCard(self):
        self.real_package.deleteAllCard()
        self.assertEqual(len(self.real_package), 0)


# -----------------------------------------------------
