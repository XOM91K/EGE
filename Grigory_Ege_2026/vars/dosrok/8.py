import itertools
k = 0
for x in itertools.product(sorted('АПРЕЛЬ'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] != 'Ь' and x[0] != 'Р':
        if x.count('Л') >= 2:
            print(k, x)