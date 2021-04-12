# ---global variables---
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_on = True
winner = None
current_player = "X"


# ---how the game should be---

def game_start():

    global board
    global game_on
    global winner
    global current_player

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    game_on = True
    winner = None
    current_player = "X"

    display_board()

    while game_on:
        handle_turn(current_player)
        check_if_game_over()
        next_player()
    if winner == "X" or winner == "O":
        print(winner + ' won the game' + ' try next time ' + current_player)
        check_fo_play_again()
    elif winner is None:
        print("Draw")
        check_fo_play_again()
    else:
        return False


# ---Display the game board---

def display_board():
    print("--------Let's start our game--------")

    print(board[0] + " | " + board[1] + " | " + board[2] + "                           1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "    here is the position   4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "                           7 | 8 | 9")


# ---turns---

def handle_turn(player):
    print(player + "'s turn.")

    position = input("Choose a position from 1-9 like you see in the right of the board :")
    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Please!, choose a position from 1-9:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Choose another position")

    board[position] = player

    display_board()


# ---check if game is over or not---

def check_if_game_over():
    check_for_winner()
    check_for_draw()


# ---checking for winner---

def check_for_winner():
    global winner
    line_winner = check_lines()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if line_winner:
        winner = line_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# ---check lines---

def check_lines():
    global game_on

    line_1 = board[0] == board[1] == board[2] != "-"
    line_2 = board[3] == board[4] == board[5] != "-"
    line_3 = board[6] == board[7] == board[8] != "-"

    if line_1 or line_2 or line_3:
        game_on = False
    if line_1:
        return board[0]
    elif line_2:
        return board[3]
    elif line_3:
        return board[6]
    else:
        return None


# ---check columns---

def check_columns():
    global game_on

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_on = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


# ---check diagonals---

def check_diagonals():
    global game_on

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_on = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


# ---check for draw---

def check_for_draw():
    global game_on
    if "-" not in board:
        game_on = False
    else:
        return True


# ---flip players---

def next_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


# ---checking if any player want to play again---

def check_fo_play_again():
    global game_on
    play_again = input("would you like to play again?Enter yes or no")

    if play_again == 'yes'.lower():
        game_start()
    elif play_again == 'no'.lower():
        print("Thank you for playing, have a good day")
        game_on = False


# ---restarting the game---

game_start()