import itertools
k = 0
for x in itertools.product(sorted('ПЛЮШКА'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'А' and len(set(x)) == 6:
        print(k, x)
