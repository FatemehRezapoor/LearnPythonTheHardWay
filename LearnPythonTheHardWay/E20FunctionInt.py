# July 9, 2020
# Create function
# Also another application for --name-- == '--main--' is defining fucntions that require inputs from the next function and run them

def main():
    x = kitten()
    print(x)

def kitten():
    print('Meaow...')

if __name__ == '__main__':
    print('This is from the 1st function:')
    main()

# Functions with Return command
def main2():
    x = kitten2()
    print(x)
def kitten2():
    return ('Meaow2...')
if __name__ == '__main__':
    print('This is from the 2nd function:')
    main2()
# Add Arguements To the Function

def main3():
    x = kitten3(5)
    print(x)
def kitten3(n):
    return ('Meaow3...',n)
if __name__ == '__main__':
    print('This is from the 3nd function:')
    main3()

# Add variable Arguements To the Function

def main4():
    x = kitten4(12,2,'hi')
    print(x)
def kitten4(*args):
    if len(args):
        for s in args:
            return ('Meaow4...', s)
    else:
        return ('Just one Meaow4')

if __name__ == '__main__':
    print('This is from the 4th function:')
    main4()

# Add List, Tuple Arguements To the Function

def main5():
   x = [12,2,'hi']
   kitten5(*x) # NOTE: if you type kitten5(x), it takes the whole list and considers that as one input. So you'll get Meaows ... 12,2,'hi' output instead of Meaows ... 12

def kitten5(*args):
    print(len(args))
    if len(args):
        for s in args:
            print ('Meaow5...', s)

    else:
        return ('Just one Meaow4')

if __name__ == '__main__':
    print('This is from the 5th function:')
    main5()

# Add Keyword/Dictionary Arguements To the Function

def main6():
   x = dict (Buffy = 'Meaow', Zilla = 'aaaaah')
   kitten6(**x) # NOTE: ** ( two stars )

def kitten6(**kwargs):
    print(len(kwargs))
    if len(kwargs):
        for s in kwargs:
            print ('Kitten {} says {}'. format(s,kwargs[s]))
        else:
            print('None')

if __name__ == '__main__':
    print('This is from the 5th function:')
    main6()

# Decorator: Used when you are defining a function to use insdie another function but do not want to run the function seperately. So the function exists in the body of the code but it will not run seperetly.

def f1(f):
    def f2():
        print('This is f2 before f3')
        f()
        print('This is f2 after f3')
    return f2



# Now what if you have a long function that you don't want to put inside f1?
@f1()
def f3():
    print('I am f3')

f1(f3) # OUTPUT: This is f2
