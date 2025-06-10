import itertools
k = 0
for x in itertools.product(sorted('ПОБЕДА'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] == 'О' and len(set(x)) == 6 and k % 2 == 0:
        print(k, x)