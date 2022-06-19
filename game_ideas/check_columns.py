''' Test board for Game Evaluation '''

from typing import List

# constants

ROWS = 5
COLS = 8

BOARD_H = ROWS + 2
BOARD_W = COLS + 2

# 1d array board representation
board =[9,9,9,9,9,9,9,9,9,9,
        9,1,0,0,0,0,0,0,0,9,
        9,0,0,0,2,2,2,0,0,9,
        9,1,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,9,9,9,9,9,9,9,9,9,]


# CHECK 3 in a ROW - todo add code for 2 in a row
def check_rows(game_board:List)->int:
    ''' see if there is a row of 2 or 3 present '''
    for i in range(1,BOARD_H) :
        for j in range(1,BOARD_W-1) :
            if 0 < game_board[j+(BOARD_W*i)] <9:
                if (game_board[j+(BOARD_W)*i]==board[j+(BOARD_W*i)+1]
                and board[j+(BOARD_W*i)+1] ==  board[j+(BOARD_W*i)+2]):
                    return 30
    return 0


# CHECK 3 in a COL - todo add code for 2 in a col
def check_cols(game_board:List)->int:
    ''' see if there is a column of 2 or 3 present '''
    for i in range(1,BOARD_H) :
        for j in range(1,BOARD_W-1) :
            if 0 < game_board[(i*BOARD_W)+j] <9:
                if (board[(i*BOARD_W)+j]==board[(i+1)*BOARD_W+j]
                and board[(i+1)*(BOARD_W)+j] ==  board[(i+2)*(BOARD_W)+j]):
                    return 30
    return 0


if __name__ == '__main__':
    RES_R = check_rows(board)
    RES_C = check_cols(board)

    print(RES_R)
    print(RES_C)

