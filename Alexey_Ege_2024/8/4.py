import itertools
k = 0
for x in itertools.product(sorted('ЖЮЯУЗЧДОФ'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] not in 'У' and x[5] not in 'У' and 'ЮЮ' in x:
        print(k, x)
