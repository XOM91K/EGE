import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=7):
    x = ''.join(x)
    if x[0] != '0' and x.count('b') == 2:
        k = True
        for y in itertools.product('13579b', repeat=2):
            y = ''.join(y)
            if y in x:
                k = False
        for y in itertools.product('02468a', repeat=2):
            y = ''.join(y)
            if y in x:
                k = False
        if k:
            ct += 1
print(ct)