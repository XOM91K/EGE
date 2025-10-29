import itertools
ct = 0
for x in set(itertools.permutations('СВЕТЛАНА', 8)):
    x = ''.join(x)
    if 'АА' not in x:
        ct += 1
print(ct)