import itertools
k = 0
for x in itertools.product(sorted('КОТЕНА'), repeat=7):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and sorted(x) == sorted('КОТЕНОК'):
        print(k, x)