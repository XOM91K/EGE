import itertools
ct = 0
for x in itertools.product('012345678',repeat = 4):
    x=''.join(x)
    if x.count('8') == 1 and x[0] != '0':
        d = x.split('8')
        d[0] = d[0] + '0'
        d[1] = d[1] + '0'
        if sum(map(int, d[0])) == sum(map(int, d[1])):
            ct += 1
print(ct)