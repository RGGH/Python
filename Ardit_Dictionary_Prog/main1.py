class Worker(object):

    def __init__(self,name,pay):
        self.name = name
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self,percent):
        self.pay *=(1 + percent)

sue = Worker("Sue Smith", 60000)

a = sue.lastname()
print(a)

sue.giveraise(0.12)
b = sue.pay
print(b)

    
bob = Worker("Bob Sm" ,56000)

c = bob.lastname()
print(c)
bob.giveraise(0.13)
d = bob.pay
print(d)
