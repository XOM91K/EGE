import itertools
k = 0
for x in itertools.product(sorted('БЭПН'), repeat=4):
    x = ''.join(x)
    k = k + 1
    if x[:1] != 'П' and x[-1:] != 'П' and x.count('ЭЭ') == 0 and k % 2 == 0:
        print(k,x)