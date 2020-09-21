# June 6 , 2018
# DICTIONARY: Like list but you can access the variables with a key not index
# MODULE: Includes functions( methods) and variables ( attributes)

# Class Example

class Customer():
    """Customer has the following properties"""
    """ Attributes:
                    name: string represents the name of a person
                    balance: represents the money
    """
    bank = 'RBC'  # class attribute

    def __init__(self, name, balance=0):
        # These are object attributes
        self.name = name
        self.balance = balance
        print('Processing:')
        print('Your balance is %d' % self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('You can not get the money')
        else:
            self.balance = self.balance - amount
            print('Your account has %d $' % self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('Your new account has %d $' % self.balance)

    """ Doesn't require the instance (self) for the output """

    @staticmethod
    def finish():
        print('we are done')


jeff = Customer('sara', 1000)
print(jeff.balance)
jeff.withdraw(10)
jeff.deposit(100)
print(jeff.bank)  # static method
print(Customer.bank)  # static method
Customer.finish()

class animal(object):

    emotion='cute and smiling' # This is a class attribute which is accessable for everyone in the class

    def __init__(self,name):
        self.name=name
        print('Dog name is %s' %self.name)

Dokme=animal('Dokme')
print(Dokme.name)
print(Dokme.emotion)
print(animal.emotion)



