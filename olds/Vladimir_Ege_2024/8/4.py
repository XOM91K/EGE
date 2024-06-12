import itertools
k = 0
for x in itertools.permutations(sorted('ЛЕОНАРД')):
    x = ''.join(x)
    k += 1
    if k == 4321:
        print(k, x)