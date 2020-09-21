# July, 8, 2020
# Mixed Structure

r = range (10)
l = [1, 'two', 3, {4:'four'},5]
t = ('one', None, 'five')
s = set('Wow!')
d = dict(one=r, two = l, three= s)
mixed = [l,r,d,s,t]


def disp(a):
    for a in mixed:
        print(a)

disp(mixed)

