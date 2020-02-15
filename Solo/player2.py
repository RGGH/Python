from random import choice

players = ["jim", "jam" ,"jom", "wim", "sim", "kim", "lim", "fim", "Alexandr"]

teamA = []
teamB = []

plen = len(players)


while plen > 0:
    try:
        player = choice(players)
        teamA.append(player)
        players.remove(player)
        
        player = choice(players)
        teamB.append(player)
        players.remove(player)
        
    except:
        print("players all used up")
        print("finished")
        plen=0
    finally:
        if plen == 0:
            print ("Team A = ")
            for i in teamA:
                print (i)
            print("")
            print("Team B = ")
            for i in teamB:
                print (i)

     



        
        
