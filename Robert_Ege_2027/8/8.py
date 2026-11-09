import itertools
ct = 0
for x in itertools.permutations('012345678', r=7):
    x = ''.join(x)
    if '2' not in x and x[0] != '0':
        x = x.replace('1', 'z')
        x = x.replace('3', 'z')
        x = x.replace('5', 'z')
        x = x.replace('7', 'z')
        x = x.replace('0', 'v')
        x = x.replace('2', 'v')
        x = x.replace('4', 'v')
        x = x.replace('6', 'v')
        x = x.replace('8', 'v')
        if 'zz' not in x and 'vv' not in x:
            ct += 1
            print(x)
print(ct)