import itertools
ct = 0
for x in itertools.product('0123456789abcd', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('9') == 1 and (x.count('b') + x.count('c') + x.count('d')) <= 3:
        ct += 1
print(ct)