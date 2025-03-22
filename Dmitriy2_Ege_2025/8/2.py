import itertools
k = 0
for x in itertools.product(sorted('КОДИМ'), repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('М') == 2 and x.count('ММ') == 0:
        print(k, x)