import itertools
c = 0
for x in set(itertools.permutations('АМФИБРАХИЙ')):
    x = ''.join(x)
    if 'ИИФАА' in x or 'ААФИИ' in x:
        c+=1
print(c)