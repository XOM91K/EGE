import itertools
ct = 0
for x in set(itertools.permutations('НОСОЧЕЧКИ')):
    x = ''.join(x)
    x = x.replace('Е', 'О')
    x = x.replace('И', 'О')
    x = x.replace('С', 'Н')
    x = x.replace('Ч', 'Н')
    x = x.replace('К', 'Н')
    if 'НН' not in x and 'ОО' not in x:
        print(x)
        ct += 1
print(ct)