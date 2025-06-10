import itertools
k = 0
for x in itertools.product(sorted('УЦЮТПСОШ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x == 'ЮШОССО':
        print(k, x)