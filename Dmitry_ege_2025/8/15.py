import itertools
t = 0
for x in itertools.product(sorted('ЖЧГМЯФИ'), repeat=6):
    x = ''.join(x)
    t += 1
    if x[0] == 'Ж' and x[1] == 'Я':
        print(t, x)