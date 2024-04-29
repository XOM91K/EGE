from itertools import *
c = 0
for x in product('01234567', repeat=8):
    x = ''.join(x)
    if x[0] != '0':
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        if x[0] == x[-1] == '1' and '00' in x and '000' not in x:
            c += 1

print(c)