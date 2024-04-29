import itertools
k = 0
for x in itertools.product(sorted('ОСЕЮГХНТ'), repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'Н' and x.count('О') >= 2 and 'С' not in x:
        print(k, x)