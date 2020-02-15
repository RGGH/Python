
s = "s"
a = 10

while (a < 12):

 try:
    print(a + s)
 except:
    print ('something went wrong')
    a = a + 1
    s = 100
 else:
    print("ok")
    
 finally:
    print('always runs')

