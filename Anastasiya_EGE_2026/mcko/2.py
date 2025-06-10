import itertools
k = 0
for x in itertools.product(sorted('ВЕСНА'), repeat=4):
    x = ''.join(x)
    k += 1
    if 'Е' not in x and 'АА' not in x:
        print(k)