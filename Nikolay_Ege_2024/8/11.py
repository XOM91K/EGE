import itertools
ct = 0
for x in itertools.product('012345', repeat=6):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('2') == 1:
            x = x.replace('1', '*')
            x = x.replace('3', '*')
            x = x.replace('5', '*')
            if '*2' not in x and '2*' not in x:
                ct += 1
print(ct)