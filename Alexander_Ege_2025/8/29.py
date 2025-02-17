import itertools
k = 0
for x in itertools.product(sorted('БАРШ'), repeat=5):
    k += 1
    x = ''.join(x)
    if len(set(x)) == 4:
        if x.count('Б') + x.count('Р') + x.count('Ш') <= 3:
            print(k, x)