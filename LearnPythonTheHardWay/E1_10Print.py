# May 31, 2018
# Updated July 8, 2020
# Exercise 1-10 ( Learn python the hard way )
# ** SIMPLE PRINT EXAMPLE **
print('Hello world in Python')
print(3 + 2)  # print just a number
print('Hi', 25 + 30 / 6)  # print numbers plus words
print('.' * 10)  # print sth for 10 times

# ** PRINT VARIABLES **
car = 100
cat = 2
name = 'sara'
print('This is the number of cars:', car, 'and number of cats', cat)
print('my name is', name, 'I have', cat, 'cats')

# ** PRINT VARIABLES IN COMPRESSED FORMAT **
print('my name is %s and I have %d cats' % (name, cat))
# * Another method *
x = 'My name is %s and I am %d years old' % (name, car)
print(x)
print('This is what I learnt today: %s' % (x))
# * Another method *
x = 'I have %d apples.%s'
y = 2
a = 'Told you it will work'
print(x % (y, a))
# * Another method *
print('my name is {} and I have {} cats'.format(name, cat))
# ** PRINT AND ADD TWO VERIABLES **
x = 5
y = 2
print(x + y)
a = 'This is my text.'
b = 'Yes I saw that'
print(a + b)

# ** PRINT LONG VARIABLES **
# * Method 1 *
print('%s %s %s' % ('First line',
                    'Second line',
                    'Third line')
      )
# * Method 2 *
print("""
        This is so fun.
        lets do that again
        """)
# ** PRINT DIFFERENT FORMATS **
days = 'sat sun mon'
month = 'jan\nfeb\nmarch'
dayslist = ['sat', 'mon', 'sun']
print('This is my special day: {} and {}'.format(dayslist[2], dayslist[1]))
print(days)
print(month)
a = 'I\'m learning'
print(a)
b = '\tmy name is'
print(b)
c = 'let\'s split this line \n from here'
print(c)

# **MY TINY PROJECT: WRITE VARIABLE TO CONVERT INCH TO CM**
y = 3
print('y is=%d cm, which equals to %f inch' % (y, y / 2.54))
print('y is={} cm, which equals to {} inch'.format(y, y / 2.54))

# Print up to spesific decimal:
x = 2.356987541
print('This is x: {:,.2f}'.format(x))
