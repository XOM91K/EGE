import itertools
ct = 0
for x in itertools.permutations('0123456789', 7):
    x = ''.join(x)
    if int(x) % 5 == 0 and x[0] != '0':
        x = x.replace('3',  '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        x = x.replace('9', '1')
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        x = x.replace('8', '0')
        if '11' not in x and '00' not in x:
            print(x)
            ct += 1
print(ct)