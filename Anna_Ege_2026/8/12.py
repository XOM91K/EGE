import itertools
from itertools import repeat
k = 0
for x in set(itertools.permutations('АМФИБРАХИЙ', 10)):
    x = ''.join(x)
    if 'ААФИИ' in x or 'ИИФАА' in x:
        k += 1
print(k)