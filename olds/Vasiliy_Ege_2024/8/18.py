import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=8):
    x = ''.join(x)
    if (x.count('2') + x.count('3') + x.count('5') + x.count('7') + x.count('b')) >= 2:
        first = x[0]
        finish = x[-1]
        if x[0] == 'a':
            first = 10
        if x[-1] == 'a':
            finish = 10
        if x[0] == 'b':
            first = 11
        if x[-1] == 'b':
            finish = 11
        if int(first) % 2 != int(finish) % 2:
            ct += 1
print(ct)