import itertools
ct = 0
for x in itertools.product('01234567', repeat=8):
    x = ''.join(x)
    x = x.replace('2', '0')
    x = x.replace('4', '0')
    x = x.replace('6', '0')
    x = x.replace('3', '1')
    x = x.replace('5', '1')
    x = x.replace('7', '1')
    if x[0] == x[-1] == '1':
        if '00' in x and '000' not in x:
            ct += 1
print(ct)