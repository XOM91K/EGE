import itertools
k = 0
for x in itertools.product(sorted('БМЮРН'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'М' and x.count('Р') >= 2 and 'Ю' not in x:
        print(k, x)