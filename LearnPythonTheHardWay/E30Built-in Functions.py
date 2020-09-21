# July 13, 2020
# BUILT IN FUNCTIONS

# **MATHEMATIC**

# INT: It is a constructor for integer type

x='47'
print(type(x))
print(type(int(x)))
print(int(47.5))

# ABS: It prints the absolute value

print(abs(-75.6))

# Divmode: It returns the remaining and division result of division

print(divmod(47,3))

# Complex: Creates a complex number

y = complex(3,5)
print(y)

# ** CONTAINER FUNCTIONS **

a=(1,2,3,4,5)
print(a)
# len: Length of a
print(len(a))

# reversed: Get a reversed tupil
b=reversed(a)
print((reversed(a)))
for i in b:
    print(i)

# list: To get a list
print(list(reversed(a)))

# Sum: to get a summation
print(sum(a))

# Max,Min: Largest + Smallest value

print(max(a))

# Any: Boolean which checks for true values ( all numbers are more than 1 so you get ture)

print(any(a))

# Zip: Zipping tupils together

a= (1,2,3,4)
b= (5,6,7,8)
z= zip(a,b)
for i in z:
    print(i)

# enumerate: Gives us index and the value

a= ('cat','dog')
for i,v in enumerate(a):
    print('Counter is {} and value is {}'.format(i,v))

# ** OBJECT FUNCTION **
x=42

# isinstance: To check for the type

print(isinstance(x,int))
print(isinstance(x,float))

