import itertools
k = 0
for x in itertools.product(sorted('РЯБИНА'), repeat=6):
    x = ''.join(x)
    k += 1
    if len(set(x)) == 6 and k % 2 != 0:
        print(k)
