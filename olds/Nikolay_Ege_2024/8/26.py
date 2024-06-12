import itertools
ct = 0
for x in set(itertools.permutations('РОСОМАХА')):
    x = ''.join(x)
    x = x.replace('А', 'О')
    x = x.replace('С', 'Р')
    x = x.replace('М', 'Р')
    x = x.replace('Х', 'Р')
    if 'ОО' not in x and 'РР' not in x:
        ct += 1
print(ct)