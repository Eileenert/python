import os
from random import choice,randint,uniform


def program(): #main program

    try:    
        def choose_type():    #Choose what we want to do
            print("""Choose the type :
            1.Reuse the same list
            2.Different list each time
            3.Random number \n""")

            global Type
            Type= int(input("Choose 1,2 or 3: "))


        choose_type()
        
    except:
        print("Error")
        program()
    else:

        if Type==1:             #First thing we can do
            x=input("write the different propositions separated by a comma \",\": ")
            x=x.split(",")
            while True:
                y=choice(x)
                print(y)
                yn= input("Restart? y/n : ")   #Choose to restart or no
                if yn=="n":
                    change=input("To change the type write \"change\" else press enter to continue: ")
                    if change=="change":
                        program()
                    else:
                        print("Bye")
                        break
        elif Type==2:       #Second thing we can do
            while True:
                x=input("write the different propositions separated by a comma \",\": ")
                x=x.split(",")
                y=choice(x)
                print(y)
                yn= input("Restart? y/n : ")   #Choose to restart or no
                if yn=="n":
                    change=input("To change the type write \"change\" else press enter to continue: ")
                    if change=="change":
                        program()
                    else:
                        print("Bye")
                        break
        elif Type==3:            #Third thing we can do

            
            def random_number(randint_or_uniform):       
                if len(number)!=2 :         #to be sure the user choose only two numbers
                    print("incorrect scheme")
                    number_between()
                elif number[0]> number[1]:         #to be sure the user put the smaller number in front
                    print("The first number is greater than the second!")
                    number_between()
                else:
                    while True:
                        z=randint_or_uniform(number[0],number[1]) #Take a random number
                        print(round(z, 3))
                        yn= input("Restart? y/n : ")   #Choose to restart or no
                        if yn=="n":
                            change=input("To change the type write \"change\" else press enter to continue: ")
                            if change=="change":
                                program()
                            else:
                                print("Bye")
                                break


            def number_between():
                #choose the type of number we want
                print("""Do you want           
                    1.whole number
                    2.number to decimal""")

                try:            #To be sure the user type 1 or 2 and not something else
                    global intOrFloat
                    intOrFloat=int(input("Choose 1 or 2: "))
                    if intOrFloat != 1 and intOrFloat != 2:
                        print("Please enter 1 or 2")
                        number_between()

                except:
                    print("Please enter 1 or 2")
                    number_between()
                else:
                    global number
                    number= input("Choose numbers (x,y): ")        #Set the range of number
                    number=number.split(",")


                    if intOrFloat==1:
                        try:                #convert the list string values into integers numbers
                            number[0]= int(number[0])
                            number[1]= int(number[1])

                        except:
                            print("Please retry")
                            number_between()

                        else:
                            random_number(randint)

                    elif intOrFloat==2:     #convert the list string values into floating numbers
                        try:
                            number[0]= float(number[0])
                            number[1]= float(number[1])

                        except:
                            print("Please retry")
                            number_between()

                        else:
                            random_number(uniform)
               
                
          

    
               
            number_between()


        else:
            print("\nError, write 1,2 or 3")
            program()



program()
os.system("pause")

