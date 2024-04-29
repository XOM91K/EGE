import itertools
k = 1
for x in  itertools.product('АЕКПТЧ', repeat = 7 ):
    x = ''.join(x)
    k += 1
    if x == 'АПТЕЧКА':
        print(k)
    if x == 'ПЕЧАТКА':
        print(k)
