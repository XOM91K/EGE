import itertools
ct = 0
for x in itertools.product('012345678', repeat=6):
    x = ''.join(x)
    if x[0] != '0' and x.count('1') >= 2 and x[-1] != '2' and x[-1] != '3':
        x = x.replace('0', '@')
        x = x.replace('1', '#')
        x = x.replace('2', '@')
        x = x.replace('3', '#')
        x = x.replace('4', '@')
        x = x.replace('5', '#')
        x = x.replace('6', '@')
        x = x.replace('7', '#')
        x = x.replace('8', '@')
        if x[0] != '#':
            ct += 1
print(ct)