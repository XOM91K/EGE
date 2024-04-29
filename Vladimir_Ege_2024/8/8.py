import itertools
k = 0
for x in itertools.product(sorted('КОМПЬЮТЕР'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 == 1 and x[0] != 'Ь' and x.count('К') == 2:
        print(k, x)