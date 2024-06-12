import itertools
k = 0
l = []
for x in set(itertools.permutations(sorted('СПОРТЛОТО'))):
    x = ''.join(x)
    k += 1
    if x[0] == 'О' and x[-1] == 'О':
        l.append(x)
print(len(l))