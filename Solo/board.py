import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    print (board)

def print_board(board):
    print(np.flip(board, 0))

def set_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    board[1,3] = 4
    print(np.flip(board, 0))
    
#create_board()

set_board()

