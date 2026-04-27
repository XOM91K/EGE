import itertools
k=0
for x in itertools.product(sorted('ГОНДБУШ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] != 'Б' and x.count('Н') >= 2 and x.count('У') == 0:
        if k % 2 != 0:
            print(k)