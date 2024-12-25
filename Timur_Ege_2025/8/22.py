import itertools
ct = 0
for x in itertools.product('012345678', repeat = 4):
    x = ''.join(x)
    if x.count('8') == 1 and x[0] != '0':
        ind = x.index('8')
        if sum(map(int, x[:ind])) == sum(map(int, x[ind + 1:])):
            ct += 1
            print(x)
print(ct)