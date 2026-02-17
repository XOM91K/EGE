import itertools
k = 0
for x in itertools.product(sorted('БАРШ'), repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('Б') + x.count('Р') + x.count('Ш') <= 3:
        povt2 = [d for d in x if x.count(d) == 2]
        povt1 = [d for d in x if x.count(d) == 1]
        if len(povt2) == 2 and len(povt1) == 3:
            print(k)