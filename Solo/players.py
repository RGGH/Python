from random import choice

players = ["bob", "jim", "kal", "pol", "ike", "goo", "jaw" ]

teamA = []
teamB = []




ll = len(players)

#print(player)
while ll >0:
    
    try:
        playerA = choice(players)
        teamA.append(playerA)
        players.remove(playerA)

        playerB = choice(players)
        teamB.append(playerB)
        players.remove(playerB)
    except:
        print("end of player list, no more players, here is final list; ")
        ll = 0
    finally:
        print(teamA)
        print(teamB)
        
