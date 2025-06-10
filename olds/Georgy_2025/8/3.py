import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x.count('8') == 1 and x[0] not in '01357' and x[-1] not in '02468':
        ct += 1
print(ct)