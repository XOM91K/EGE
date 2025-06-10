import itertools
k = 0
for x in itertools.permutations(sorted('ВАРВАРА'), 7):
    x = ''.join(x)
    k += 1
    if (k // 6 // 2 // 2) % 2 == 0 and x[0] == 'В' and 'ААА' in x and 'РР' not in x:
        print((k // 6 // 2 // 2) , x)