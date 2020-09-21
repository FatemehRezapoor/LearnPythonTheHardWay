# June 6 , 2018
# Dictionary

# You can use numbers to “index” into a list, meaning you can use numbers to fi nd out what’s in lists.
# What a dict does is let you use anything, not just numbers. Yes, a dict associates one thing to
# another, no matter what it is.
# Dictionaries are indexed by keys: string or number
# IMPORTANT: You can't use lsit as a key since list can be modified by append ,...
# The key to the dictionary needs to be immutable

# * HOW TO MAKE A DICTIONARY *
mydic={'Hi':'salam','How':'Khobi?',1:23}
myal={'a':'alef','d':'de','b':'be'}
print(mydic)

# * Other Methods to Create a dictionry *
a=[('Hi',1),('Salam',2),('Khobi',3)]
print(dict(a))

# * How to extract one lement of dictionary *

print(mydic['Hi'])
print(mydic[1])

# * How to list all keys in dictionary *

print(list(mydic.keys()))

# * How to list all keys in dictionary in sorted format *

print(sorted(myal.keys()))

# * How to add sth to dictionary *

mydic['yeki dige']='ina'
print(mydic)

# * How to delete sth from dictionary *

del(mydic[1])
print(mydic)

# * How to check if there is a key in dictionary *
print('Hi' in mydic)
print(123 in mydic)


# * How to loop in a dictionary *
for a,b in mydic.items():
    print(a,b)

# Print keys and values

print(mydic.keys())
print(mydic.values())

