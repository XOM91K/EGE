import itertools
k = 0
for x in set(itertools.permutations('АМФИБРАХИЙ')):
   x = ''.join(x)
   if 'ААФИИ' in x or 'ИИФАА' in x:
       k += 1
print(k)