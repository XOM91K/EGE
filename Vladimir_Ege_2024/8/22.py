import itertools
k = -1
for x in itertools.product(sorted('КАЛЕЙДОСКОП')[::-1], repeat=6):
    x = ''.join(x)
    k += 1
    if (k // 4) % 2 == 0 and x[0] == 'К' and x.count('Й') >= 2 and 'С' not in x and 'Е' not in x:
        print(k // 4, x)
        break