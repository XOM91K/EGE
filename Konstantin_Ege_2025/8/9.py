from itertools import *
ct = 0
for x in set(permutations('АМФИБРАХИЙ', r=10)):
    x = ''.join(x)
    if x[4] == 'Б':
            if x[5] == 'Р':
                ct += 1
print(ct)