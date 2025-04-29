import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    if x[-1] in '4546' and x[0] != '0':
        x = x.replace('0', '!')
        x = x.replace('1', '#')
        x = x.replace('2', '!')
        x = x.replace('3', '#')
        x = x.replace('4', '!')
        x = x.replace('5', '#')
        x = x.replace('6', '!')
        if x.count('!') == x.count('#'):
            ct += 1
print(ct),