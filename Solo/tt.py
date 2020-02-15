Python 3.6.8 (default, Aug 20 2019, 17:12:48) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(self):
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car():
  File "/home/ian/ab.py", line 10, in Car
    self.model
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(selk):
NameError: name 'selk' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(sel):
NameError: name 'sel' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(self):
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(self):
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car():
  File "/home/ian/ab.py", line 10, in Car
    model = _self.model
NameError: name '_self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car():
  File "/home/ian/ab.py", line 10, in Car
    model = self.model
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car():
  File "/home/ian/ab.py", line 10, in Car
    model = self.model
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car():
  File "/home/ian/ab.py", line 10, in Car
    model = self.model
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(self):
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(self,model):
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(model):
NameError: name 'model' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(model):
NameError: name 'model' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 9, in <module>
    class Car(self, model):
NameError: name 'self' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 13, in <module>
    c1 = Car(fiesta)
NameError: name 'fiesta' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 15, in <module>
    print (c1.model())
TypeError: 'str' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 15, in <module>
    print (c1.model())
TypeError: 'str' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 13, in <module>
    c1 = Car(fiesta)
NameError: name 'fiesta' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
Traceback (most recent call last):
  File "/home/ian/ab.py", line 13, in <module>
    c1 = Car(fiesta)
NameError: name 'fiesta' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
5
fiesta
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 8, in <module>
    c1 = Car("fiesta", 1.4)
  File "/home/ian/ab.py", line 6, in __init__
    slef.engine = engine
NameError: name 'slef' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
1.4
>>> 
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 8, in <module>
    c1 = Car("fiesta")
TypeError: __init__() missing 1 required positional argument: 'engine'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 8, in <module>
    c1 = Car("fiesta")
  File "/home/ian/ab.py", line 6, in __init__
    self.engine = engine
NameError: name 'engine' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (i.model)
AttributeError: 'str' object has no attribute 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (str(i.model))
AttributeError: 'str' object has no attribute 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (model[i])
NameError: name 'model' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car.model)
AttributeError: type object 'Car' has no attribute 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car.__getattribute__model)
AttributeError: type object 'Car' has no attribute '__getattribute__model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car.model)
AttributeError: type object 'Car' has no attribute 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car.cars())
AttributeError: type object 'Car' has no attribute 'cars'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
<__main__.Car object at 0x7f4b124726a0>
<__main__.Car object at 0x7f4b124726a0>
<__main__.Car object at 0x7f4b124726a0>
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car(model))
NameError: name 'model' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car(i.model))
AttributeError: 'str' object has no attribute 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car())
TypeError: __init__() missing 1 required positional argument: 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
<__main__.Car object at 0x7fa496692710>
<__main__.Car object at 0x7fa496692710>
<__main__.Car object at 0x7fa496692710>
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car.model(i))
AttributeError: type object 'Car' has no attribute 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car.i)
AttributeError: type object 'Car' has no attribute 'i'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 18, in <module>
    print (Car())
TypeError: __init__() missing 1 required positional argument: 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (Car.model)
AttributeError: type object 'Car' has no attribute 'model'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
<__main__.Car object at 0x7f9eb1b116d8>
<__main__.Car object at 0x7f9eb1b116d8>
<__main__.Car object at 0x7f9eb1b116d8>
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (Car(model[i]))
TypeError: string indices must be integers
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (Car(model()))
TypeError: 'str' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (Car(model()))
TypeError: 'str' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
<__main__.Car object at 0x7f5ffded9710>
<__main__.Car object at 0x7f5ffded9710>
<__main__.Car object at 0x7f5ffded9710>
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (Car.model())
TypeError: 'str' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (cars())
TypeError: 'list' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (cars(i))
TypeError: 'list' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (cars())
TypeError: 'list' object is not callable
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
['fiesta', 'capri', 'escort']
['fiesta', 'capri', 'escort']
['fiesta', 'capri', 'escort']
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
fiesta
capri
escort
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    Carname = c + i
NameError: name 'c' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
fiesta
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    print (Carnme)
NameError: name 'Carnme' is not defined
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
fiesta
cfiesta
capri
ccapri
escort
cescort
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta
fiesta
car_fiesta
capri
car_capri
escort
car_escort
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 11, in <module>
    print (c1.model + c1.engine)
TypeError: must be str, not float
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 11, in <module>
    print (c1.model + float(c1.engine))
TypeError: must be str, not float
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta1.4
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
is crap
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
is crap
Traceback (most recent call last):
  File "/home/ian/ab.py", line 17, in <module>
    print (c2.model + str(c2.engine) + c2.what())
TypeError: must be str, not NoneType
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
Traceback (most recent call last):
  File "/home/ian/ab.py", line 17, in <module>
    print (c2.model + str(c2.engine) + c2.what)
TypeError: must be str, not method
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
>>> c2.what()
is crap
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (c2.what())
  File "/home/ian/ab.py", line 8, in what
    print(self + "is crap")
TypeError: unsupported operand type(s) for +: 'Car' and 'str'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    print (str(c2.what()))
  File "/home/ian/ab.py", line 8, in what
    print(self + "is crap")
TypeError: unsupported operand type(s) for +: 'Car' and 'str'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    c2.what()
  File "/home/ian/ab.py", line 8, in what
    print(self + "is crap")
TypeError: unsupported operand type(s) for +: 'Car' and 'str'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
is crap
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
escort is crap
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
escort is slow
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
escort is fast
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta 1.4
escort 1.6
fiesta is slow
escort is fast
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 16, in <module>
    c1 = Car("fiesta", 1.3)
TypeError: __init__() missing 1 required positional argument: 'colour'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
>>> Python 3.6.8 (default, Aug 20 2019, 17:12:48)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
========================== RESTART: /home/ian/ab.py ==========================
>>> 
========================== RESTART: /home/ian/ab.py ==========================
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 11, in speed
    if (self.engine < 1.5):
TypeError: '<' not supported between instances of 'str' and 'float'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 11, in speed
    if (self.engine < 1.5):
TypeError: '<' not supported between instances of 'str' and 'float'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 11, in speed
    if (self.engine < 1.5):
TypeError: '<' not supported between instances of 'str' and 'float'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 11, in speed
    if (self.engine < 1.5):
TypeError: '<' not supported between instances of 'str' and 'float'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 14, in speed
    print (self.model + " is fast")
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 11, in speed
    if (self.engine < 1.5):
TypeError: '<' not supported between instances of 'str' and 'float'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 20, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 11, in speed
    if (self.engine < 1.5):
TypeError: '<' not supported between instances of 'str' and 'float'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 15, in <module>
    c1 = Car("fiesta", 1.3, "red")
TypeError: __init__() takes 3 positional arguments but 4 were given
>>> 
========================== RESTART: /home/ian/ab.py ==========================
Traceback (most recent call last):
  File "/home/ian/ab.py", line 19, in <module>
    c1.speed()
  File "/home/ian/ab.py", line 10, in speed
    if (self.engine < 1.5):
TypeError: '<' not supported between instances of 'str' and 'float'
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta is slow
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta is slow
escort is slow
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta is slow
escort is slow
Traceback (most recent call last):
  File "/home/ian/ab.py", line 25, in <module>
    c2.read_mileage()
  File "/home/ian/ab.py", line 17, in read_mileage
    print ("car has done " + self.mileage)
TypeError: must be str, not int
>>> 
========================== RESTART: /home/ian/ab.py ==========================
fiesta is slow
escort is slow
car has done 100
>>> 
========================== RESTART: /home/ian/ab.py ==========================

========================== RESTART: /home/ian/ab.py ==========================
