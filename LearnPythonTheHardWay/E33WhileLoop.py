# June 6 , 2018
# Updated: July 8, 2020
# While loop

i=0
number=[]

while i<6:
    print('i is equal to %d:' %i)
    number.append(i)
    i=i+1
    print(number)
print('Done')

numbers=[]

for i in range(0,6,2):  # To give different step to the for loop ( Here it is +2 step)
    print('This is the i from for loop: %d'%i)
    numbers.append(i)
    print(numbers)

# Tiny project: Ask for a username and continue asking until they enter the correct code

code= 'Minoo'
User = ''
while User != code:
    User=input('What is the code:')
print('welcome')

# LOOP CONTROLS
# 1. Continue: Short cut a loop and start the code all over again
# 2. Break: Break out of the loop prematurely and continue the execution after the entire loop
# 3. else: It will execute only if the loop ends NORMALLY, it will not execute if break is used at the loop

code= 'Minoo'
User = ''
auth = False
count = 1
max_attemp = 5
while User != code:
    if count>max_attemp:
        print('Timeout')
        break
    User=input('What is the code:')
    count += 1
else:
    auth = True
print ('Authorized to enter' if auth else 'Try later')