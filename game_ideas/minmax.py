 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
""" elongated tic-tac-toe for minimax study """

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

def gen_rowcols(board):
    """ filter the playable coordinates """
    sq_ids=[]
    for h in range(bheight):
        if h > 0 and h < bheight-1:
            for w in range(bwidth): 
                if w > 0 and w < bwidth-1:
                    x=h,w
                    sq_ids.append (x)
    return sq_ids


def check_win(sq_ids):
    pass


# def player1(sq_ids):
#     """ update inner playable grid with user input """
#     print(f"which square? - top left = 1 bottom right = {playable} ")
#     x=int(input())
#     sq_ids[1]=x
#     print(sq_ids)

# def player2(sq_ids):
#     """ update inner playable grid with user input """
#     print(f"which square? - top left = 1 bottom right = {playable} ")
#     x=int(input())
#     sq_ids[x]=-x
#     print(sq_ids)


# main driver
if __name__ == "__main__":

    sq = gen_rowcols(board)
    print(sq)

