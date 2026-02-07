import itertools

k = 0
for x in itertools.product(sorted('МИНУСОВОЙ'), repeat=4):
    x = ''.join(x)
    k += 1
    if x.count('М') + x.count('Н') + x.count('С') >= x.count('И') + x.count('У'):
        print(k, x)

