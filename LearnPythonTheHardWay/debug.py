#play = [[21, 22, 2],
       # [15, 36, 1],
        #[90, 1, 1]]

tset=set(play[0])
print(tset)
if len(tset)==1:
    for item in tset:
        print('Player {} is the winner!'.format(' '.join(str(item)))) # Used for loop to remove {} when printing the results

play = [[1, 1, 1],
        [15, 1, 15],
        [11, 0, 12]]



play = [[21, 22, 2,5],
        [15, 36, 1,5],
        [90, 1, 1,5],
        [15, 36, 1,5]]
pl=len(play)
emp=[]
# READ ROWS: HORIZENTAL CHECK
for i in range(0,(len(play))):
    for j in range(0,(len(play))):
        emp.append(play[i][j])
    #print(emp)
    emp=[]
# READ COLUMNS: VERTICAL CHECK
for j in range(0,(len(play))):
    for i in range(0,(len(play))):
        emp.append(play[i][j])
    #print(emp)
    emp=[]

# READ DIAGONAL: LEFT TO RIGHT
for i in range(0,(len(play))):
    j=i
    emp.append(play[i][j])
print(emp)
emp = []

# READ DIAGONAL: RIGHT TO LEFT

for i in range(0,(len(play))):
    j=(len(play)-1)-i
    emp.append(play[i][j])

print(emp)
