import itertools
glas = 'О'
k = 0
for x in set(itertools.permutations('СПОРТЛОТО')):
    x = ''.join(x)
    if x[-1] != glas:
        k += 1
print(k)