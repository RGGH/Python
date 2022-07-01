'''🅡🅔🅓🅐🅝🅓🅖🅡🅔🅔🅝.🅒🅞.🅤🅚'''

# -------------------------
# --- set up -------------
# -------------------------
from colorama import init
from termcolor import colored
init()
from typing import List

import timeit

board = [9, 9, 9, 9, 9,
         9, 0, 0, 0, 9,
         9, 0, 0, 0, 9,
         9, 0, 0, 0, 9,
         9, 9, 9, 9, 9
         ]

ROWS = 3
COLS = 3

BOARD_H = ROWS + 2
BOARD_W = COLS + 2

ROW = 0
COL = 0

BOARD_LEN = BOARD_H * BOARD_W

AI = 2
PLAYER = 1

GAME_OVER = 0

# -------------------------
# -------Functions --------
# -------------------------

def game_won(brd):
    ''' check for 3 in a row or column '''
    if evaluate(brd)>= 30:
        return PLAYER

def moves_left(brd):
    ''' check each square of every column of every row '''
    for i in range(BOARD_H):
        for j in range(BOARD_W):
            if brd[j+BOARD_W*i] == 0:
                return True
    return False


def print_board(brd):
    ''' draws current board state to screen '''
    print("\n")
    for i in range(BOARD_H):
        for j in range(BOARD_W):
            print(brd[j+BOARD_W*i],end=" ")
        print(f"- row {i}")


def update_board(brd, best):
    ''' Updated board array with MiniMax AI best choice'''
    for i in range(BOARD_H):
        for j in range(BOARD_W):

            # find position
            if brd[j+(BOARD_W*i)] == best:

                # Make the AI move
                brd[j+(BOARD_W*i)] = AI 

                return


def evaluate(brd):
    ''' heuristics - score for minimax '''
    score = 0
    max_score = 0
    mx=0

    for i in range(1, BOARD_H):
        for j in range(1, BOARD_W):
    
            # Evaluate Board 
            if 0 < brd[j+(BOARD_W*i)] <9:

                # Establish which player
                mx = -1 if brd[j+(BOARD_W*i)] == 2 else 1

                # 2 Check rows - 2 in a row
                if (brd[j+(BOARD_W)*i] == brd[j+(BOARD_W*i)+1]):
                    score = 22
                
                # 2 Check for 2 in a Column
                if (brd[(i*BOARD_W)+j] == brd[(i+1)*BOARD_W+j]):
                    score = 21

                # 3 Check rows - 3 in a row
                if (brd[j+(BOARD_W*i)] == brd[j+(BOARD_W*i)+1]
                and brd[j+(BOARD_W*i)+1] == brd[j+(BOARD_W*i)+2]):
                    score = 30
                    
                # 3 Check for 3 in a Column
                if (brd[(i*BOARD_W)+j] == brd[((i+1)*BOARD_W)+j]
                and brd[(i*BOARD_W)+j] == brd[((i+2)*BOARD_W)+j]):
                    score = 31
                    
            if score > max_score:
                max_score = score

    return max_score * mx

def get_move(rw: int, cl: int, brd: List) -> board:
    ''' get the row and column number from user '''

    user_choice = 0
    print(colored("\nPlayer enter your choice \n", "yellow"))

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

    brd[pos] = PLAYER
    return brd


# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the brd
def minimax(brd, depth, is_max):
    ''' originally based on geeksforgeeks example '''

    a_score = evaluate(brd)

    # If Maximizer has won the game return 

    # evaluated score
    if a_score == 30:
        return a_score

    if a_score == -30:
        return a_score

    # If there are no more moves and no winner then
    # it is a tie
    if not moves_left(brd):
        return 0

    # If this maximizer's move
    if (is_max):

        best = -30

        # Traverse all cells
        for i in range(BOARD_H):
            for j in range(BOARD_W):

                # Check if cell is empty
                if brd[j+(BOARD_W*i)] == 0:

                    # Make the move
                    brd[j+(BOARD_W*i)] = PLAYER

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(brd,
                                            depth + 1,
                                            not is_max))
                    #print("\tmaximizer>",best)
                    # Undo the move
                    brd[j+(BOARD_W*i)] = 0

        print(f"max depth ={depth} best={best}")
        return best

    # If this minimizer's move
    else:
        best = 30

        # Traverse all cells
        for i in range(BOARD_H):
            for j in range(BOARD_W):

                # Check if cell is empty
                if (brd[j+(BOARD_W*i)] == 0):

                    # Make the move
                    brd[j+(BOARD_W*i)] = AI

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(brd, 
                                            depth + 1, 
                                            not is_max))
                    #print("minimizer...>",best)
                    # Undo the move
                    brd[j+(BOARD_W*i)] = 0
        
        print(f"min depth ={depth} best={best}")
        return best


def AI_move(brd):
    ''' call minimax '''
    best = minimax(brd, 0, True)
    print(best)
    return best

# ------------ #
# -- Main --- #
# ------------ #

if __name__ == "__main__":

    print(colored("\n ## redandgreen.co.uk ##", "green"))
    print(colored(" #### Starting Game ####\n", "red"))
    print_board(board)

    #1
    print(evaluate(board))

    # Start Game Loop
    while not GAME_OVER:

        # Play Moves

        ############################################## Human
        get_move(ROW, COL, board)
        print_board(board)

        # Check for winner 
        if game_won(board) == PLAYER:
            print(colored("\n*** Game Over - human wins ***\n", "green"))
            GAME_OVER = True
            break
        
        if game_won(board) == AI:
            print(colored("\n*** Game Over - AI wins ***\n", "blue")) 
            GAME_OVER=True
            break

        # Check for tie
        if not moves_left(board):
            print(colored("*** Game Over! - Tie *** ","green"))
            GAME_OVER=True
            break
        
        ################################################## AI

        print("\nAI to play")
        starttime = timeit.default_timer()
        print("The start time is :",starttime)
        #
        vbest = AI_move(board)
        print(f" best move = {vbest}")
        update_board(board, vbest)
        #
        print_board(board)

        # Check for winner 
        if game_won(board) == PLAYER:
            print(colored("\n*** Game Over ***\n", "green"))
            GAME_OVER = True
            break

        if game_won(board) == AI:
            print(colored("\n*** Game Over ***\n", "blue")) 
            GAME_OVER=True
            break

        # Check for tie
        if not moves_left(board):
            print(colored("*** Game Over! - Tie *** ","green"))
            GAME_OVER=True
            break

        print("\nTime difference is :", timeit.default_timer() - starttime)
        print(colored(f"\nGame Score = {evaluate(board)}","red"))


