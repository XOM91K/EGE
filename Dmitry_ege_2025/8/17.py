import itertools
t = 0
for x in itertools.product(sorted('ГОНДУБШ'), repeat=6):
    x = ''.join(x)
    t += 1
    if t % 2 != 0 and x[0] != 'Б' and x.count('Н') >= 2 and 'У' not in x:
        print(t, x)