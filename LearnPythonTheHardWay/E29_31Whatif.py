# June 5, 2018
# Update: July 8, 2020
# E 29 - what if

cat = input('Inter the number of cats:')
dog = input('Inter the number of dogs:')

if cat < dog:
    print('Number of cat is smaller than dog')

if cat > dog:
    print('Number of cats is larger than dog')

if cat == dog:
    print('They are equal')

# You can use Boolean inside if command

if 5>2 and 5>4:
    print('If is working')

# ** Let's compress the commands **

if cat>dog:
    print('More cat than dog')
elif cat<dog:
    print('Less cat than dog')
else:
    print('I think they are equal')
# you can have multiplr if and else in one command

if 0<int(cat)<5:
    if 0<int(dog)<5:
        print('There are at least 5 cats and dogs in the room')
    elif 6<int(dog)<8:
        print('There are a lot of dogs in the room')
else:
    print('A lot of cats')

# Different types of conditional operators:
# 1. Comparison: equal: == , Not equal: !=, Less than or equal <= , Greater than or equal : >=
# 2. Logical operators: x and y ( true if both x and y ), x or y ( true if x or y, not x ( invert state)
# 3. Identity operator: x is y ( true if the same object), x is not y ( true if not the same object)
# 4. Memebership operator: x in y ( true if x meember of collection y ), x not in y ( true if x not member of collection y.

# Turnary operator. Only used when you want to use both if + else ( turnary = 3 conditions )

Hungary=True
x='feed the bear' if Hungary else 'Do not feed the bear'
# Means it will set 'feed the bear' string if the condition is met, if not it will set else variable.
print(x)
