from random import shuffle

VALUES=["as","2","3","4","5","6","7","8","9","10","valet","lady","king"]      #usefull variable


SIGN=["spade","diamant","heart","clover"]
COLOR={
    "spade":"black",
    "clover":"black",
    "diamant":"red",
    "heart":"red",
}



class Card: #a card
    
    def __init__(self,values,sign):

        
        if values not in VALUES:
            raise ValueError (f"unknown value: {values}")       #To be sure it s a right value

        if sign not in SIGN:            #To be sure it s a right sign
            raise ValueError (f"unknown sign: {sign}")

        self.values= values     #values of the card
        self.sign= sign         #sign of the card
        
 
        
    def __repr__(self):         #representation of the object
        return f"<Card(values='{self.values}', sign='{self.sign}')"

    def __str__(self):          #string output with print
        return f"{self.values} of {self.sign}"

    def __eq__(self,b):
        if self.values==b.values and self.sign==b.sign:
            return True
        else:
            return False

    
    @property
    def color(self):        #color of the card
        return COLOR[self.sign] 


       

class Game52Cards:
    
    def __init__(self):
        self.cards=[]       #card package

        for sign in SIGN:       #fill up the package
            for values in VALUES:
                self.cards.append(Card(values,sign))
      


        
    def __str__(self):  #string output with print
        return ", ".join([str(card) for card in self.cards])

    def __repr__(self): #representation of the card package
        return f"{self.cards}" 

    def __contains__(self,card):        #behind the in function
        return card in self.cards

    def __getitem__(self,index):    #When we want to get an item
        return self.cards[index]

    def __len__(self):      #Return the number of cars in the package
        return len(self.cards)

    def mix(self):      #mix the cards
       shuffle(self.cards)

    def draw(self): #Pick a card
        if len(self.cards)==0:
            raise ValueError("The game as no more cards.")
        return self.cards.pop(0)


    def append(self,card):  #Add a Card to the game
        if card not in self.cards:  #Verify that the card is not in the package already
            self.cards.append(card)
        else:
            print(f"{card} is already in")


    def sort(self):
        n=[]    #temporary list
        for sign in SIGN:       
            for values in VALUES:
                if Card(values,sign) in self.cards: #verify that the card is in the package
                    n.append(Card(values,sign))     #add the card to the temporary list


        self.cards= n   #teh package take the temporary list which is ordered
        return self.cards

    def deleteAllCard(self):
        self.cards.clear()      #empties the list
        return self.cards

