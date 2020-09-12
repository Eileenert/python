import os
import functions as f
from random import choice,shuffle
import tkinter as tk



def game():
    #decide to see the rules or not


    f.see_rules()

    #to know how many players there are
    numberPlayers=f.numberPlayers()

    #choose a random place
    thePlace=f.random_place()

    #number of villager and spies in the party
    villagers=numberPlayers - 2
    spies= 2

    #add the villagers
    vi=[]
    v=0
    while v<villagers:
        vi.append(f.villager(thePlace))
        v+=1

    #add the spies
    sp=[]
    s=0
    while s< spies:
        sp.append(f.spy())
        s+=1

    #put together villagers and spies
    visp= sp + vi
    shuffle(visp)   #mix the order

    #display the roles
    i=0
    while i<numberPlayers:
        root=tk.Tk()
        root.title("Role")
        a=visp.pop()
        input("\nPress enter or anything to see your card: \n")
        tk.Label(root, text=a).pack()
        tk.Button(root, text="ok", command=root.destroy).pack()
        root.mainloop()
        input("Press enter or anything to move on to the next player: ")
        
        i+=1


    def restart():
        rst= input("Restart Game? (y/n): ")
        if rst.lower()=="y":      
            game()
        elif rst.lower()=="n":
            pass
        else:       #if the user didn't choose y or n
            print("Please enter y or n")
            restart()

    restart()

game()




os.system("pause")