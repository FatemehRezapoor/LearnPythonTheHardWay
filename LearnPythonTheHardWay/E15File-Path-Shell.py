# July 2020

# EXAMPLE: Working with os.path module

import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

# Print the name of os
print(os.name)

# Check if the item exist
print('Item exist {}'.format(path.exists('test.txt')))

# Check if the item is a file
print('Item is file? : {}'.format(path.isfile('test.txt')))

# Check if the item is a directory
print('Item is directory? : {}'.format(path.isdir('test.txt')))

# ** GET FULL PATH FOR THE ITEM
print('Item path is :' + str(path.realpath('test.txt')))
# Seperate the file name
print('File name is'+str(path.split(path.realpath('test.txt'))))

# Get info on the file modification time:
t=time.ctime(path.getmtime('test.txt'))
print(t)


# ** SHELL METHODS **
# Make duplicate from the file
import shutil
src=path.realpath('test.txt') # Source
dst= src + '.bak' # Destination
shutil.copy(src,dst)

# Duplicate all source info including modification time
shutil.copystat(src,dst)

# Rename the original file
#os.rename('test.txt','newtest.txt')

# PUT THINGS IN ZIP FILE
from shutil import make_archive
root_dir,tail =path.split(src) # getting directory
shutil.make_archive('Archive','zip',root_dir)

# More control on Zip file
from zipfile import ZipFile
with ZipFile('testzip.zip','w') as newzip: # w indicates writable
    newzip.write('test.txt')
    newzip.write('test.txt.bak')



