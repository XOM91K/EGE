import itertools
for x in itertools.product('ПИР', repeat=3):
    x = ''.join(x)
    print(x)