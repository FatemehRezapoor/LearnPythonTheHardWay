# July 9, 2020
# What is the meaning of __name__ = __main__?

# To outline the basics: The global variable, __name__, in the module that is the entry point to your program, is '__main__'. Otherwise, it's the name you import the module by. So, code under the if block will only run if the module is the entry point to your program.
# It allows the code in the module to be importable by other modules, WITHOUT executing the code block beneath on import.

# CASE 1: Let make mymath.py file which includes the following command:
def add(a,b):
    return a+b
print(__name__)
print(add(2,3))
# name is a built in function in python which checks for the name of the called function. So if you call the function within it's module(mymath.py), name is equal to the 'main' which is the main module ( name of the module: mymath is the main module ).

# Create this function and save it as add.py.It will print the output of the first function

# **OUTPUT**:
# __main__   ( Means we are running the module directly)
#5

# *CASE 2: Now let's make ANOTHER .py file which imports add module. NOTE: YOU HAVE TO RUN THIS IN ANOTHER my2.PY FILE TO WORK:
# ***CODE***
# import mymath
# print (mymath.add(5,8))

# OUTPUT:
# mymath ( means the name != main, means module is being called within another module, not directly)
# 5 ( The whole mymath.py module is running )
# 13 ( After mymath.py execution, my2.py will execute)
# NOTE: WHAT IF WE DONT WANT THE WHOLE mymath.py execute. What if we only want specific line to execute?

# SOLUTION:

def add(a,b):
    return a+b
print(__name__)
if __name__ == '__main__':
    print(add(2,3)) # This line will only execute if and only if, we run the module directly

# OUTPUT:
# __main__
# 5

# Let's go back to my2.py and run it again
# OUTPUT:
# mymath
# 13

# 5 does not execute because the if condition did not meet.





