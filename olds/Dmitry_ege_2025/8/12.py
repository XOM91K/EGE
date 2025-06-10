import itertools
t = 0
for x in itertools.product(sorted('БЭПН'), repeat=4):
    x = ''.join(x)
    t += 1
    if x[0] != 'П' and x[-1] != 'П' and 'ЭЭ' not in x and t % 2 == 0:
        print(t, x)