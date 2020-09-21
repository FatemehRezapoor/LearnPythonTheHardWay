# June 1, 2018

# function that return sth

# Function with one value to return
def mysym(a,b):
    print('Here is your summation results')
    return a+b


print(mysym(2,3))


# Example 1: Function with two values to return
def symmulti(a,b):
    s=a+b
    m=a*b
    return s,m

s,m=symmulti(2,3)
print('Here is summation %d and here is multiple %d:' %(s,m))