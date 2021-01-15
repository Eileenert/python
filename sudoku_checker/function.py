# ----------------------- sudoku_resolution.py 's function--------------------------------

# sudoku_resolution's data
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
background_color = "#000000"


def get_lists(number_var_list):
    """First we get the value of each variables

    We ll create 3 lists:
        number_position_list: this list has sub-lists for each large box (already create)
        row_list: this list has sub-lists for each row
        column_list: this list has sub-lists for each column
        """

    number_position_list = []
    # we get the value of each variables and put them in self.number_position_list
    for i in range(len(number_var_list)):
        list_big_case_data = []
        for j in range(len(number_var_list)):
            if number_var_list[i][j].get() == "":
                list_big_case_data.append(0)
            else:
                list_big_case_data.append(
                    int(number_var_list[i][j].get()))

        number_position_list.append(list_big_case_data)

    # lists with data for each large box, row or column
    large_box_list = number_position_list
    row_list = []
    column_list = []

    # inverse column and row in column_list1
    counter = 0
    column_list1 = []
    for i in range(len(number_position_list)):
        column_list1.append([])
        counter_index = 0

        for j in range(len(number_position_list)):
            column_list1[i].append(
                number_position_list[counter][counter_index])

            counter_index += 3
            if counter_index >= 9:
                counter_index -= 8

        counter += 3
        if counter >= 9:
            counter -= 8

    # Get a list sub-lists for each row and column
    counter_number = 0
    for i in range(len(number_position_list)):
        # to get a list for each row
        one_row = []
        # to get a list for each column
        one_column = []
        for j in range(3):
            x = j
            if i >= 3 and i < 6:
                x += 3
            elif i >= 6:
                x += 6

            for k in range(3):
                one_row.append(number_position_list[x][k + counter_number])
                one_column.append(column_list1[x][k + counter_number])

        row_list.append(one_row)
        column_list.append(one_column)
        counter_number += 3
        if counter_number >= 9:
            counter_number = 0

    return large_box_list, row_list, column_list


def check_if_error(large_box_list, row_list, column_list):
    """ Check if the grid as error
        we compare the len of 2 lists:
            a list without 0 and the set of the list without 0.
        Like that we can check if there are any double number
    """

    # True if there is an error
    error = False

    largeBox_list_without_0 = []
    row_list_without_0 = []
    column_list_without_0 = []

    if not error:
        # remove all 0 from the 3 lists, create set and compare len to verify if there are double number
        for i in range(len(large_box_list)):
            largeBox_list_without_0.append([])
            # remove 0 of large_box_list
            largeBox_list_without_0[i] = list(
                filter(lambda a: a != 0, large_box_list[i]))

            # compare len of largeBox_list_without_0 and is set
            if len(largeBox_list_without_0[i]) != len(set(largeBox_list_without_0[i])):
                error = True
                break

    if not error:
        for i in range(len(row_list)):
            row_list_without_0.append([])
            # remove 0 of row_list
            row_list_without_0[i] = list(filter(lambda a: a != 0, row_list[i]))

            # compare len of row_list_without_0 and is set
            if len(row_list_without_0[i]) != len(set(row_list_without_0[i])):
                error = True
                break

    if not error:
        for i in range(len(column_list)):
            column_list_without_0.append([])
            # remove 0 of column_list
            column_list_without_0[i] = list(
                filter(lambda a: a != 0, column_list[i]))

            if len(column_list_without_0[i]) != len(set(column_list_without_0[i])):
                error = True
                break

    return error


def is_finished(large_box_list):
    """check if the sudoku is complete"""

    finished = False

    for i in large_box_list:
        if sum(i) != 45:
            return finished

    finished = True
    return finished
