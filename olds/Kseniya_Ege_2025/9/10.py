import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    if x.count('0') == 1 and x[0] != '0':
        x = x.replace('2','0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        if x.count('0') % 2 == 0:
            ct += 1
print(ct)