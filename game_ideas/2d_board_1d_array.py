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
    if evaluate(brd) == 30:
        #print(PLAYER, "human wins")
        return PLAYER
    if evaluate(brd)== -30:
        #print(AI, "AI wins")
        return AI


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
      
        print(f" : row {i}")


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
    mscore = 0
    maximum = 0
    npn = -1

    for i in range(1, BOARD_H-1):
        for j in range(1, BOARD_W-2):
    
            # Evaluate Board 
            if 0 < brd[j+(BOARD_W*i)] <9:

                # 3 Check rows 3 in a row
                if (brd[j+(BOARD_W*i)] == brd[j+(BOARD_W*i)+1]
                and brd[j+(BOARD_W*i)+1] == brd[j+(BOARD_W*i)+2]):
                    mscore = 30
                    if brd[j+(BOARD_W*i)] == 2:
                        mscore = - 30

                # 3 Check for 3 in a Column
                elif (brd[(i*BOARD_W)+j] == brd[((i+1)*BOARD_W)+j]
                and brd[(i*BOARD_W)+j] == brd[((i+2)*BOARD_W)+j]):
                    mscore = 30
                    if brd[j+(BOARD_W*i)] == 2:
                        mscore = -30

                # 2 Check rows 2 in a row
                elif (brd[j+(BOARD_W)*i] == brd[j+(BOARD_W*i)+1]):
                    mscore = 20
                    if brd[j+(BOARD_W*i)] == 2:
                        mscore = -20

                # 2 Check for 2 in a Column
                elif (brd[(i*BOARD_W)+j] == brd[(i+1)*BOARD_W+j]):
                    mscore = 20
                    if brd[j+(BOARD_W*i)] == 2:
                        mscore = -20

                if abs(maximum) < abs(mscore):
                    maximum = mscore
    #print("Score =", maximum)
    return maximum

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

    # evaluated score
    if evaluate(brd) == PLAYER:
        print("PLAYER")
        return PLAYER

    if evaluate(brd) == AI:
        print("AI")
        return AI

    if not moves_left(board):
        return 0

    # If this maximizer's move
    if (is_max):

        best = -1000

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

                    # Undo the move
                    brd[j+(BOARD_W*i)] = 0

        #print(f"max depth ={depth} best={best}")
        return best

    # If this minimizer's move
    else:
        best = 1000

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
                                            is_max))

                    # Undo the move
                    brd[j+(BOARD_W*i)] = 0


        return best


def ai_move(brd):
    ''' call minimax '''
    best = minimax(brd, 0, True)
    return best

# ------------ #
# -- Main --- #
# ------------ #

if __name__ == "__main__":

    print(colored("\n ## redandgreen.co.uk ##", "green"))
    print(colored(" #### Starting Game ####\n", "red"))
    print_board(board)

    # Start Game Loop
    while not GAME_OVER:

        # Play Moves

        ############################################## Human
        get_move(ROW, COL, board)
        print_board(board)
        #print(colored(f"\nGame Score = {evaluate(board)}","blue"))

        # Check for winner 
        if game_won(board) == PLAYER:
            print(colored("\n*** Game Over p ***\n", "green"))
            GAME_OVER = True
            break
        
        if game_won(board) == AI:
            print(colored("\n*** Game Over a ***\n", "blue")) 
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
        vbest = ai_move(board)
        print(f" best move = {vbest}")
        update_board(board, vbest)
        print_board(board)

        # Check for winner 
        if game_won(board) == PLAYER:
            print(colored("\n*** Game Over p ***\n", "green"))
            GAME_OVER = True
            break

        if game_won(board) == AI:
            print(colored("\n*** Game Over a ***\n", "blue")) 
            GAME_OVER=True
            break

        # Check for tie
        if not moves_left(board):
            print(colored("*** Game Over! - Tie *** ","green"))
            GAME_OVER=True
            break

        print("\nTime difference is :", timeit.default_timer() - starttime)



