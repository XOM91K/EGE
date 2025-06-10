import itertools
k = 0
for x in itertools.permutations('АДКНОРТ', 7):
    x = ''.join(x)
    k += 1
    if k == 2233:
        print(x)