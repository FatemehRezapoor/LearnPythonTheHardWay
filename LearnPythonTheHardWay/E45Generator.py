# July 2020
# PYTHON GENERATOR
# GENERATOR IS A VARIABLE WHICH IS GENERTED BY A FOR LOOP. BUT THE DIFFERENCE IS THE VALUES ARE NOT KEPT IN THE MEMORY. SO IT IS READY FOR THE USER TO ASK FOR THE VALUE

# EXAMPLE 1 : TO SAVE THE RESULTS IN A LIST: You have to create empty list and return the value
result=[]
def myfun(mlist):
    for i in mlist:
        result.append(i*i)
    return result
x=myfun([1,2,3,4,5])
print('Simple Function: ',x)

# EXAMPLE  : Another option is to make a generator

def myfun2(mlist):
    yield (i*i for i in mlist) # Function creates a generator

mlist2=[3,2,3,5,4]
mynum=myfun2(mlist2)
print('Type:',(type(mynum)))
print('Star:',*(mynum))
print('No star:',(mynum))
print('List command: ',list(mynum))

# Example: PASS LIST INSIDE THE FUCNTION
def myfun3(mlist):
    yield [i*i for i in mlist] # Function creates a generator

mlist2=[3,2,3,5,4]
mynum=myfun3(mlist2)
print('Type:',(type(mynum)))
print('Star:',*(mynum))
print('No star:',mynum)
print('List command: ',list(mynum))


print([i*i for i in mlist2])

x= (i*i for i in mlist2)
print(type(x))
print(list(x)[:2])

# Generator is only accessible through iterative functions such as print or list. Otherwise nohing is saved in memory and it always returns []
print(list(set(x)))
x=set(i*i for i in mlist2)
print(x)
# In here we are not saving the entire results in memeory. We are yielding the results one at a time.


