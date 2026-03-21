import itertools
a = set()
ct = 0
for i in set(itertools.permutations(sorted(list('АМФИБРАХИЙ')))):
    i = ''.join(i)
    if 'ААФИИ' in i or 'ИИФАА' in i:
        ct += 1
print(ct)