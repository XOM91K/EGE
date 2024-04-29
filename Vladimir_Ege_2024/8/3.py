import itertools
ct = 0
for x in set(itertools.product('POLYGON', repeat=5)):
    x = ''.join(x)
    if x[2] in 'OY' and x == x[::-1]:
        ct += 1
print(ct)