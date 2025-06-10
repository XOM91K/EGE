import itertools
k = 0
for x in itertools.permutations('АГЕИМРС'):
    x = ''.join(x)
    k += 1
    if k == 1899:
        print(k, x)