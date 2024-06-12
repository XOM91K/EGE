import itertools
k = 0
for x in itertools.product(sorted('ЖЮЯУЗЧДОФ'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 == 1 and x[0] != 'У' and x[-1] != 'У':
        if 'ЮЮ' in x:
            print(k)