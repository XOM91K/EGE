import itertools
ct = 0
for x in itertools.product('012345678', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('5') == 1 and ('51' in x or '53' in x or '57' in x):
        ct += 1
print(ct)