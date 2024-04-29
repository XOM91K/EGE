import itertools
ct = 0
for x in set(itertools.permutations('ПРОСТО')):
    x = ''.join(x)
    if 'ОО' not in x:
        print(x)
        ct += 1
print(ct)