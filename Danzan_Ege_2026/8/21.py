import itertools
k = 0
for x in itertools.product(sorted('EZGWP'), repeat = 6):
    x = ''.join(x)
    k += 1
    if x.count('E') > 2:
        k -= 1
    if x == 'EZGGWP':
        print(k, x)