import itertools
for x in itertools.product('БЭПН', repeat=4):
    x = ''.join(x)
    print(x)