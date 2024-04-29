import itertools
ct = 0
for x in set(itertools.permutations('АМФИБРАХИЙ')):
    x = ''.join(x)
    if 'ИИФАА' in x or 'ААФИИ' in x:
        ct += 1
        print(x)
print(ct)