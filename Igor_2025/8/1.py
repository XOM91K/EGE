import itertools
k = 0
for x in itertools.product(sorted('БЭПН'), repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and not(x[0] == x[-1] == 'П') and 'ЭЭ' not in x:
        print(k, x)