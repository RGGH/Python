''' Test board for Game Evaluation '''

board =[9,9,9,9,9,9,9,9,9,9,
        9,1,0,0,0,0,0,0,0,9,
        9,1,0,0,2,2,2,0,0,9,
        9,1,0,0,0,0,0,0,0,9,''' Test board for Game Evaluation '''

board =[9,9,9,9,9,9,9,9,9,9,
        9,1,0,0,0,0,0,0,0,9,
        9,1,0,0,2,2,2,0,0,9,
        9,1,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,9,9,9,9,9,9,9,9,9,]


ROWS = 5
COLS = 8

BOARD_H = ROWS + 2
BOARD_W = COLS + 2

# CHECK 3 in a ROW

for i in range(1,BOARD_H) :
    for j in range(1,BOARD_W-1) :
        if 0 < board[j+(BOARD_W*i)] <9:
            if (board[j+(BOARD_W)*i]==board[j+(BOARD_W*i)+1] and board[j+(BOARD_W*i)+1] ==  board[j+(BOARD_W*i)+2]):
                print(f"3 x player {board[j+(BOARD_W)*i]} in a row!")


# CHECK 3 in a COL

for i in range(1,BOARD_H) :
    for j in range(1,BOARD_W-1) :
        if 0 < board[(i*BOARD_W)+j] <9:
            if (board[(i*BOARD_W)+j]==board[(i+1)*BOARD_W+j] and board[(i+1)*(BOARD_W)+j] ==  board[(i+2)*(BOARD_W)+j]):
                #print(f"3 x player {board[(i*BOARD_W)+j]} in a column!")
                print(f"{(i*BOARD_W)+j}\n")
                print(f"{((i+1)*BOARD_W)+j}\n")
                print(f"{((i+2)*BOARD_W)+j}\n")

        9,0,0,0,0,0,0,0,0,9,
        9,0,0,0,0,0,0,0,0,9,
        9,9,9,9,9,9,9,9,9,9,]


ROWS = 5
COLS = 8

BOARD_H = ROWS + 2
BOARD_W = COLS + 2

# CHECK 3 in a ROW

for i in range(1,BOARD_H) :
    for j in range(1,BOARD_W-1) :
        if 0 < board[j+(BOARD_W*i)] <9:
            if (board[j+(BOARD_W)*i]==board[j+(BOARD_W*i)+1] and board[j+(BOARD_W*i)+1] ==  board[j+(BOARD_W*i)+2]):
                print(f"3 x player {board[j+(BOARD_W)*i]} in a row!")


# CHECK 3 in a COL

for i in range(1,BOARD_H) :
    for j in range(1,BOARD_W-1) :
        if 0 < board[(i*BOARD_W)+j] <9:
            if (board[(i*BOARD_W)+j]==board[(i+1)*BOARD_W+j] and board[(i+1)*(BOARD_W)+j] ==  board[(i+2)*(BOARD_W)+j]):
                #print(f"3 x player {board[(i*BOARD_W)+j]} in a column!")
                print(f"{(i*BOARD_W)+j}\n")
                print(f"{((i+1)*BOARD_W)+j}\n")
                print(f"{((i+2)*BOARD_W)+j}\n")
