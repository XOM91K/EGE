import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        x = x.replace('0', '#')
        x = x.replace('2', '#')
        x = x.replace('4', '#')
        x = x.replace('6', '#')
        x = x.replace('8', '#')
        x = x.replace('a', '#')
        if x.count('#') == 3 and '###' in x:
            ct += 1
print(ct)