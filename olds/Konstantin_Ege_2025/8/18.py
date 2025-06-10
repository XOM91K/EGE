import itertools
ct = 0
for x in itertools.product('012345', repeat=3):
    x = ''.join(x)
    if x[0] != '0' and x.count('5') >= 2:
        ct += 1
print(ct)