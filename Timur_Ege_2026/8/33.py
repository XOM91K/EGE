import itertools

k = 0
for x in itertools.product(sorted('ПОБЕДА'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[0] == 'О' and x.count('П') == 1 and x.count('О') == 1 and x.count('Б') == 1 and x.count('Е') == 1 and x.count(
            'Д') == 1 and x.count('А') == 1:
        print(k, x)
