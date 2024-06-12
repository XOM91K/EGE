import itertools
k = 0
for x in itertools.product('ДЕЙНПТЬЯ', repeat=4):
    x = ''.join(x)
    k += 1
    if len(set(x)) == 4 and 'Е' not in x and 'Я' not in x:
        print(k, x)