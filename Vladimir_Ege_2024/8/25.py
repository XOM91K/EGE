import itertools
k = 0
for x in itertools.product(sorted('СВЕТА'), repeat=5):
    x = ''.join(x)
    k += 1
    if x == 'СВЕТА':
        print(k)