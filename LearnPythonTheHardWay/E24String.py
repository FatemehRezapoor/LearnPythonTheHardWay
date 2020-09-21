# July, 8, 2020
# STRING IN PYTHON IS AN OBJECT
# So you can call methods on strings
print('Hello'.upper())
print('Hello'.swapcase())

s='Hi.{}'
a='Tadda'
print( s+ a)
print(s.format(47+2))

# Use Format

a = 'Avali'
b = 'Dovomi'

print('Ina: {} {}'.format(a,b))
# To change the order
print('Ina: {1} {0}'.format(a,b))
# To add space
print('Ina: {0:<10} {1:>10}'.format(a,b))
# To add space and fill with zero
print('Ina: {0:<010} {1:>010}'.format(a,b))
# Let's deal with big numbers
c = 42*747+1000
print('{}'.format(c))
# To add comma
print('{:,}'.format(c))
# Specifiy the decimal places
print('{:f}'.format(c))
print('{:.3f}'.format(c))
# Split strings
s = 'salam khobi?'
print(s.split())
# Split on letter a
print(s.split('a'))
# Join the list with : charactor
sl=s.split()
s2= ':'.join(sl)
print(s2)




