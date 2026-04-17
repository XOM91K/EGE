import itertools
k = 0
for x in itertools.product(sorted('ЯНВАРЬ'), repeat=5):
    x = ''.join(x)
    k += 1
    if x[0] != 'Я' and x.count('Ь') <= 1 and x.count('ЯЯ') == 0:
        print(k, x)