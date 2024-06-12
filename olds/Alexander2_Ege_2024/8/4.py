import itertools
ct = 0
for x in set(itertools.permutations('БИТКОИН')):
    x = ''.join(x)
    print(x)
    ct += 1
print(ct)
