import itertools
k = 0
for x in itertools.product(sorted('ЛИСЁНОК'), repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('Ё') >= 2 and x[0] != 'О' and x[1] == 'К':
        print(k, x)