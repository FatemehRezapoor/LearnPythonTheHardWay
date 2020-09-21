# June 1, 2018
from sys import argv
from os.path import exists  # it checks the existance of a file

script, filename, filename2 = argv

print('Reading your file is in progress %s' % filename)
txt1 = open(filename, 'r')
txtfrom = txt1.read()  # reading first file
print(type(txtfrom))
print('Checking if the new file exist: %r' % exists(filename2))  # Requires the file name
txt2 = open(filename2, 'w')
txt2.truncate()
txt2.write(txtfrom)  # writing to the second file
txt1.close()
txt2.close()

# MINI PROJECT:  How to make write the code in one line?
from sys import argv
script, filename, filename2 = argv
open(filename2,'w').write(open(filename,'r').read())
