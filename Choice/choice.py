import os
from random import choice, randint, uniform
import pickle


def program():  # main program
    global redo
    redo = True

    def restart():  # Choose to restart or no
        global redo
        global yn
        yn = input("Restart? y/n :")
        if yn.lower() == "n":
            # Change the type
            change = input(
                "\nTo change the type write \"change\" else press enter to continue: ")
            if change.lower() == "change":
                program()
            else:  # Exit
                print("\n Bye")

                redo = False
        elif yn.lower() == "y":
            pass
        else:
            print('\nPlease enter "y" or "n" ')
            restart()

    def choose_type():  # Choose what we want to do
        print("""\nChoose the type :
            1.Reuse the same list(Create one, or take one already saved)
            2.Different list each time
            3.Random number \n""")

        global Type
        Type = input("Choose 1,2 or 3: ")

        try:
            Type = int(Type)
            if Type < 1 or 3 < Type:
                raise ValueError
        except ValueError:
            print("\n Error")
            choose_type()

    choose_type()

    if Type == 1:  # First thing we can do

        def display_randomly_list():  # display the items of the list choose below randomly
            print("\nNow an item will be choose randomly...")
            while redo:
                y = choice(dict_of_list[select])
                print(f"\n{y}\n")
                restart()

        def chooseTheList():
            global dict_of_list
            global dL
            global my_depickler
            try:
                with open("dictList", "rb") as dL:  # We get the dictionary
                    my_depickler = pickle.Unpickler(dL)
                    # The dictionary which will contain all the names of the lists we created and their items
                    dict_of_list = my_depickler.load()
                    dL.close()
            except:
                dict_of_list = {}

            # We choose if we want to create a new list or see the existants ones
            create_or_saved = input(
                '\nIf you want to create a list press "c", if you want to see the saved one press "s": ')

            if create_or_saved.lower() == "c":  # If the user press c
                global name
                # choose the name of the new list
                name = input(
                    "\nPlease enter the name of the list you want to create: ")
                name = name.lower()

                if name in dict_of_list:  # To be sure that an existing list does not have the same name to avoid errors
                    print("\nPlease enter a non-existent name")
                    chooseTheList()

                global listItems
                # We enter the list items
                listItems = input(
                    "\nPlease enter the items of the list separated by a comma \",\": ")
                listItems = listItems.split(",")

                # We show the user his list
                print(f"\nThe name of the list is {name} and the items are =")
                for x in listItems:
                    print(x)

                # We place the new list in he dictionary
                dict_of_list[name] = listItems

                global my_pickler
                with open("dictList", "wb") as dL:  # We save the new list in the dictionary
                    my_pickler = pickle.Pickler(dL)
                    my_pickler.dump(dict_of_list)
                    dL.close()

                global select
                select = name  # To use in the display_randomly_list() function
                display_randomly_list()

            elif create_or_saved.lower() == "s":  # If the user press s
                if len(dict_of_list) == 0:  # Check if their is somethong in the dictionary
                    print("\nThere is no list already saved")
                    chooseTheList()

                print("\nList saved: ")  # Show all the list available
                for x, y in dict_of_list.items():
                    print(x, "= ", y)

                # if the user want to modify the dictionary
                modify = input(
                    '\nIf you want to delete a list press "d" else press enter to choose the list: ')

                def delete_list():
                    if modify.lower() == "d":
                        global name_delete
                        name_delete = input(
                            "\nEnter the name of the list to delete: ")
                        if name_delete.lower() in dict_of_list:  # verify that the list exist
                            dict_of_list.pop(name_delete)  # delete the list

                            # We save the dictionary to remember we delete a list
                            with open("dictList", "wb") as dL:
                                my_pickler = pickle.Pickler(dL)
                                my_pickler.dump(dict_of_list)
                                dL.close()

                            print(f"{name_delete} has been delete")

                            if len(dict_of_list) == 0:  # check that there are still lists
                                print("\nTheir is no more list")
                                chooseTheList()

                            # if the user want to delete an other list
                            one_more = input(
                                'If you want to delete an other list press "o" else press enter: ')
                            if one_more.lower() == "o":
                                # Show all the list available
                                print("\nList saved: ")
                                for x, y in dict_of_list.items():
                                    print(x, "= ", y)
                                delete_list()

                        else:
                            print("\nPlease enter a correct name")
                            delete_list()

                delete_list()

                select = input("\nType the name of the list you want to use: ")
                if select.lower() in dict_of_list:  # verify that the list exist
                    display_randomly_list()
                else:
                    print("\n Please an existant name")
                    chooseTheList()

            else:
                print('\n Please enter "c" or "s"')
                chooseTheList()

        chooseTheList()

    elif Type == 2:  # Second thing we can do
        while redo:
            x = input(
                "\nWrite the different propositions separated by a comma \",\": ")
            x = x.split(",")
            y = choice(x)
            print(f"\n{y}\n")
            restart()
    elif Type == 3:  # Third thing we can do

        def random_number(randint_or_uniform):
            while redo:
                # Take a random number
                z = randint_or_uniform(number[0], number[1])
                print(f"\n{round(z, 3)}\n")
                restart()

        def number_between():
            # choose the type of number we want
            print("""\nDo you want           
                    1.whole number
                    2.decimal number""")

            global intOrFloat
            intOrFloat = input("\nChoose 1 or 2: ")

            try:  # To be sure the user type 1 or 2 and not something else
                intOrFloat = int(intOrFloat)
                if intOrFloat < 1 or 2 < intOrFloat:
                    raise ValueError

            except ValueError:
                print("\nPlease enter 1 or 2")
                number_between()

            def two_numbers():
                global number
                # Set the range of number
                number = input("\nChoose numbers (x,y): ")
                number = number.split(",")

                def convert():
                    if intOrFloat == 1:
                        try:  # convert the list string values into integers numbers
                            number[0] = int(number[0])
                            number[1] = int(number[1])
                            if len(number) != 2 or number[0] > number[1]:
                                raise Exception

                        except Exception:
                            print("\nPlease retry")
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
                            print("\nPlease retry")
                            two_numbers()

                        else:
                            random_number(uniform)

                convert()

            two_numbers()

        number_between()


program()
os.system("pause")
