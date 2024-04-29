import itertools
k = 0
for x in set(itertools.permutations(sorted('СПОРТЛОТО'))):
    x = ''.join(x)
    if x[0] == 'О':
        k += 1
        print(k, x)