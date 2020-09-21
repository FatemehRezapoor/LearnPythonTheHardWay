# June 8, 2018
# Parents and Subclass

# Source: https://www.digitalocean.com/community/tutorial_series/object-oriented-programming-in-python-3

""" A parents class which can define some of the main properties of a fish"""


class Fish(object):
    def __init__(self, firstname, lastname='fish', body='bone'):  # This means the last name is always fish
        self.firstname = firstname
        self.lastname = lastname
        self.body = body

    def swim(self):
        print('%s is swiming' % self.firstname)

    def swimback(self):
        print('%s can swim backward' % self.firstname)


Dokme = Fish('Dokme')
Dokme.swim()
print(Dokme.body)

""" Child class called goldfish"""


class newfish(Fish):
    pass  # passes everything from the class


Goldfish = newfish('Goldy')
Goldfish.swim()

""" Another child class which has some functions"""


class catfish(Fish):
    def food(self):
        print('%s eats carrots' % self.firstname)  # Function just for this child


Catty = catfish('Catty')
Catty.swim()
Catty.food()


# HOW TO OVERRIDE A PARENT CLASS

class shark(Fish):
    # Because we want to over write parents we need to start with init
    def __init__(self, firstname, lastname='Shark'):
        self.lastname = lastname
        self.firstname = firstname

    def swim(self):
        print('%s%s can not swim' % (self.firstname, self.lastname))


sharky = shark('Sharky')
print(sharky.lastname)


# print(sharky.body) # Becasue you use init, you have changed the whole attributes

# * IMPORTANT: When ever you use init in the child, you are changing the parents *

# How to change a part of parents but use other attributes?
# Super() function will do this

class domsia(Fish):
    def __init__(self, Behaviour='Bad Boy'):  # over writes the whole parents
        self.Behaviour = Behaviour
        super().__init__(self)  # Re read the whole parents


Domy = domsia()  # starts the class with your new sets.
print(Domy.Behaviour)
# To call sth from paretns you need ti initialise the paretns
# Parents needs a first name to initialise
Domy.firstname = 'Domy'  # parents is called
print(Domy.lastname)
Domy.swim()
