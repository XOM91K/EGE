import itertools
ct = 0
for x in itertools.permutations('01235', 4):
    x = ''.join(x)
    if x[0] != '0':
        x = x.replace('0', 'a')
        x = x.replace('2', 'a')
        x = x.replace('1', 'b')
        x = x.replace('3', 'b')
        x = x.replace('5', 'b')
        if 'aa' not in x and 'bb' not in x:
            ct += 1
print(ct)