from itertools import *
ct = 0
for x in set(permutations('АМФИБРАХИЙ', r=10)):
    x = ''.join(x)
    if 'ИФИ' in x or 'АФА' in x:
        ct += 1
print(ct)