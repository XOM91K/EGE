import itertools
ct = 0
k = 0
for x in set(itertools.permutations('СОВЕСТЬ')):
    x = ''.join(x)
    k += 1
    x = x.replace('В', 'С')
    x = x.replace('Т', 'С')
    x = x.replace('Ь', 'О')
    x = x.replace('Е', 'О')
    if not('СС' in x and 'ОО' in x):
        ct += 1
        print(k, x)
print(ct)