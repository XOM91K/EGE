from itertools import product

cnt = 0
for x in product(sorted('УЦЮТПСОШ'), repeat=6):
    s = ''.join(x)
    cnt += 1
    if s == 'ЮШОССО':
        print(cnt, s)
