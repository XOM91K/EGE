import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    if int(x[-1]) >= 4 and x[0] != '0':
        if x.count('0') + x.count('2') + x.count('4') + x.count('6') == 3:
            ct += 1
print(ct)