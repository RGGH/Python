'''🅡🅔🅓🅐🅝🅓🅖🅡🅔🅔🅝.🅒🅞.🅤🅚'''

# -------------------------
# --- set up -------------
# -------------------------

from typing import List

board = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
         9, 0, 0, 0, 0, 0, 0, 0, 0, 9,
         9, 0, 0, 0, 0, 0, 0, 0, 0, 9,
         9, 0, 0, 0, 0, 0, 0, 0, 0, 9,
         9, 0, 0, 0, 0, 0, 0, 0, 0, 9,
         9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
         ]

ROWS = 4
COLS = 8

BOARD_H = ROWS + 2
BOARD_W = COLS + 2

ROW = 0
COL = 0

BOARD_LEN = BOARD_H * BOARD_W
MOVE_COUNTER = 1

PLAYER = 1
AI = -1

# -------------------------
# -------Functions --------
# -------------------------


def moves_left(brd):
    ''' check each square of every column of every row '''
    for i in range(BOARD_H):
        for j in range(BOARD_W):
            if brd[j+BOARD_W*i] == 0:
                return True
    return False


def print_board(brd):
    print("\n")
    for i in range(BOARD_H):
        for j in range(BOARD_W):
            print(brd[j+BOARD_W*i], end=" ")
        print("-")


def evaluate(board):
    ''' heuristics '''
    for i in range(1, BOARD_H):
        for j in range(1, BOARD_W-1):
            if abs(board[j+(BOARD_W*i)]) == 1:
                # Check rows - 3 in a row
                if (board[j+(BOARD_W)*i] == board[j+(BOARD_W*i)+1]
                        and board[j+(BOARD_W*i)+1] == board[j+(BOARD_W*i)+2]):
                    if board[j+(BOARD_W)*i] == 1:
                        return 30, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        return -30, AI

                # 2 Check rows - 2 in a row
                if (board[j+(BOARD_W)*i] == board[j+(BOARD_W*i)+1]):
                    if board[j+(BOARD_W)*i] == 1:
                        return 20, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        return -20, AI

    for i in range(1, BOARD_H-1):
        for j in range(1, BOARD_W-1):
            if abs(board[j+(BOARD_W*i)]) == 1:
            # 3 in a COL
                if (board[(i*BOARD_W)+j] == board[(i+1)*BOARD_W+j]
                        and board[(i+1)*(BOARD_W)+j] == board[(i+2)*(BOARD_W)+j]):
                    if board[j+(BOARD_W)*i] == 1:
                        return 30, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        return -30, AI

            # 2 in a COL
            if abs(board[j+(BOARD_W*i)]) == 1:
                if (board[(i*BOARD_W)+j] == board[(i+1)*BOARD_W+j]):
                    if board[j+(BOARD_W)*i] == 1:
                        return 20, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        return -20, AI

    return 0


def get_move(rw: int, cl: int, brd: List) -> board:
    ''' get the row and column number from user '''

    user_choice = 0

    print(f"\nPlayer enter your choice \n")

    try:
        user_choice = int(
            input(f"Please choose a row number between 1 and {ROWS} > "))
    except ValueError:
        print('We expect you to enter a valid integer')
    rw = user_choice

    user_choice = 0
    # Get col
    try:
        user_choice = int(
            input(f"Please choose a column number between 1 and {COLS} > "))
    except ValueError:
        print('We expect you to enter a valid integer')
    cl = user_choice

    pos = ((int(rw)*BOARD_W))+(int(cl))

    if MOVE_COUNTER % 2 != 0:
        brd[pos] = 1
    else:
        brd[pos] = -1

    return brd


# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax):
    score = evaluate(board)

    # If Maximizer has won the game return his
    # evaluated score
    if (score == 30):
        return score

    # If Minimizer has won the game return his
    # evaluated score
    if (score == -30):
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if (moves_left(board) == False):
        return 0

    # If this maximizer's move
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(BOARD_H):
            for j in range(BOARD_W):

                # Check if cell is empty
                if board[j+(BOARD_W*i)] == 0:

                    # Make the move
                    board[j+(BOARD_W*i)] = PLAYER

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(board,
                                             depth + 1,
                                             not isMax))

                    # Undo the move
                    board[j+(BOARD_W*i)] = 0
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(BOARD_H):
            for j in range(BOARD_W):

                # Check if cell is empty
                if (board[j+(BOARD_W*i)] == 0):

                    # Make the move
                    board[j+(BOARD_W*i)] = AI

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax))

                    # Undo the move
                    board[j+(BOARD_W*i)] = 0
        return best


# ------------ #
# -- Start --- #
# ------------ #
if __name__ == "__main__":

    while True:

        if moves_left(board) is False:
            print("No moves left")
            break

        get_move(ROW, COL, board)
        print_board(board)
        print(evaluate(board))

        MOVE_COUNTER += 1

        x = minimax(board, 3, True)
        
        print(x)

