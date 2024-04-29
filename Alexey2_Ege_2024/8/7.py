import itertools
glas = 'ИАЕ'
sog_las = 'ТМШВСК'

ct = 0
for x in itertools.permutations('ТИМАШЕВСК'):
    x = ''.join(x)
    glas_ct = 0
    for q in x:
        if q in glas:
            glas_ct += 1
        elif glas_ct == 3:
            break
        else:
            glas_ct = 0
    if x[0] in sog_las and x[-1] in sog_las and glas_ct == 3:
            ct += 1
print(ct)