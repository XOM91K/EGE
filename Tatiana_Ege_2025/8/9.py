import itertools
ct = 0
for x in itertools.product('012345678', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('4') == 1:
            x = x.replace('3', '1')
            x = x.replace('5', '1')
            x = x.replace('7', '1')
            if x.count('1') == 2:
                ct += 1
print(ct)