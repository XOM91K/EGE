import itertools
k = 0
for x in itertools.product(sorted('КОМПЬЮТЕР'), repeat=5):
    x = ''.join(x)
    k += 1
    if x[0] != 'Ь' and x.count('К') == 2 and k % 2 == 1:
        print(k, x)
