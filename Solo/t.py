from random import choice

players = ['dave', 'bob' , 'jim' , 'ray', 'ted', "moo" , "Boo","doo" ,"woo"]



teamA = []
teamB = []


while len(players) > 1:


  p1 = choice(players)
  players.remove(p1)
  teamA.append(p1)
  #print (teamA)
 

  p2 = choice(players)
  players.remove(p2)
  teamB.append(p2)
  #print (teamB)

  print("Team A " + str(teamA))
  print ("Team B" + str(teamB))
