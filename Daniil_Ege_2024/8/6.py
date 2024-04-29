import itertools
g = 0
for x in itertools.product(sorted('УЦЮТПСОШ'), repeat=6):
    x = ''.join(x)
    g += 1
    if x == 'ЮШОССО':
        print(g, x)