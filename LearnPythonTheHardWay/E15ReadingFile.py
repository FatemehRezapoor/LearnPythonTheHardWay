# June 1, 2018

# What we want to do is “open” that file in our script and print it out.

from sys import argv

script, filename, path = argv

print('Your file name is %s' % filename)
txt = open(filename, 'r')  # Open makes a file object called txt
print(txt.read())
txt.close()

# ** IMPORTANT POINT **
# Line 8 command works as long as the text file has normal ASCII or UTF-8 charactors. However when you get into wired
# letters you may get |UnicodeDecodeError| which means the program can not read some charactors in your text file
# to deal with this problem you need to introdcude encoder to the 'open' command which will act as a dictionary. It will
# give more charactor information to the program which can be used to read the file.


# MINI PROGECT: Read the text file from another directory
# path = 'D:/read.txt' (format you need to enter the directory)


newtxt = open(path, 'r')
print(newtxt.read())
newtxt.close()


# ** IMPORTANT POINT ABOUT FUNCTION **
# So here's a simpler explanation. There are two kinds of functions (actually one is technically a method but we'll
#  ignore that).
#  TYPE1: One kind of function takes an argument by putting that argument inside the parentheses. For example
# len("mystring") will return 8 because there are 8 letters in "mystring".

# TYPE 2: Another kind of function is one that is specific to a ''type or class of objects''. An example of a class is List.
# An example of a List is [1,2,3,4]. The class List has functions defined that work specifically on Lists. To use
# those functions on a specific List we would use dot notation. For example, to use the special function append on
#  a List called my_list we would write my_list.append(insert_thing_to_append).

# So when I use the open() command I am creating a class ( text file class )
# There are some specific functions which corresponds to the text file class like read. In order to cal those fucntions
# I need to use .read ( because I am calling a function inside my class to do sth on my variable)

# ** OTHER COMMANDS FOR FILE **
# readline (): Read just one line of the text
# truncate(): empties the file
# write ()
