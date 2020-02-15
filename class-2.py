drivers = {"Lewis Hamilton" : 100000, "Lando Norris": 33333, "Max Vers" : 23222}

class Worker(object):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def set_pay(self, percent):
        self.pay *= (1 + percent)

    def show_pay(self):
        print(int(self.pay))
        
def proc_pay():
    for driver, sal in drivers.items():
        fname = driver.split()[0]
        r=(fname)
        print(r)
        r = Worker(driver, sal)
        r.set_pay(0.12)
        r.show_pay()
   
proc_pay()
