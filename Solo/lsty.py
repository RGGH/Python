drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

bets2 = bets[:]

print(bets2)
bets2.append(33)

print(bets)
print(bets2)
del bets

print (bets2)

print(bets)
