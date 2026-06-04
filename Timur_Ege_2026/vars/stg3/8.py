import itertools
k = 0
for x in itertools.product(sorted('ОДСАЦЛФЩ'), repeat=4):
    x = ''.join(x)
    k += 1
    if x[-1] != 'А' and x[0] != 'А':
        if x.count('Л') >= 3:
            if k % 2 != 0:
                print(k, x)