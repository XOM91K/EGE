import itertools
k = 0
for x in itertools.product(sorted('СТАРЫ'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 !=0 and x[0] == 'С' and len(set(x)) == 5:
        print(k, x)