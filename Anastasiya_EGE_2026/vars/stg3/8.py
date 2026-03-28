import itertools
k = 0
for x in itertools.product(sorted('ОДСАЦЛФЩ'), repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] != 'А' and x[-1] != 'А' and x.count('Л') >= 3:
        print(k, x)
        break