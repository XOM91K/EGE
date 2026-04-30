import itertools
k = 0
for x in itertools.product(sorted('СИМВОЛ'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'О' and x[0] != 'С' and x.count('В') == 1 and x.count('С') <= 1:
        print(k)