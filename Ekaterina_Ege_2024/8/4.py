import itertools
k = 0
for x in itertools.permutations("АГЕИМРС"):
    k += 1
    x = ''.join(x)
    if k == 1899:
        print(k, x)