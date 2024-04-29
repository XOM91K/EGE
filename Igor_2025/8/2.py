import itertools
ct = 0
for x in set(itertools.permutations('НОСОЧЕЧКИ')):
    x = ''.join(x)
    x = x.replace('С', 'Н')
    x = x.replace('Ч', 'Н')
    x = x.replace('К', 'Н')
    x = x.replace('Е', 'О')
    x = x.replace('И', 'О')
    if 'НН' not in x and 'ОО' not in x:
        ct += 1
print(ct)