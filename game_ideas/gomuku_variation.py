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
MOVE_COUNTER = 1

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
    """ Show the board to the PLAYER """
    print("\n")
    for i in range(BOARD_H):
        for j in range(BOARD_W):
            print(brd[j+BOARD_W*i], end = " ")
        print("-")

# def is_square_taken(brd):
#     ''' zero in square or not '''


def evaluate() :
    ''' check heuristics '''
    for i in range(1,BOARD_H):
        for j in range(1,BOARD_W-1) :
            if 0 < board[j+(BOARD_W*i)] <9:
                if (board[j+(BOARD_W)*i]==board[j+(BOARD_W*i)+1]):
                    print(f"\n\t !!! 2 in a row on row {i}!!!")

def get_move(rw:int,cl:int,player:int,brd:List)->board:
    """ get the row and column number from user """
    
    user_choice = 0
    print(f"\nPlayer {player} enter your choice \n")

    # Get Row
    while user_choice < 1 or user_choice > ROWS:
        try:
            user_choice = int(input(f"Please choose a row number between 1 and {ROWS} > "))
        except ValueError:
            print('We expect you to enter a valid integer')
        rw = user_choice

    user_choice = 0
    # Get col
    while user_choice < 1 or user_choice > COLS:
        try:
            user_choice = int(input(f"Please choose a colum number between 1 and {ROWS} > "))
        except ValueError:
            print('We expect you to enter a valid integer')
        cl = user_choice

    pos = ((int(rw)*BOARD_W))+(int(cl))

    if PLAYER == 1:
        brd[pos]=1
    else:
        brd[pos]=2

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
            PLAYER = 1
        else:
            PLAYER = 2
        MOVE_COUNTER+=1


        # Get the move and redraw the board on screen
        get_move(ROW,COL,PLAYER,board)
        print_board(board)
        evaluate()

# ------------ #
