import itertools
k = 0
for x in itertools.product(sorted('барш'), repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('б') + x.count('р') + x.count('ш') <= 3:
        if len(set(x)) == 4:
            print(k,x)