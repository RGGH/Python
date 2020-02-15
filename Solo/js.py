# fibonacci #

n, n1, nth = 0,0,0

for i in range(0,8):
    if i == 0:
        
        n = 0
        n1 = i
        nth = n1 + n
        print(nth)
        
    elif i == 1:
        
        n = 1    
        n1 = nth
        nth = n1 + n
        print(nth)

    elif i > 1:

        
        n = n1      
        n1 = nth
        nth = n1 + n
        print(nth)
