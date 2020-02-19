import json

drivers = {"Alfie Noakes" : 100000, "John Stitch": 33333, "Barry McDermott" : 23222}

class Worker(object):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def set_pay(self, percent):
        self.pay *= (1 + percent)

    def show_pay(self):
        print(int(self.pay))

    def get_pay(self):
        return(int(self.pay))
        
def proc_pay():
    for driver, sal in drivers.items():
        fname = driver.split()[0] # use the first word from the key
        r=(fname)
        print(r)
        r = Worker(driver, sal)
        r.set_pay(0.12) # increase the pay by 12%
        r.show_pay()
        print("+" * 12)
        new_sal = (r.get_pay())
        drivers.update({driver : new_sal}) # update the original 'dict'
   
proc_pay()

# Next - Sort the keys by way of using JSON

with open ("drivers.json", "w") as jf:
    json.dump(drivers, jf, indent =2,  sort_keys = True)

# See output file, Barry is now BEFORE John. Good!


