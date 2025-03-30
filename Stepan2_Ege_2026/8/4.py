import itertools
k = 0
for x in itertools.product(sorted('КОДИМ'), repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('М') == 2 and 'ММ' not in x:
        print(k, x)