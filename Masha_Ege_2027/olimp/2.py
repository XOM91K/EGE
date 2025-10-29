import itertools
ct = 0
for x in itertools.product('xyz', repeat=9):
    x = ''.join(x)
    if x.count('x') == 3 and x.count('y') >= 1 and x.count('z') <= 2:
        ct += 1
print(ct)