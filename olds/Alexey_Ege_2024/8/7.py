import itertools
k = 0
for x in itertools.product(sorted('БЭПН'), repeat = 4):
    x = ''.join(x)
    k +=1
    if k%2 == 0 and x[0] not in 'П' and x[3] not in 'П' and x.count('ЭЭ') == 0:

        print(k, x)