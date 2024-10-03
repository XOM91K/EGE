import itertools
ct = 0
for x in itertools.product('012345', repeat=3):
    x = ''.join(x)
    if x[0] != '0' and x.count('5') == 1:
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        if '05' not in x and '50' not in x:
            ct += 1
print(ct)