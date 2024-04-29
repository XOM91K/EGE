import itertools
k = 0
for x in itertools.permutations('АВГСТУ'):
    x = ''.join(x)
    k += 1
    if k == 311:
        print(k, x)