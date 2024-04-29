import itertools
ct = 0
for x in itertools.permutations('01234567', 5):
    x = ''.join(x)
    if x[0] != '0' and '1' not in x:
        x = x.replace('2', '0')
        x = x.replace('4', '0')
        x = x.replace('6', '0')
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        if '11' not in x and '00' not in x:
            print(x)
            ct += 1
print(ct)