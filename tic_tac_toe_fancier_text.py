from collections import deque
from pyfiglet import Figlet
# Due to the size of the classic tic-tac-toe board being 3x3, instead of using a variable for the size I've written the
# numbers directly. Other way to do it is by creating a "SIZE = 3" constant variable.


def green(text):
    return "\033[92m {}\033[00m" .format(text)


def yellow(text):
    return "\033[93m {}\033[00m" .format(text)


def red(text):
    return "\033[91m {}\033[00m" .format(text)


def cyan(text):
    return "\033[96m {}\033[00m" .format(text)


def purple(text):
    return "\033[95m {}\033[00m" .format(text)


def check_for_win():
    player_name, player_symbol = players[0].values()

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(3)])
    second_diagonal_win = all([board[i][3 - i - 1] == player_symbol for i in range(3)])

    row_win = any([all([el == player_symbol for el in row]) for row in board])
    col_win = any([all([board[r][c] == player_symbol for r in range(3)]) for c in range(3)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(purple(f"{player_name} won!"))

        exit()


def place_symbol(row, col):
    board[row][col] = players[0]["symbol"]

    check_for_win()
    print_board()

    if turns == 9:
        yellow("It's a draw!")
        exit()

    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0]['name']} choose a free position [1-9]: "))
            row, col = (position - 1) // 3, (position - 1) % 3
        except ValueError:
            print_select_a_valid_position_message()
            continue

        if 1 <= position <= 9 and board[row][col] == " ":
            turns += 1
            place_symbol(row, col)
        else:
            print_select_a_valid_position_message()


def print_select_a_valid_position_message():
    print(red(f"{players[0]['name']}, please select a valid position!"))


def print_board():
    [print(f"| {' | '.join(row)} |") for row in board]


def print_game_state():
    print("This is the numeration of the board: ")
    print_board()

    for row in range(3):
        for col in range(3):
            board[row][col] = " "


def start():

    f = Figlet(font='doom')
    print(f.renderText('Welcome to \nTic Tac Toe'))

    player_one_name = input(green("Player 1, enter your name: "))
    player_two_name = input(cyan("Player 2, enter your name: "))

    while True:
        player_one_symbol = input(f"{player_one_name}, would you like to play with X or O?: ").upper()

        if player_one_symbol not in ["X", "O"]:
            red(f"{player_one_name}, please select a valid option!")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append({"name": player_one_name, "symbol": player_one_symbol})
    players.append({"name": player_two_name, "symbol": player_two_symbol})

    print_game_state()
    choose_position()


turns = 0

board = [[str(r + c) for c in range(3)] for r in range(1, 10, 3)]
players = deque()

start()