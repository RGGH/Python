# Sudoku Grid

gridh = 9
gridv = 9

def pr_row():
	for j in range (0, gridh + 4):
		if j %4 != 0:
			print ("+", end = " ")
		else:
			print ("|", end = " ")
	

for i in range(0, 13):
    if i % 4 ==0:
        print ("- " * 13)
    else:
            pr_row()
            print("\n")
