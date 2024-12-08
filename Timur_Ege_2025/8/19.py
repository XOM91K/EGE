import itertools
ct = 0
for x in itertools.product('0123456789abc', repeat = 6):
    x = ''.join(x)
    if x[0]!= '0' and x.count('2') == 1 and x.count('a') + x.count('b') + x.count('c') <= 4:
        ct += 1
print(ct)