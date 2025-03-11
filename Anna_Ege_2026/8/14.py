import itertools
k = 0
for x in itertools.permutations('012345678', r = 7):
    x = ''.join(x)
    if '2' not in x and x[0] != '0':
        x = x.replace('4', '2')
        x = x.replace('6', '2')
        x = x.replace('8', '2')
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        if '22' not in x and '02' not in x and '20' not in x and '11' not in x:
            k += 1
print(k)