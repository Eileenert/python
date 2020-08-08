import os
from random import choice, randint, uniform

redo = True


def program():  # main program

    def restart():  # Choose to restart or no
        global yn
        yn = input("Restart? y/n : ")
        if yn.lower() == "n":
            # Change the type
            change = input(
                "To change the type write \"change\" else press enter to continue: ")
            if change.lower() == "change":
                program()
            else:  # Exit
                print("Bye")
                global redo
                redo = False

    def choose_type():  # Choose what we want to do
        print("""Choose the type :
            1.Reuse the same list
            2.Different list each time
            3.Random number \n""")

        global Type
        Type = input("Choose 1,2 or 3: ")

        try:
            Type = int(Type)
            if Type < 1 or 3 < Type:
                raise ValueError
        except ValueError:
            print("Error")
            choose_type()

    choose_type()

    if Type == 1:  # First thing we can do
        x = input("write the different propositions separated by a comma \",\": ")
        x = x.split(",")
        while redo:
            y = choice(x)
            print(y)
            restart()

    elif Type == 2:  # Second thing we can do
        while redo:
            x = input(
                "write the different propositions separated by a comma \",\": ")
            x = x.split(",")
            y = choice(x)
            print(y)
            restart()
    elif Type == 3:  # Third thing we can do

        def random_number(randint_or_uniform):
            while redo:
                # Take a random number
                z = randint_or_uniform(number[0], number[1])
                print(round(z, 3))
                restart()

        def number_between():
            # choose the type of number we want
            print("""Do you want           
                    1.whole number
                    2.decimal number""")

            global intOrFloat
            intOrFloat = input("Choose 1 or 2: ")

            try:  # To be sure the user type 1 or 2 and not something else
                intOrFloat = int(intOrFloat)
                if intOrFloat < 1 or 2 < intOrFloat:
                    raise ValueError

            except ValueError:
                print("Please enter 1 or 2")
                number_between()

            def two_numbers():
                global number
                # Set the range of number
                number = input("Choose numbers (x,y): ")
                number = number.split(",")

                def convert():
                    if intOrFloat == 1:
                        try:  # convert the list string values into integers numbers
                            number[0] = int(number[0])
                            number[1] = int(number[1])
                            if len(number) != 2 or number[0] > number[1]:
                                raise Exception

                        except Exception:
                            print("Please retry")
                            two_numbers()

                        else:
                            random_number(randint)

                    elif intOrFloat == 2:  # convert the list string values into floating numbers
                        try:
                            number[0] = float(number[0])
                            number[1] = float(number[1])
                            if len(number) != 2 or number[0] > number[1]:
                                raise Exception

                        except:
                            print("Please retry")
                            two_numbers()

                        else:
                            random_number(uniform)

                convert()

            two_numbers()

        number_between()


program()
os.system("pause")
