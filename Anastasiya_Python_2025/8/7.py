import itertools

ct = 0
k = 0
for x in itertools.product(sorted('ВЕЧНОСТЬ'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x.count('О') >= 2 and x[0] not in 'ВЧНСТ':
        ct += 1
print(ct)