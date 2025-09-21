import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('0') == 1:
            k = 0
            for y in '246':
                k += x.count(y)
            if k % 2 == 0:
                ct += 1
print(ct)
