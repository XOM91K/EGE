import itertools
ct = 0
for x in itertools.product('0123456', repeat = 6):
    x = ''.join(x)
    if int(x[5]) >= 4 and x.count('1') + x.count('3') + x.count('5') == 3 and x[0] != '0':
        ct = ct + 1
print(ct)