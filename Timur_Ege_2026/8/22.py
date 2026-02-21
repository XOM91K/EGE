import itertools
k = 0
for x in itertools.product(sorted('СЕНТЯБРЬ'), repeat=5):
    k += 1
    x = ''.join(x)
    if k % 2 == 0 and x[0] == 'Р' and x.count('Ь') == 0:
        print(k, x)