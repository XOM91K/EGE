import itertools
k = 0
for x in itertools.product(sorted('СТАРЫ'), repeat=5):
    x = ''.join(x)
    k += 1
    nepovt = [y for y in x if x.count(y) == 1]
    if x[0] == 'С' and len(nepovt) == 5 and k % 2 != 0:
        print(k, x)
