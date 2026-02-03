import itertools
k = 0
for x in itertools.product(sorted('АИКЛМЬ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] == 'К' and x[-1] == 'Ь' and len(set(x)) == 6:
        print(k, x)