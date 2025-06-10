import itertools
ct = 0
for x in itertools.product('0123456789AB', repeat = 7):
    x = ''.join(x)
    if x.count('B') == 2 and x[0] != '0':
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        x = x.replace('9', '1')
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        x = x.replace('8', '0')
        x = x.replace('A', '0')
        x = x.replace('B', '1')
        if  '11' not in x and '00' not in x:
            ct += 1
print(ct, x)