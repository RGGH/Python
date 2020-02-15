#!/bin/sh

class Car():

    def __init__(self, engine, model, mileage = 100):
        self.engine = engine
        self.model = model
        self.mileage = mileage

    def speed(self):
        if (self.engine < 1.5):
            print ( self.model + " is slow")
        else:
            print (self.model + " is fast")

    def read_mileage(self):
        print (self.model + " car has done " + str(self.mileage))

    def increment_m(self):
        self.mileage += 100

c1 = Car(1.3, "fiesta")
c2 = Car(1.3, "escort")
c3 = Car(1.1, "ka")

c1.speed()
c2.speed()
c3.speed()
c2.read_mileage()

c2.increment_m()
c2.read_mileage()

c2.increment_m()
c2.read_mileage()






