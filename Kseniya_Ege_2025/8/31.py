import itertools
k = 0
for x in itertools.product('АБРШ', repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('Б') + x.count('Р') + x.count('Ш') <= 3:
        if len(set(x)) == 4:
            print(k, x)