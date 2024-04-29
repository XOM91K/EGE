import itertools
ct = 0
for x in set(itertools.permutations('СПОРТЛОТО', 9)):
    x = ''.join(x)
    if 'ОО' in x:
        ct += 1
        print(x)
print(ct)