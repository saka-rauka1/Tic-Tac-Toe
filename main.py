import os

# The 3x3 board is represented by a dict with 9 keys, which mimic the numpad on a keyboard. For example: top left is 7
# and center is 5. The borders of the board are added by the draw_board() function.
GRID_VALUES = {
    "1": " ",
    "2": " ",
    "3": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "7": " ",
    "8": " ",
    "9": " ",
}


def main_menu():
    clear()
    in_menu = True
    while in_menu:
        print("Welcome to Tic Tac Toe\n")
        print("1. Player vs Player\n"
              "2. Player vs Computer (Coming Soon)\n"
              "3. Read the Rules\n"
              "4. Exit")
        menu_choice = input("Please pick from the above options: ")
        if menu_choice == "1":
            while True:
                sign_choice = input("Will the first player be represented by 'X' or 'O'?: ").upper()
                if sign_choice == "X":
                    first_player_sign = "X"
                    second_player_sign = "O"
                    break
                elif sign_choice == "O":
                    first_player_sign = "O"
                    second_player_sign = "X"
                    break
            play_game(first_player_sign, second_player_sign)
            clear()
        elif menu_choice == "2":
            clear()
            print("Coming Soon")
            input("Press any key to continue: ")
            return main_menu()
        elif menu_choice == "3":
            return print_rules()
        elif menu_choice == "4":
            clear()
            print("Goodbye!")
            return
        else:
            clear()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
    clear()
    print("Placeholder")
    input("Press any key to continue: ")
    return main_menu()


def play_game(sign1, sign2):
    global GRID_VALUES
    while True:
        clear()
        draw_board()
        valid_input = False
        while not valid_input:
            grid_ref = input("Pick a grid square using 1-9: ")
            if int(grid_ref) in range(1, 10) and GRID_VALUES.get(grid_ref) == " ":
                valid_input = True
                GRID_VALUES[grid_ref] = sign1
            else:
                clear()
                draw_board()
                print("Invalid Input.\nPlease pick a value between 1-9 that hasn't been picked already")

        # After a player takes their turn the sign is swapped from "X" to "O" or vice versa, so that the other player
        # can take their turn
        sign1, sign2 = sign2, sign1

        if is_game_won():
            clear()
            draw_board()
            print("Winner!")
            break
        # If there are no mor empty squares, the game is drawn
        elif " " not in GRID_VALUES.values():
            clear()
            draw_board()
            print("Draw!")
            break

    input("Press any key to return to the main menu: ")
    reset_board()


def draw_board():
    # Borders are added here
    board = [
        f" {GRID_VALUES['7']} | {GRID_VALUES['8']} | {GRID_VALUES['9']}",
        "-----------",
        f" {GRID_VALUES['4']} | {GRID_VALUES['5']} | {GRID_VALUES['6']}",
        "-----------",
        f" {GRID_VALUES['1']} | {GRID_VALUES['2']} | {GRID_VALUES['3']}",
    ]
    for row in board:
        print(row)


def is_game_won():
    # These represent all the possible ways to connect 3 in a row: 3 rows, 3 columns and 2 diagonals
    win1 = GRID_VALUES["7"], GRID_VALUES["8"], GRID_VALUES["9"]
    win2 = GRID_VALUES["4"], GRID_VALUES["5"], GRID_VALUES["6"]
    win3 = GRID_VALUES["1"], GRID_VALUES["2"], GRID_VALUES["3"]

    win4 = GRID_VALUES["7"], GRID_VALUES["4"], GRID_VALUES["1"]
    win5 = GRID_VALUES["8"], GRID_VALUES["5"], GRID_VALUES["2"]
    win6 = GRID_VALUES["9"], GRID_VALUES["6"], GRID_VALUES["3"]

    win7 = GRID_VALUES["7"], GRID_VALUES["5"], GRID_VALUES["3"]
    win8 = GRID_VALUES["1"], GRID_VALUES["5"], GRID_VALUES["9"]

    possible_wins = [win1, win2, win3, win4, win5, win6, win7, win8]
    for win in possible_wins:
        # First the tuple representing a winning combo is converted to a set, which will have a length of 1
        # if all values are the same. We also make sure that value is either not " ".
        if len(set(win)) == 1 and win[0] != " ":
            return True

    return False


def reset_board():
    global GRID_VALUES
    for k in GRID_VALUES:
        GRID_VALUES[k] = " "


if __name__ == '__main__':
    main_menu()
