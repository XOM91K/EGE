import itertools

ct = 0
for x in itertools.product('0123456789ABC', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('0') >= 2:
            x = x.replace('B', 'A').replace('C', 'A')
            if x.count('A') == 2 and 'AA' in x:
                ct += 1
                print(x)
print(ct)
