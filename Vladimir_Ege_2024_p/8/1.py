import itertools
k = 0
for x in itertools.product(sorted('ФОКУС'), repeat=5):
    x = ''.join(x)
    k += 1
    if 'Ф' not in x and x.count('У') == 2:
        print(k, x)