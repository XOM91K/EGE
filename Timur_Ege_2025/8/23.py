import itertools
ct = 0
for x in itertools.product('012345678', repeat = 7):
    x = ''.join(x)
    if x[0] not in '01357' and x[-1] not in '036' and x.count('6') >= 1:
        ct += 1
print(ct)