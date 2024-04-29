import itertools
ct = 0
for x in set(itertools.permutations('СПОРТЛОТО')):
    x = ''.join(x)
    if x[0] in 'О' and x[-1] in 'О':
        ct += 1
print(ct)