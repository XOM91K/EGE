import itertools
k = 0
for x in sorted(set(itertools.product(sorted('СТАРТЫ'), repeat=5))):
    x = ''.join(x)
    k += 1
    if x[0] == 'С' and len(set(x)) == len(x) and k % 2 != 0:
        print(k, x)