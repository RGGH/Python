#Have a list of players
#Choose 2 teams
#each team is made from the list of players

from random import choice

players = ["bob", "jim", "mel", "kim", "koo", "moo", "goo", "Alexandr", "tom", "dave", "alan"]

teamA = []
teamB = []

pl = len(players)

while pl > 0:
    try:
        player = choice(players)
        teamA.append(player)
        players.remove(player)

        player = choice(players)
        teamB.append(player)
        players.remove(player)

    except:
        print("Players all used up!")
        print("finished teams have been chosen!")
        pl = 0

    finally:
        if pl == 0:
            print ("team A = ")
            for i in teamA:
                print (i)

            print(" ")
            print ("team B =  ")
            for i in teamB:
                print (i)
