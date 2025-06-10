import itertools
k = 0
kk = 0
for x in itertools.product(sorted('ПРИВЫЧКА'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 5 != 0:
        kk += 1
        #ПРВЧК
        if 'П' in x and 'Р' in x and 'В' in x and 'Ч' in x and 'К' in x:
            if len(set(x)) == 5:
                print(kk, x)