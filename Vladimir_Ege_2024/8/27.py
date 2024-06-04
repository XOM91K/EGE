import itertools
k = 0
for x in itertools.permutations(sorted('ВАРВАРА')):
    s = ''.join(x)
    k += 1
    if k % 2 == 0 and s[0] == 'В' and 'ААА' in s and 'РР' not in s:
        print(k, s)