import itertools
ct = 0
for x in itertools.permutations('012345678', 7):
    x = ''.join(x)
    if x[0] != '0' and '2' not in x:
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        x = x.replace('8', '0')
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        if '00' not in x and '11' not in x:
            ct += 1
print(ct)