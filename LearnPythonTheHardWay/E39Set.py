# July, 8, 2020
# Set

# * HOW TO MAKE A SET *
myset = set('acdefj')
print(myset) # each time that you print, it will sort them in random. No duplication will be printed

# * HOW TO SORT SET
print(sorted(myset))

# COMBINE SETS
myset2=set('gbhijkl')
print(sorted(myset | myset2)) # print memebers in a or b
print(sorted(myset & myset2)) # Prints the only memebers in both

# MAKE SET FROM ANOTHER SET

Myset3 = { x for x in 'Super'}
print(Myset3)
myset4 = { x for x in 'Super' if x not in 'pd'}
print(myset4)