import itertools, string
ct = 0
print(string.ascii_uppercase)
alf = '0123456789ABCDEFGHIJKLMNO'
for x in itertools.product(alf, repeat = 4):
    x = ''.join(x)
    sm_cif = 0
    if x[0] != '0':
        for y in alf:
            sm_cif += x.count(y) * alf.index(y)
        if sm_cif % 5 == 0:
            for y in alf[::2]:
                x = x.replace(y, '#')
            for y in alf[1::2]:
                x = x.replace(y, '%')
            if '##' not in x and '%%' not in x:
                ct += 1
print(ct)