'''🅡🅔🅓🅐🅝🅓🅖🅡🅔🅔🅝.🅒🅞.🅤🅚'''

#-------------------------
# --- set up -------------
#-------------------------
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

rows = 8
cols = 8

board_h = rows + 2
board_w = cols + 2

row=0
col=0

board_len = board_h * board_w
move_counter = 1
#-------------------------

def print_board(board):
    for i in range(board_h):
        for j in range(board_w):
            print(board[j+board_w*i], end = " ")
        print("-")

def get_move(row,col,player,board):
    """ get the row and column number from user """
    user_choice = 0
    print(f"\nPlayer {player} enter your choice \n")

    # Get Row
    while user_choice < 1 or user_choice > rows:
        try:
            user_choice = int(input(f"Please choose a row number between 1 and {rows} >"))
        except ValueError:
            print('We expect you to enter a valid integer')
        row = user_choice

    user_choice = 0
    # Get col
    while user_choice < 1 or user_choice > cols:
        try:
            user_choice = int(input(f"Please choose a colum number between 1 and {rows} > "))
        except ValueError:
            print('We expect you to enter a valid integer')
        col = user_choice

    pos = ((int(row)*board_w))+(int(col))

    if player == 1: 
        board[pos]=1
    else:
        board[pos]=2

    return board

# ------------ #
# -- Start --- #
# ------------ #

while True:
    """ run the game loop """
    if move_counter % 2 != 0:
        player = 1
    else:
        player = 2
    move_counter+=1

    get_move(row,col,player,board)
    print_board(board)

# ------------ #
