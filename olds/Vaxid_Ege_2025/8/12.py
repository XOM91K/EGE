import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=6):
    x = ''.join(x)
    if x.count('b') == 1 and x[0] != '0':
        x = x.replace('0', '?')
        x = x.replace('2', '?')
        x = x.replace('4', '?')
        x = x.replace('6', '?')
        x = x.replace('8', '?')
        x = x.replace('a', '?')
        x = x.replace('1', '/')
        x = x.replace('3', '/')
        x = x.replace('5', '/')
        x = x.replace('7', '/')
        x = x.replace('9', '/')
        x = x.replace('b', '/')
        if x.count('?') == x.count('/'):
            ct += 1
print(ct)