from itertools import *
c = 0
ct = 0

for x in product(sorted('привычка'), repeat=5):
    x = ''.join(x)
    ct += 1
    if ct % 5 != 0:
        c += 1
        if 'а' not in x and 'и' not in x and 'ы' not in x and len(set(x)) == 5:
            print(c, x)