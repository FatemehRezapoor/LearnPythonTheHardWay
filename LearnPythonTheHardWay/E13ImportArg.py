# May 31, 2018
# * REQUIRES TERMINAL TO RUN *
# Important expressions:
# Arguement: A value passed to a function (or method) when calling the function.
# Module: Sth you import to make your python do more
# An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python
# ... objects. Modules are loaded into Python by the process of importing.
from sys import argv

# IMPORTANT: AGRV WILL ASK FOR INPUT FROM USER LIKE INPUT()
# BUT: IF YOU WANT THAT USER INTER INPUTS IN COMMAND LINE USE ARGV
# IF YOU WANT TO GET INPUT WHILE THE SCRIPT IS RUNNING USE INPUT()

script, first, second, third = argv # The user needs to enter 4 inputs on terminal
print('This script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:',third)

# USER TYPES: $python ImportArg.py apple orange banana
# What is it doing: It is putting those inputs in to argv and then unpack them

