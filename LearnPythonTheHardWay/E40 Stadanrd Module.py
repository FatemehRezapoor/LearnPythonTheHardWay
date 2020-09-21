# July, 8, 2020
# Introduction to Module
# In STANDARD PYTHON LIBRARY ( SECTION 6)

# System related functions
import sys

v = sys.version_info
print(v)
print('Python version {}.{}.{}'.format(*v)) # * means we have mulitple outputs

import os

print(os.name)

# Get the path
print(os.getenv('PATH'))

# Get the directory
print(os.getcwd())

import random

# Get a random number

x=random.randint(1,1000)
print(x)

# Shuffle a list

x= list(range(25))
print(x)
print(random.shuffle(x))

# Date & Time
import datetime

now=datetime.datetime.now()
print(now)