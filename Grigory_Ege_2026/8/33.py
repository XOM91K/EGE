import itertools
ct = 0
for x in itertools.product('0123456789AB', repeat=7):
    x = ''.join(x)
    if x[0] != '0':
        for i in '124578AB':
            x = x.replace(i, '/')
        for c in '0369':
            x = x.replace(c, '*')
        if '//' not in x and '**' not in x:
            ct += 1
print(ct)