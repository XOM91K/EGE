import itertools
ct = 0
for x in itertools.product('0123456789abcdef', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        if (x.count('0') + x.count('1') + x.count('2') + x.count('3') + x.count('4') + x.count('5') + x.count('6') + x.count('7') + x.count('8') + x.count('9')) == 1:
            ct += 1
print(ct)