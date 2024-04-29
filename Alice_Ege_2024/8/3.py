import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=3):
    x = ''.join(sorted(''.join(x)))
    if x.count('2') == 1 and x[0] != '0':
        ln = len(x[x.index('2') + 1:])
        if ln == 1:
            if x[-1] in '13579b':
                ct += 1
                print(x)
        if ln == 2:
            if x[-1] in '13579b' and x[-2] in '13579b':
                ct += 1
                print(x)
print(ct)