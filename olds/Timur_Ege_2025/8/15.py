import itertools
ct = 0
for x in set(itertools.permutations('СВЕТЛАНА')):
    x = ''.join(x)
    if x.count('АА') == 0:
        ct += 1
        print(x)
print(ct)