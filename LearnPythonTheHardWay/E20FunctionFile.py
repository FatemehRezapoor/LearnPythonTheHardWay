# June 1 , 2018
# This exercise is used to make function to read a text file
# IMPORTANT POINT: Whenever you read a file, the cursor gors to the end of the file. So if you want to read it again the
# out put will be EMPTY unless you use txt.seek(0) which will remove the cursor to the beginning of the file or to the
# location you want to
# function is dealing in bytes, not lines. So that’s going to the 0 byte (first byte) in the file

from sys import argv

script, file = argv

txt = open(file, 'r')


def read_all(arg1):
    print(arg1.read())


def read_half(arg1):
    print(arg1.seek(0))  # moves the cursor to the beginning of the file


def read_line(linecount, arg2):
    print(linecount, arg2.readlines())


read_all(txt)
read_half(txt)
read_line(1, txt)

# Mini project: how to read the whole text file with readline()

txt.seek(0)
for line in txt:
    print(line)

# Important point: If you go txt.readline(3) it only prints out the 3 charactros of your line

txt.seek(5) # moves the cursor to the 5th charactor
print(txt.read())
