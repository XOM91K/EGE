import itertools
ct = 0
for x in itertools.permutations('ТИХОРЕЦК', 4):
    x = ''.join(x)
    gl = x.count('И') + x.count('О') + x.count('Е')
    if gl == 2:
        #ТИХО
        ct_pos = 0
        if x[0] == 'Т':
            ct_pos += 1
        if x[1] == 'И':
            ct_pos += 1
        if x[2] == 'Х':
            ct_pos += 1
        if x[3] == 'О':
            ct_pos += 1
        if ct_pos == 2:
            ct += 1
print(ct)