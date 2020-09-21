# ** TINY PROJECT: LET'S USE ARGV AND USER INPUT TOGETHER **
# May 31, 2018
# Exercise 14
from sys import argv

script, user_name = argv
message = 'Please inter here:'
print('Hello %s, I am %s python script' % (user_name, script))
print('Do you like me %s' % user_name)
input(message)
print('Where are you from %s' % user_name)
country = input(message)
print("""This is what I know about you:
        \nYou are from %s""" % country)
