import itertools
ct = 0
for x in set(itertools.permutations('СПОРТЛОТО')):
    x = ''.join(x)
    if x[0] == x[8]:
        print(x)
        ct += 1
print(ct)