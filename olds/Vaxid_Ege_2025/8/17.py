import itertools
k = 0
for x in itertools.product(sorted('EZGWP'), repeat = 6):
    x = ''.join(x)
    if x.count('E') <= 2:
        k = k + 1
        if x == 'EZGGWP':
            print(k, x)