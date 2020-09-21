# Updated July 8, 2020
# Exercise 1-10 ( Operators )
# ** Different Types of operators in python 3**

# Normal math:
x= 5
y = 3
# 1.Division
print('This is a float output:{}'.format(x/y))
print('This is an integer output:{}'.format(x//y))
# 2. Remainder
print('This is a remainder output:{}'.format(x%y))

# 2. Unary operators
x = -x
print('This is a float output:{}'.format(x))

# 3. Bitwise operators: Operate on bits
# & and, | or, ^ Xor, << Shift left, >> shift right

# 4. Comparison operators: == equal, != Not equal, <= Less than or equal, >= Greater than or equal

# Boolean operator: and, or, not, in ( value in set), not in ( value not in sret), is ( same object identity), is not ( not same object identity)

a = True
b= False
x = ('cat','bear')
y = 'bear'

if a and b:
    print('Expression is true')
else:
    print('False')

if a or b:
    print('True')
else:
    print('False')

if not b:
    print('Expression is True')
else:
    print('False')

if y in x:
    print('Expression is True')
else:
    print('False')

if y is x[1]:
    print('True. This means they are the same object')
    print('Look, they have the same id:',id(y),' '  ,id(x[1]))
else:
    print('False')
