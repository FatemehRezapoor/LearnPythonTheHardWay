# Updated July 8, 2020
# Exercise 1-10 ( Variable )
# ** Different Types **
a = 2
b = 2.0
c = 'salam'
d = True
e = None
print(type(a),type(b),type(c),type(d),type(e))

# ** LIST AND TULIPS
# List is mutable which means we can rewrite and change the length
al = [1, '2', True]
print(al,al[1],type(al),type(al[2]))
al[1] = 'sara'
print('This is a new list: {}'.format(al[1]))
al.append('Omid')
al.insert(0,'Maman')
print('This is a new list: {}'.format(al))

# Tulip is not as flexible as a list and you can not add or change anything
at = (1, '2', [True])
print(at,at[1],type(at),type(at[2]))

# ** How to check if two variables are the same object?

if a is b:
    print('a is the same type')
else:
    print('a is a different type')

# ** How to check if the object is specific type?

if isinstance(at,list):
    print('yep')
else:
    print('Nope')

