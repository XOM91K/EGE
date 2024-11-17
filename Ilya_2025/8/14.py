import itertools
ct = 0
for x in set(itertools.permutations('АМФИБРАХИЙ')):
    x = ''.join(x)
    if x[4:6] == 'БР':
        ct += 1
print(ct)