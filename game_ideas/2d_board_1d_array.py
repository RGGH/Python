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

MOVE_COUNTER = 1

AI = 2
PLAYER = 1

GAME_OVER = 0

# -------------------------
# -------Functions --------
# -------------------------

def game_won(brd):
    ''' check for 3 in a row or column '''
    if evaluate(brd)[1]== 30:
        return PLAYER
    if evaluate(brd)[0]== -30:
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
    ''' heuristics '''

    AI_score=0
    PLAYER_score=0

    for i in range(1, BOARD_H):
        for j in range(1, BOARD_W):
            ''' Evaluate AI '''
            if (brd[j+(BOARD_W*i)]) == AI:

                # Check rows - 3 in a row
                if (brd[j+(BOARD_W)*i] == brd[j+(BOARD_W*i)+1]
                and brd[j+(BOARD_W*i)+1] == brd[j+(BOARD_W*i)+2]):
                    AI_score =  -30 #, AI
                    break

                # 2 Check rows - 2 in a row
                if (brd[j+(BOARD_W)*i] == brd[j+(BOARD_W*i)+1]):
                    AI_score = -20 #, AI
                    break
       
                #----------------
                          
                # 2 in a COL
                if (brd[(i*BOARD_W)+j] == brd[(i+1)*BOARD_W+j]):
                    AI_score = -20 # , AI
                    break

                # 3 in a COL
                if (brd[(i*BOARD_W)+j] == brd[(i+1)*BOARD_W+j]
                and brd[(i+1)*(BOARD_W)+j] == brd[(i+2)*(BOARD_W)+j]):
                    AI_score = -30 # , AI
                    break

            ''' Evaluate Player'''
            if (brd[j+(BOARD_W*i)]) == PLAYER:
                
                # Check rows - 3 in a row
                if (brd[j+(BOARD_W)*i] == brd[j+(BOARD_W*i)+1]
                and brd[j+(BOARD_W*i)+1] == brd[j+(BOARD_W*i)+2]):
                    PLAYER_score =  30 #, 
                    break

                # 2 Check rows - 2 in a row
                if (brd[j+(BOARD_W)*i] == brd[j+(BOARD_W*i)+1]):
                    PLAYER_score = 20 #, 
                    break

                # if (brd[j+(BOARD_W*i)]) == PLAYER:
                #     PLAYER_score = 10 #,            

                #----------------

                # 3 in a COL
                if (brd[(i*BOARD_W)+j] == brd[(i+1)*BOARD_W+j]
                and brd[(i+1)*(BOARD_W)+j] == brd[(i+2)*(BOARD_W)+j]):
                    PLAYER_score = 30 # , AI
                    break

                # 2 in a COL
                if (brd[(i*BOARD_W)+j] == brd[(i+1)*BOARD_W+j]):
                    PLAYER_score = 20 # , AI
                    break
                        
                # # 1 in a COL
                # PLAYER_score = 10 # , AI

    #print(f"AI_Score = {AI_score} ***  PLAYER_score = {PLAYER_score}")
    return AI_score, PLAYER_score


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

    if MOVE_COUNTER % 2 != 0:
        brd[pos] = 1
    else:
        brd[pos] = 2

    return brd


# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the brd
def minimax(brd, depth, is_max):
    ''' originally based on geeksforgeeks example '''
    score = evaluate(brd)

    # If Maximizer has won the game return 
    # evaluated score
    if (score == 30):

        #print("Player won")
        return score

    # If Minimizer has won the game return 
    # evaluated score
    if (score == -30):
 
        #print("AI won")
        return score

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
    best = minimax(brd, 0, False)
    print(best)
    return best

# ------------ #
# -- Main --- #
# ------------ #

if __name__ == "__main__":

    ''' Main '''

    # Print board    
    print(colored("\n ## redandgreen.co.uk ##", "green"))
    print(colored(" #### Starting Game ####\n", "red"))

    print_board(board)

    # Start Game Loop
    while not GAME_OVER:
    

        # Checkfor winner 
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

        # Play Moves
            
        # Human
        get_move(ROW, COL, board)
        print_board(board)
        MOVE_COUNTER +=1

        # Checkfor winner 
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
        
        # AI
        print("\nAI")
        starttime = timeit.default_timer()
        print("The start time is :",starttime)
        vbest = AI_move(board)
        update_board(board, vbest)
        print_board(board)
        print("The time difference is :", timeit.default_timer() - starttime)
        print(f"\nAI Score = {evaluate(board)[0]}")
        print(f"Player Score = {evaluate(board)[1]}")
        MOVE_COUNTER +=1



    
        
