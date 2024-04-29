from itertools import *
ct=0
k = 0
for x in product(sorted('привычка'),repeat=5):
    x=''.join(x)
    k += 1
    if k % 5 != 0:
        ct += 1
        if 'а' not in x and 'и' not in x and 'ы' not in x and len(set(x)) == 5:
            print(ct, x)
            break