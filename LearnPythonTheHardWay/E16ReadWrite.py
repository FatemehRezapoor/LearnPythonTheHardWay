# June 1, 2018
# Update: July 13, 2020

# ** OPEN A TEXT FILE:**
f = open('read.txt','r') # Returns a file object.

"""The 'r' means the file is opening in read mode.
# If you put 'w', it will open the file in  the write mode, so it will empty the file if it's not empty.
# The 'a' is append mode and it will start at the end of the file and will not empty the file.
#  The 'r+' means you can both read and write the text file.
# The 'r+b' and 'r+t' identifies the file type to see if it is binary or a text file"""

print(type(f))
for line in f:
    print(line.rstrip()) # rstrip() will strip any new lines and white spaces from the end of the line
# Option 2:
print(f.read())

# ** WRITE A FILE **
f = open('read.txt','r')
fout= open('readCopy.txt','w+')
for line in f:
    print(line.rstrip(),file=fout)

for i in range(1,5):
    fout.write('This is a new line {}:\r'.format(i))
fout.close()

# ** ADD LINES TO THE END OF FILE
fout = open('readCopy.txt', 'a')
fout.write('Hi')
fout.close()

# ** READ AND WRITE IN A DIRECTORY**

path = 'D:/Repository/LearnPythonTheHardWay/new.txt'
txt = open(path, 'r+')
print(txt.read())
txt.write('This is a new line 5')  # If you don't truncate, It will write in the end of lines
print(txt.read())
txt.close()

""" from sys import argv

script, filename = argv
print('Hello. You want to open %s text file' % filename)
txt = open(filename, 'w')
print('File is opened\n next step: Deleting')
txt.truncate()
sen1 = input('Sentence 1:')
sen2 = input('Sentence 2:')
txt.write('writing in progress')
txt.write('\n')
txt.write(sen1)
txt.write('\n')
txt.write(sen2)
txt.close()
txtmine = open(filename, 'r')
print(txtmine.read())
txtmine.close()"""




