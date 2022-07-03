'''🅡🅔🅓🅐🅝🅓🅖🅡🅔🅔🅝.🅒🅞.🅤🅚'''
## test board evalutions 1,2,3 ##

from dem1b import evaluate

board_m11 = [9, 9, 9, 9, 9,
            9, 1, 0, 0, 9,
            9, 2, 0, 0, 9,
            9, 0, 0, 0, 9,
            9, 9, 9, 9, 9
            ]

board_20 = [9, 9, 9, 9, 9,
            9, 0, 0, 0, 9,
            9, 1, 0, 0, 9,
            9, 1, 0, 0, 9,
            9, 9, 9, 9, 9
            ]

board_m22 = [9, 9, 9, 9, 9,
            9, 1, 1, 0, 9,
            9, 2, 2, 0, 9,
            9, 2, 0, 0, 9,
            9, 9, 9, 9, 9
            ]

board_30 = [9, 9, 9, 9, 9,
            9, 1, 0, 0, 9,
            9, 1, 0, 0, 9,
            9, 1, 0, 0, 9,
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

def test_evaluate():
    ''' check 2 and 3 in row/col scores'''
    ch_w = evaluate(board_m11)
    assert ch_w == 0
    ch_x = evaluate(board_20)
    assert ch_x == 20
    ch_y =evaluate(board_m22)
    assert ch_y == 20
    ch_z =evaluate(board_30)
    assert ch_z == 30
