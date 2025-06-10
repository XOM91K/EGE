import itertools
ct = 0
for x in itertools.product('0123456789ab', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        x = x.replace('9', '1')
        x = x.replace('b', '1')
        if '1111' not in x:

            print(x)
            ct += 1
print(ct)