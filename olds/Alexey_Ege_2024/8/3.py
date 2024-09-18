import itertools
k = 0
ct = 0
for x in itertools.product(sorted('БЮУОФЦЖ'), repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0:2] == 'ЖО':
        ct += 1
print(ct)
