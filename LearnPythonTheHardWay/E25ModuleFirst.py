# June 1, 2018
# E25PracticeSkills is actually a module that we created
# The functions are the methods of our module
# when you call this file in terminal, it acts as a module which includes multiple functions

# split is used to split the sentence. When you type split(), python looks for space for splitting
# But you can use some other parameters like split(',') which will look for , to split the sentence

def break_word(sentence):
    # Triple double quote is used as a help for our module. When you do help(E25..) what you get is inside triple "
    """This function will break up the word for us"""

    words = sentence.split() # The output is a list
    return words


# sorts the letters in a sentence
def sort_word(words):
    return sorted(words) # the output is a list

# removes the words from a list.
def first_word(words):
    return(words.pop(0)) # pop(0) removes the first word

def last_word(words):
    return (words.pop(-1)) # pop(-1) removes the second word

# IMPORTANT POINT: HOW TO RUN THIS CODE FROM TERMINAL?
# 1- type python in terminal
# 2- change the directory of python to your module directory by: import sys  ...   sys.path.append() (Explained in pycharmtrick)

# METHOD 1:
# Each time you need to call the module/then the methd
#sentence='Hi every one'
#E25PracticeSkills.break_word(sentence)

#METHOD 2
# from E25PracticeSkills import break_word
# or if you want to improt everything from your module
# from E25PracticeSkills import *
# then you can go ahead with only your method
# break_word(sentence)









