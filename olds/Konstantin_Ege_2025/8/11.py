import itertools
k = 0
s = []
for x in itertools.permutations('АААВВРР', 7):
    x = ''.join(x)
    if x not in s:
        s.append(x)
        k += 1
        if k % 2 == 0 and x[0] == 'В' and 'ААА' in x and 'РР' not in x:
            print(k, x)