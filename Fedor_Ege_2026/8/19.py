import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x[0] in '2468' and x[-1] in '124578':
        if x.count('6') >= 1:
            ct += 1
print(ct)