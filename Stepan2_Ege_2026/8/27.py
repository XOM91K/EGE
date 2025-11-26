import itertools
ct = 0
for x in itertools.product('0123456789ABCDE', repeat=8):
    x = ''.join(x)
    if x.count('0') == 2 and x[0] != '0' and x.count('A') + x.count('B') + x.count('C') + x.count('D') + x.count('E') <= 4:
        ct += 1
print(ct)