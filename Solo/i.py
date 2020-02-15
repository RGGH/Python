f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


fobj = open("demofile2.txt", "rt")
print(fobj.read())

i = 5;

while i < 12:
    
    print ("Hello" + str(i))
    i= i + 2
