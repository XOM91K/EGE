import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x[0] != '0' and x[-1] not in '347':
        k = 0
        for y in '012345678':
            k += x.count(y + y + y)
        if k == 0:
            ct += 1
print(ct)