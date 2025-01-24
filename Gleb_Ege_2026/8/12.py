import itertools
for x in set(itertools.product('ГАЛАКТИКА', repeat=8)):
    x = ''.join(x)
    if x[0] in 'ГЛКТ' and x[-1] in 'АИ':
        print(x)