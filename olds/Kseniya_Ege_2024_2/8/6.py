import itertools
ct = 0
for x in itertools.permutations('0123456789abcdef', 3):
    if x[0] != '0':
        x = ''.join(x)
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        x = x.replace('8', '0')
        x = x.replace('a', '0')
        x = x.replace('c', '0')
        x = x.replace('e', '0')
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        x = x.replace('9', '1')
        x = x.replace('b', '1')
        x = x.replace('d', '1')
        x = x.replace('f', '1')
        if '00' not in x and '11' not in x:
            ct += 1
print(ct)