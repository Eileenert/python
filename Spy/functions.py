from random import choice
import tkinter as tk

# list of different places
place = ["Parking", "Home", "Office", "Airport", "Bakery", "Bank", "Bar", "Bookstore", "Bus station", "Café", "Church", "Cinema", "Gym", "School", "Hospital",
         "Hotel", "Gallery", "Jail", "Library", "Mall", "Museum", "Pharmacy", "Police station", "Post office", "Park", "Restaurant", "Supermarket", "Zoo"]


rules= """\nEach in turn you are going to receive your role (one person at a time must see his role).
The villagers receive at the same time a location.. 
There are 2 spies among you, you must unmask them. 
The spies do not receive the location and must convince the villagers that they know the location to not be unmask.
When you are ready, you must each vote 2 people you think are the spies\n"""


# choose a place randomly
def random_place():
    thePlace = choice(place)
    return thePlace
