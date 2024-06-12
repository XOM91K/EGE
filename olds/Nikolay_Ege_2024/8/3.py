import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=3):
    x = ''.join(x)
    if x[0] != '0' and x.count('2') == 1 and x[-1] != '2':
        ind = x.index('2')
        if ind == 0:
            if x[1] in '13579b' and x[2] in '13579b':
                ct += 1
        elif ind == 1:
            if x[2] in '13579b':
                ct += 1
print(ct)