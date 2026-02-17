import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=7):
    x = ''.join(x)
    if x[0] != '0':
        x = x.replace('0', '3')
        x = x.replace('6', '3')
        x = x.replace('9', '3')
        x = x.replace('1', '2')
        x = x.replace('4', '2')
        x = x.replace('5', '2')
        x = x.replace('7', '2')
        x = x.replace('8', '2')
        x = x.replace('a', '2')
        x = x.replace('b', '2')
        if '33' not in x and '22' not in x:
            ct += 1
print(ct)