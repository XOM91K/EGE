import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x[0] != '0':
        if int(x[0]) % 2 == 0:
            if x[-1] not in '036':
                if x.count('6') >= 1:
                    ct += 1
print(ct)