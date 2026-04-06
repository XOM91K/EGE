import itertools
k = 0
for x in sorted(set(itertools.permutations(sorted('ВАРВАРА'), 7))):
    x = ''.join(x)
    k += 1
    #print(k, x)
    if k % 2 == 0 and x[0] == 'В' and x.count('А') == 3 and 'ААА' in x and 'РР' not in x:
        print(k, x)
# s = 'abracadabra'
# print(set(s))