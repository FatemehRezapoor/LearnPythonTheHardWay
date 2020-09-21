# July, 8, 2020
# IMPORTANT NOTES ABOUT CLASS
# NOTE 1 : Methods in the form of funcitons. Self is a reference to the object. So when the object is created by the class it will refer to the object. Whenever a function starts with self in a class, it is called method, otherwise it is a normal function and you can not call it as a class method.

# NOTE 2 : self refers to the object. Meaning you are passing an object to the function. When you type: Man=animal(), you are passing man as an object and it will substituite your self command. The other input to init are you variables. Here, the magic keyword "self"  represents the instance of the class. It binds the attributes with the given arguments.

# NOTE 3: "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

# NOTE 4: LOOK FOR SPECIAL METHOD NAMES TO FIND SPECIAL FUNCTIONS IN CLASS

# 1. Let's Make a Class


class Car(object):
    """
    blueprint for car
  """

    def __init__(self, model, color, company, speed_limit): # Class Constructor
        self._color = color  # List of attributes that car can have
        self._company = company
        self._speed_limit = speed_limit
        self._model = model

    def start(self):  # Methods for the car
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"


car1 = Car('Jeep', 'Grey', 'Crysler', 200)
print(car1._model)
print(car1.accelarate())


# Practice: Make a class to calculate the area and volume of a rectangule

class Rectangle(object):
    def __init__(self, width, length, height):
        self._width = width
        self._length = length
        self._height = height

    def area(self):
        return self._width * self._length

    def volume(self):
        return self._width * self._length * self._height



MyRec = Rectangle(2, 3,5)
print('Area =', MyRec.area())
print('Volume =', MyRec.volume())

# Setter & Getter in Class

class Rectangle2(object):
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def area(self): # GETTER: GETS THE DEFINED VARIABLES FROM THE --INIT--
        return self._width * self._length

    def volume(self,Height): # SETTER: ACCEPTS INPUT FROM USER AND SET THAT TO THE VARIABLE
        return self._width * self._length * Height

NewRec= Rectangle2(3,3)
print('Area =', NewRec.area())
print('Volume = ', NewRec.volume(2))

# INHERITANCE CLASS
# *PARENT*
class RectangleA():
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def area(self): # GETTER: GETS THE DEFINED VARIABLES FROM THE --INIT--
        return self._width * self._length
# *CHILD*
class RectangleV(RectangleA):
    def vol(self,v):
        return (self.area()*v)

NewRecV = RectangleV(5,9)
print('This is calling from child class: ', NewRecV.area())
print(NewRecV.vol(3))

# CLASS ATTRIBUTE VS OBJECT INSTANCE

class A(object):
    def __init__(self):
        self.num = [2]

class B(object):
    num = [2]

xread = B()
yread=B()
print('Original Value x: ', xread.num)
xread.num.append(5)
print('New Value x: ', xread.num)
print('Original Value y: ', yread.num) # NOTE: We changed the num value for x object, but it modified the result for y too.

x_read = A()
y_read=A()
print('Original Value x: ', x_read.num)
x_read.num.append(5)
print('New Value x: ', x_read.num)
print('Original Value y: ', y_read.num)

# NOTE: In class A, num variable is defined as object instance. So it will only change by calling that specific object, but in class B, num is classs instance, so changing the variable by the object, it will change the class instance and will effect other objects too.

""" ADDITIONAL: Other points about the Parent/Child  """
# Source: https://www.digitalocean.com/community/tutorial_series/object-oriented-programming-in-python-3

class Fish(object):
    def __init__(self, firstname, lastname='fish', body='bone'):  # This means the last name is always fish
        self.firstname = firstname
        self.lastname = lastname
        self.body = body
    def swim(self):
        print('%s is swiming' % self.firstname)
    def swimback(self):
        print('%s can swim backward' % self.firstname)
Dokme = Fish('dokme')
Dokme.swim()
print(Dokme.body)

""" Ex 1: Child Class"""

class newfish(Fish):
    pass  # PASS ALL FROM PARENTS TO CHILD
Goldfish = newfish('Goldy')
Goldfish.swim()

""" Ex 2 : Child Class"""
class catfish(Fish): # PASS ALL FROM PARENTS
    def food(self): # ADDITIONAL METHOD JUST FOR CHILD
        print('%s eats carrots' % self.firstname)  # Function just for this child
Catty = catfish('Catty')
Catty.swim()
Catty.food()

# HOW TO OVERRIDE A PARENT CLASS

# print(sharky.body) # Becasue you use init, you have changed the ALL ATTRIBUTES IN THE PARENT BUT METHODS ARE STILL AVAIALBEL
# * IMPORTANT: When ever you use init in the child, you are changing the parents *

class shark(Fish):
    # Because we want to over write parents we need to start with init
    def __init__(self, firstname, lastname='Shark'):
        self.lastname = lastname
        self.firstname = firstname
    def swim(self):
        print('%s%s can not swim' % (self.firstname, self.lastname))


sharky = shark('SHARKY')
print(sharky.lastname)
print(sharky.swimback())

# How to add another attributes to the child?
# Super() function will do this

class domsia(Fish):
    def __init__(self, Behaviour='Bad Boy'):  # over writes the ALL ATTRIBUTES IN parents
        self.Behaviour = Behaviour
        super().__init__(self)  # ReWRITE the parents


Domy = domsia() # starts the class with your new sets.
print(Domy.Behaviour)
# To call sth from parents you need to initialise the paretns
# Parents needs a first name to initialise
print(Domy.body)
Domy.firstname = 'Domy'  # parents is called
print(Domy.lastname)
Domy.swim()

# CHECK YOUR ATTRIBUTES

print(Domy.__dict__)

# Count # of Objects using the class

