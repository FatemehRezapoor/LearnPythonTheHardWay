# May 31, 2018
# Exercise 11-13
# ** ASK FOR INPUT FROM USER **
print('How old are you?')
age = input()
print('How tall are you?')
height = input()
print('I am %s years old and I am %r tall' % (age, height))  # The user input is string

# Another Method to combine print with input command
age = input('How old are you:')
print('I am %s years old' % age)

# My Tiny project: Ask for numbers from user and add them up
print('Please enter two numbers')
a = int(input())
b = int(input())
print(a + b)
