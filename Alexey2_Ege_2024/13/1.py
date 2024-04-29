import itertools
ct = 0
for x in itertools.product('01', repeat=10):
    x = ''.join(x)
    if 9 + x.count('1') == 13 or 9 + x.count('1') == 11 or 9 + x.count('1') == 17:
        ct += 1
print(ct)