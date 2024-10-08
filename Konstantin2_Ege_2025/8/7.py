import itertools
k = 0
for x in itertools.product('567', repeat=12):
    x = ''.join(x)

    if "55" not in x:
        k += 1
        print(k, x)