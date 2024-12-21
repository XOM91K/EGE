import itertools

ct = 0
for x in set(itertools.permutations('АМФИБРАХИЙ', 10)):
    x = ''.join(x)
    if x[4] == 'Б' and x[5] == 'Р':
        ct += 1
print(ct)
