import random
import data
# ---------------------------------game.py functions-----------------------------------------------


def new_game(grid_len):
    """make a board of the game and ask for the positions of the two 2"""
    board = []
    for i in range(grid_len):
        board.append([0] * grid_len)

    board = add_two(board)
    board = add_two(board)

    return board


def add_two(board):
    """add a 2 to the board"""
    a = random.randint(0, len(board) - 1)
    b = random.randint(0, len(board) - 1)

    #to be sure not to put a 2 on an already existing number
    while board[a][b] != 0:
        a = random.randint(0, len(board) - 1)
        b = random.randint(0, len(board) - 1)

    board[a][b] = 2
    return board


def game_stat(board):
    #check if a cell as a value of 2048
    for i in range(data.grid_len):
        for j in range(data.grid_len):
            if board[i][j] == 2048:
                return "win"

    # check for any zero entries
    for i in range(data.grid_len):
        for j in range(data.grid_len):
            if board[i][j] == 0:
                return "not over"

    # check for same cells that touch each other
    for i in range(data.grid_len - 1):
        for j in range(data.grid_len - 1):
            if board[i][j] == board[i + 1][j] or board[i][j] == board[i][j +
                                                                         1]:
                return "not over"

    return "lose"


def reverse(board):
    """
    example:
   [[0, 0, 0, 0],           [[0, 0, 0, 0], 
    [0, 0, 0, 2],   to ->    [2, 0, 0, 0], 
    [0, 2, 0, 2],            [2, 0, 2, 0],
    [0, 0, 0, 0]]            [0, 0, 0, 0]]
    """
    new_board = []

    for i in range(data.grid_len):
        new_board.append([])
        for j in range(data.grid_len):
            new_board[i].append(board[i][data.grid_len - j - 1])

    return new_board


def turn_board(board):
    """turn the board
    example:
   [[0, 0, 0, 0],           [[0, 0, 0, 0], 
    [0, 0, 0, 2],   to ->    [0, 0, 2, 0], 
    [0, 2, 0, 2],            [0, 0, 0, 0],
    [0, 0, 0, 0]]            [0, 2, 2, 0]]
    """
    new_board = []
    for i in range(data.grid_len):
        new_board.append([])
        for j in range(data.grid_len):
            new_board[i].append(board[j][i])

    return new_board


def swipe_number(board):
    """
    example:
    [[0, 0, 0, 0],              [[0, 0, 0, 0], 
     [0, 0, 2, 0],     to ->     [2, 0, 0, 0],
     [0, 0, 0, 0],               [0, 0, 0, 0],
     [0, 2, 2, 0]]               [2, 2, 0, 0]]
    """
    done = False
    new_board = []
    for i in range(data.grid_len):
        new_board.append([0] * 4)

    for i in range(data.grid_len):
        count = 0
        for j in range(data.grid_len):
            if board[i][j] != 0:
                new_board[i][count] = board[i][j]
                if j != count:
                    done = True
                count += 1

    return new_board, done


def merge(board, done):
    """
    example:
    [[0, 0, 0, 0],              [[0, 0, 0, 0], 
     [2, 0, 0, 0],     to ->     [2, 0, 0, 0],
     [0, 0, 0, 0],               [0, 0, 0, 0],
     [2, 2, 0, 0]]               [4, 0, 0, 0]]
    """

    for i in range(data.grid_len):
        for j in range(data.grid_len - 1):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
                done = True

    return board, done


def key_up_pressed(board):
    board = turn_board(board)
    board, done = swipe_number(board)
    board, done = merge(board, done)
    board = swipe_number(board)[0]
    board = turn_board(board)
    return board, done


def key_down_pressed(board):
    board = turn_board(board)
    board = reverse(board)
    board, done = swipe_number(board)
    board, done = merge(board, done)
    board = swipe_number(board)[0]
    board = reverse(board)
    board = turn_board(board)
    return board, done


def key_left_pressed(board):
    board, done = swipe_number(board)
    board, done = merge(board, done)
    board = swipe_number(board)[0]
    return board, done


def key_right_pressed(board):
    board = reverse(board)
    board, done = swipe_number(board)
    board, done = merge(board, done)
    board = swipe_number(board)[0]
    board = reverse(board)
    return board, done