import itertools
k = 0
for x in itertools.product(sorted('СЕНТЯБРЬ'), repeat=5):
    x = ''.join(x)
    k += 1
    if x[0] == 'Р' and 'Ь' not in x:
        print(k, x)