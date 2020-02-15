import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0 #bottom row {called 5, as top is Zero}#

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    for c in range(COLUMN_COUNT-3): #check horizontal
        for r in range(ROW_COUNT):
           if board[r][c]== piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3]:
               return True
            
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-2):  #check vetical
           if board[r][c]== piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c]:
               return True

#-------------------------------------------------------------------------------------------------------#

board = create_board()
print(board)
game_over = False
turn = 0

#-------------------------------------------------------------------------------------------------------#

while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input("player 1 make your selection (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 wins!!!!")
                game_over = True
        
    #Ask for player 2 input
    else:
        col = int(input("player 2 make your selection (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("Player 2 wins!!!!")
                game_over = True

    print_board(board)
    turn +=1
    turn = turn %2

