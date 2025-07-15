import itertools
k = 0
kk = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 5 != 0:
        kk += 1
        if 'И' not in x and 'Ы' not in x and 'А' not in x and len(set(x)) == 5:
            print(kk, x)