import itertools
k = 0
for x in set(itertools.permutations('АМФИБРАХИЙ')):
    x = ''.join(x)
    if x[4] == 'Б' and x[5] == 'Р':
        k+=1
print(k)