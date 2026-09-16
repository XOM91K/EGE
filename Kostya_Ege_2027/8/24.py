import itertools
ct = 0
for x in itertools.product('012345678',repeat=4):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('8') == 1:
            lt = sum(map(int, x[:x.index('8')]))
            rt = sum(map(int, x[x.index('8') + 1:]))
            if lt == rt:
                ct += 1
print(ct)