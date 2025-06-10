import itertools
ct = 0
for x in itertools.product('012345678', repeat=4):
    x = ''.join(x)
    if x.count('8') == 1 and x[0] != '0':
        pol1 = x[:x.index('8')]
        pol2 = x[x.index('8') + 1:]
        if sum(map(int, pol1)) == sum(map(int, pol2)):
            ct += 1
print(ct)