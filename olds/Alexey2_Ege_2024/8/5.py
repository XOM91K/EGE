import itertools
k = 0
for x in set(itertools.permutations('СПОРТЛОТО')):
    x = ''.join(x)
    if 'ОО' in x:
        k += 1
print(k)