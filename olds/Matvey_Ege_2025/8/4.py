import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    if x[-1] in '456' and x[0] != '0':
        x = x.replace('0', '2')
        x = x.replace('4', '2')
        x = x.replace('6', '2')
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        if x.count('2') == x.count('1'):
            ct += 1
print(ct)