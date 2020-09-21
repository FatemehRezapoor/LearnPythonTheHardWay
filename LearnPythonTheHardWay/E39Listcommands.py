# June 5, 2018
# The commands you can use for list

# * Define a list*
OneD = ['a', 'b', 'c']
TwoD = [['a', 'b', 1], ['c', 'd', 2, 4]]

# * ELEMENTS *

print(OneD[0])  # the index starts from 0 in python
print(TwoD[0])
print(TwoD[0][1])

# * LENGTH *
print(len(OneD))
print(len(TwoD))
print(len(TwoD[1]))

# * APPEND *: Add sth to the end of list
OneD.append('1')
print(OneD)
TwoD.append(['n'])
print('From Append %s' % TwoD)
TwoD[0].append('n')
print(TwoD)

# * INSERT *: Add sth to the specific point in the list
OneD.insert(0, 'man')
print(OneD)
TwoD.insert(1, 'man')
print(TwoD)

# * EXTEND *: Extends the list according to new iteration

new = [8, 8, 9]
OneD.extend(new)
print(OneD)
TwoD.extend(new)
print(TwoD)

# * REMOVE *: Removes the first item which matches with input
OneD.remove('man')
print(OneD)

# * POP *: Removes the item from list and return it
OneD.pop(0)
print(OneD)
TwoD.pop(0)
print(TwoD)

# * CLEAR *: Remove all items from the list
new.clear()
print(new)

# * INDEX *: Returns the index of input
print(OneD.index('b'))
print(TwoD.index(8))

# * COUNT *: Counts and return number of time input is repeated
print(OneD.count(8))
print(OneD)

# * REVERSE *: Reverse the list
print(OneD.reverse())
print(OneD)

#You can use reversed(formation) to return a reverse iterator of formation. 
#When you call formation.reverse() it does an in place reversal of the list 
#and returns None.

# * SORT *: Sorts the list
# print(OneD.sort())
# print(OneD)

# List
x= [1,2,3,'Hi'] # mutable
print('List:',x)
# Tuple
x=(1,2,3,'Hi') # unmutable
print('Tuple:',x)
# Dictionary
x={'a':1, 'b':2, 'c':3}
print('Dic:',x)
x=dict(a='1')
print('Dic:',x)
# Set
x={1,2,3,4} # Unordered values, it is iterable, mutable with no duplicate
print('set',x)

# CREATE LIST from LIST SEQUENCE

alist = [1,2,3,4,5]
b = [ a*2 for a in alist]
print(b)

# CREATE TUPLE FROM LIST

c = [(a,a**2) for a in alist]
print(c,type(c))

# CREATE LIST WITH IF CLAUSE

d = [a*2 for a in alist if a*2>5]
print(d)

# CREATE DICTIONARY

e = { a : a**2 for a in alist}
print(e)