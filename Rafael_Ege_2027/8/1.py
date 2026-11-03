import itertools
k = 0
for x in itertools.product(sorted('БЭПН'), repeat=4):
    x = ''.join(x)
    k += 1
    #if k % 2 == 0 and x[0] != 'П' and x[-1] != 'П' and 'ЭЭ' not in x:
    if k % 2 == 0 and x[0] != 'П' and x[-1] != 'П' and x.count('ЭЭ') == 0:
        print(k, x)
# 7. ББНП
# 8. ББНЭ
# 9. ББПБ
# 10 ББПН