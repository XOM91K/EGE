import itertools
k = 0 #когда заводим переменную для порядкового номера, то называем
# её "k" обязательно именно так
for x in itertools.product(sorted('УЦЮТПСОШ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x == 'ЮШОССО':
        print(k, x)