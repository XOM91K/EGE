import itertools
ct = 0
for x in set(itertools.permutations('АМФИБРАХИЙ', 10)):
    x = ''.join(x)
    if 'ААФИИ' in x or 'ИИФАА' in x:
        ct += 1
print(ct)