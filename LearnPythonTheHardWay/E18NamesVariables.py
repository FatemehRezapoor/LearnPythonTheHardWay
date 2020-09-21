# June 1 , 2018
# Update: July 9, 2020
# E18,16
# Learn how to make a function in Python

# First type: *args accepts variable number of inputs to the function

def print_two(*args):
    arg1, arg2 = args
    print('This is my argument 1:%r and argumrent 2: %r' % (arg1, arg2))

def print_2again(arg1, arg2):
    print('This is my argument 1:%r and argumrent 2: %r' % (arg1, arg2))


def printone(arg1):
    print('This is my argument 1:%r' % arg1)


def print_none():
    print('I got nothing to print')


print_two(2, 'yohooo')
print_2again('lala', 'lolo')
printone('What\'s up')
print_none()

# Mini project: Define a function to add numbers and ask user to input values

t2 = int(input('enter the second number'))
t1 = int(input('enter the first number:'))


def mysum(arg1, arg2):
    argsum = arg1 + arg2
    print('Thi seummation results is %d' % argsum)
    return argsum


# mysum(t1, t2)
# you can even do operation on your inputs
summ = mysum(t1 * 2, t2 * 2)


# Mini project: Define a function inside a function

def multiply(arg1, arg2):
    multi = mysum(arg1, arg2) * 10
    print('This is your summation and multiplication:%d' % multi)
multiply(1, 2)

# Function in a function

def main():
    kitten()

def kitten():
    print('Meaow....')
print(__name__)
# if __name__ =='__main__':main()