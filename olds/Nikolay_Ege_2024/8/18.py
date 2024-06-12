import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    if x.count('3') == 1 and x[0] != '0':
        x = x.replace('1', '+')
        x = x.replace('3', '+')
        x = x.replace('5', '+')
        if '++' not in x:
            ct += 1
print(ct)