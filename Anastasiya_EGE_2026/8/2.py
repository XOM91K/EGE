import itertools
k = 0
for x in itertools.product(sorted('ГОНДУБШ'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'Б':
        if x.count('Н') >= 2 and 'У' not in x:
            print(k)