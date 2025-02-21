import itertools
ct = 0
for x in itertools.permutations('ТИХОРЕЦК', 4):
    x = ''.join(x)
    if (x.count('Е') + x.count('О') + x.count('И')) == 2:
        k = 0
        if x[0] == 'Т':
            k += 1
        if x[1] == 'И':
            k += 1
        if x[2] == 'Х':
            k += 1
        if x[3] == 'О':
            k += 1
        if k == 2:
            ct += 1
print(ct)