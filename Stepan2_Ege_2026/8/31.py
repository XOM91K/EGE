import itertools
ct = 0
for x in itertools.product('012345678', repeat=4):
    x = ''.join(x)
    if x.count('8') == 1 and x[0] != '0':
        lt = x[:x.index('8')]
        rt = x[x.index('8') + 1:]
        lt = sum(map(int, lt))
        rt = sum(map(int, rt))
        if lt == rt:
            ct += 1
print(ct)