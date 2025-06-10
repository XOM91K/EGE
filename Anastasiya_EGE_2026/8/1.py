import itertools
k = 0 #когда строим нумерацию переменную называем всегда "k"
for x in itertools.product(sorted('УЦЮТПСОШ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x == 'ЮШОССО':
        print(k, x)