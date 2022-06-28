

'''🅡🅔🅓🅐🅝🅓🅖🅡🅔🅔🅝.🅒🅞.🅤🅚'''

# -------------------------
# --- set up -------------
# -------------------------
from colorama import init
from termcolor import colored
init()
from typing import List

board = [9, 9, 9, 9, 9,
         9, 0, 0, 0, 9,
         9, 0, 0, 0, 9,
         9, 0, 0, 0, 9,
         9, 0, 0,-1, 9,
         9, 9, 9, 9, 9
         ]

ROWS = 4
COLS = 3

BOARD_H = ROWS + 2
BOARD_W = COLS + 2

ROW = 0
COL = 0

BOARD_LEN = BOARD_H * BOARD_W

MOVE_COUNTER = 1

PLAYER = 1
AI = -1

GAME_OVER = 0

# -------------------------
# -------Functions --------
# -------------------------

def game_won(board):
    ''' check for 3 in a row or column '''
    if evaluate(board)==30:
        return 1
    if evaluate(board)==-30:
        return -1

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
        print("-")


def update_board(brd, best):
    ''' Updated board array with MiniMax AI best choice'''
    for i in range(BOARD_H):
        for j in range(BOARD_W):

            # find position
            if brd[j+(BOARD_W*i)] == best:

                # Make the AI move
                brd[j+(BOARD_W*i)] = -1
                return


def evaluate(board):
    ''' heuristics '''

    scores=0

    for i in range(1, BOARD_H):
        for j in range(1, BOARD_W):
            if abs(board[j+(BOARD_W*i)]) == 1:

                # Check rows - 3 in a row
                if (board[j+(BOARD_W)*i] == board[j+(BOARD_W*i)+1]
                        and board[j+(BOARD_W*i)+1] == board[j+(BOARD_W*i)+2]):
                    if board[j+(BOARD_W)*i] == 1:
                        scores = 30 #, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        scores =  -30 #, AI

                # 2 Check rows - 2 in a row
                if (board[j+(BOARD_W)*i] == board[j+(BOARD_W*i)+1]):
                    if board[j+(BOARD_W)*i] == 1:
                        if scores < 30:
                            scores =  20 #, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        if scores > -30:
                            scores = -20 #, AI


    # for i in range(1, BOARD_H):
    #     for j in range(1, BOARD_W):
    #         if abs(board[j+(BOARD_W*i)]) == 1:

                            
            # 3 in a COL
                if (board[(i*BOARD_W)+j] == board[(i+1)*BOARD_W+j]
                        and board[(i+1)*(BOARD_W)+j] == board[(i+2)*(BOARD_W)+j]):
                    if board[j+(BOARD_W)*i] == 1:
                        scores = 30 # , PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        scores = -30 # , AI

            # 2 in a COL
                if (board[(i*BOARD_W)+j] == board[(i+1)*BOARD_W+j]):
                    if board[j+(BOARD_W)*i] == 1:
                        if scores < 30:
                            scores = 20 # , PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        if scores > -30:
                            scores = -20 # , AI

    #print(scores)
    return scores


def get_move(rw: int, cl: int, brd: List) -> board:
    ''' get the row and column number from user '''

    user_choice = 0
    print(colored(f"\nPlayer enter your choice \n", "yellow"))

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
    ''' originally based on geeksforgeeks example '''
    score = evaluate(board)

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
    if (moves_left(board) == False):
        return 0

    # If this maximizer's move
    if (isMax):
        best = -30

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
                    # print("maximizer",best)
                    # Undo the move
                    board[j+(BOARD_W*i)] = 0

        return best

    # If this minimizer's move
    else:
        best = 30

        # Traverse all cells
        for i in range(BOARD_H):
            for j in range(BOARD_W):

                # Check if cell is empty
                if (board[j+(BOARD_W*i)] == 0):

                    # Make the move
                    board[j+(BOARD_W*i)] = AI

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, 
                                            depth + 1, 
                                            not isMax))
                    # print("minimizer>",best)
                    # Undo the move
                    board[j+(BOARD_W*i)] = 0
        
        return best


def AI_move(board):
    ''' call minimax '''
    best = minimax(board, 0, False)
    return best

# ------------ #
# -- Main --- #
# ------------ #

if __name__ == "__main__":

    ''' Main '''

    # Print board    
    print(colored("Starting Game...\n", "blue"))
    print_board(board)

    # Start Game Loop
    while not GAME_OVER:

        # Human
        get_move(ROW, COL, board)
        print_board(board)
        print(evaluate(board))
        MOVE_COUNTER +=1
        
        # AI
        print("\nAI")
        vbest = AI_move(board)
        update_board(board, vbest)
        print_board(board)
        print(evaluate(board))
        MOVE_COUNTER +=1

        # Checkfor winner 
        if game_won(board) == PLAYER:
            print(colored("Game Over - human wins\n", "red"))
            GAME_OVER = True
        if game_won(board) == AI:
            print(colored("Game Over - AI wins\n", "blue")) 
            GAME_OVER = True

        # Check for tie
        if moves_left(board) == False:
            print(colored("Game Over! - Tie","green"))
            GAME_OVER = True


    
        
