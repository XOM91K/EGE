import itertools
ct = 0
for x in itertools.product('0123456789ABC', repeat = 6):
    x = ''.join(x)
    if x[0] != '0' and x.count('0') >= 2:
        if x.count('A') + x.count('B') + x.count('C') == 2:
            x = x.replace('B', 'A')
            x = x.replace('C', 'A')
            if 'AA' in x:
                ct += 1
print(ct)