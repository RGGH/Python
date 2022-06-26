'''🅡🅔🅓🅐🅝🅓🅖🅡🅔🅔🅝.🅒🅞.🅤🅚'''

#-------------------------
# --- set up -------------
#-------------------------


from typing import List


board =[9,9,9,9,9,9,9,9,9,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,9,9,9,9,9,9,9,9,9,
        ]

ROWS = 8
COLS = 8

BOARD_H = ROWS + 2
BOARD_W = COLS + 2

ROW=0
COL=0

BOARD_LEN = BOARD_H * BOARD_W
MOVE_COUNTER = 0

PLAYER = 1
AI = -1

turn = 0

#-------------------------
#-------Functions --------
#-------------------------


def moves_left(brd) :
    ''' check each square of every column of every row '''
    for i in range(BOARD_H) :
        for j in range(BOARD_W) :
            if brd[j+BOARD_W*i] == 0 :
                return True
    return False

def print_board(brd):
    print("\n")
    for i in range(BOARD_H):
        for j in range(BOARD_W):
            print(brd[j+BOARD_W*i], end = " ")
        print("-")


def evaluate() :
    ''' heuristics '''
    for i in range(1,BOARD_H):
        for j in range(1,BOARD_W-1) :
            if abs(board[j+(BOARD_W*i)])==1:

                # Check rows - 3 in a row
                if (board[j+(BOARD_W)*i]==board[j+(BOARD_W*i)+1] and board[j+(BOARD_W*i)+1] ==  board[j+(BOARD_W*i)+2]):
                    if board[j+(BOARD_W)*i] == 1:
                        return 30, PLAYER
                    if board[j+(BOARD_W)*i] == 1:
                        return -30, AI
                
                #2 Check rows - 2 in a row  
                elif (board[j+(BOARD_W)*i]==board[j+(BOARD_W*i)+1]):
                    if board[j+(BOARD_W)*i] == 1:
                        return 20, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        return -20, AI

 
    for j in range(1,BOARD_H-1):
        for j in range(1,BOARD_W-1) :

        # 3 in a COL
            if abs(board[j+(BOARD_W*i)])==1:
                if board[(i*BOARD_W)+j]==1 or board[(i*BOARD_W)+j]==-1:
                    if (board[(i*BOARD_W)+j]==board[(i+1)*BOARD_W+j]
                    and board[(i+1)*(BOARD_W)+j] ==  board[(i+2)*(BOARD_W)+j]):
                        if board[j+(BOARD_W)*i] == 1:
                            return 30, PLAYER
                        if board[j+(BOARD_W)*i] == -1:
                            return -30, AI

            # 2 in a COL
            if abs(board[j+(BOARD_W*i)])==1:
                if (board[(i*BOARD_W)+j]==board[(i+1)*BOARD_W+j]):
                    if board[j+(BOARD_W)*i] == 1:
                        return 20, PLAYER
                    if board[j+(BOARD_W)*i] == -1:
                        return -20, AI


def get_move(rw:int,cl:int,turn:int,brd:List)->board:
    ''' get the row and column number from user '''
    
    user_choice = 0
    print(f"\nPlayer {turn} enter your choice \n")

    # Get Row

    try:
        user_choice = int(input(f"Please choose a row number between 1 and {ROWS} > "))
    except ValueError:
        print('We expect you to enter a valid integer')
    rw = user_choice

    user_choice = 0
    # Get col
    try:
        user_choice = int(input(f"Please choose a column number between 1 and {ROWS} > "))
    except ValueError:
        print('We expect you to enter a valid integer')
    cl = user_choice

    pos = ((int(rw)*BOARD_W))+(int(cl))

    if turn == PLAYER:
        brd[pos]=1
    if turn == AI:
        brd[pos]=-1

    return brd

# ------------ #
# -- Start --- #
# ------------ #

if __name__ == "__main__":

    while True:
        
        if moves_left(board) is False:
            print("No moves left")
            break

        if MOVE_COUNTER % 2 != 0:
            turn = PLAYER
        else:
            turn = AI


        # Get the move and redraw the board on screen
        get_move(ROW,COL,turn,board)
        print_board(board)
        print(evaluate())

        MOVE_COUNTER+=1

# ------------ #
