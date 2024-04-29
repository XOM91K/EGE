import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x[0] not in '2460':
        if not(x[6] == x[5] == x[4]):
            ct += 1
print('количество', ct)