""" elongated tic-tac-toe for minimax study """

from re import I


player1 = +1
comp = -1

board =[99,99,99,99,99,
        99, 0, 0, 0,99,
        99, 0, 0, 0,99,
        99, 0, 0, 0,99,
        99, 0, 0, 0,99,
        99,99,99,99,99]

bwidth=5
bheight=6
rows=bheight-2
cols=bwidth-2

playable = rows * cols

def grid():
    """ idenitfy inner, playable grid """
    sq_id=[]
    i=0
    while i < len(board): 
        if board[i] != 99:
            sq_id.append ((board[i]))
        i+=1
    return sq_id


def check_win(sq_id):
    for i in range (cols):
        for j in range(rows):
            if j == j+1:
                print("OH")



def player1(sq_id):
    """ update inner playable grid with user input """
    print(f"which square? - top left = 1 bottom right = {playable} ")
    x=int(input())
    sq_id[x]=x
    print(sq_id)

def player2(sq_id):
    """ update inner playable grid with user input """
    print(f"which square? - top left = 1 bottom right = {playable} ")
    x=int(input())
    sq_id[x]=-x
    print(sq_id)


# main driver
if __name__ == "__main__":
    sq = grid()
    check_win(sq)
    # add code for game loop
    player1(sq)
    player3(sq)
