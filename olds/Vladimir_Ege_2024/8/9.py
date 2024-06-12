import itertools
k = 0
for x in itertools.product(sorted('КОМПЬЮТЕР'), repeat=5):
    k += 1
    x = ''.join(x)
    if k % 2 != 0 and x[0] != 'Ь' and x.count('К') == 2:
        print(k, x)