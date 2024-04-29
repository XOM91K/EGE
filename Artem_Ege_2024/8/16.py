import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=8):
    x = ''.join(x)
    if x[0] != '0' and (x.count('2') + x.count('3') + x.count('5') + x.count('7') + x.count('b')) >= 2:
        last = x[-1]
        if x[-1] in 'a':
            last = 10
        if x[-1] in 'b':
            last = 11
        last = int(last)
        one = x[0]
        if x[0] in 'a':
            last = 10
        if x[0] in 'b':
            last = 11
        one = int(x[0])
        if one % 2 != last % 2:
            ct += 1
print(ct)