import itertools
k = 0
for x in itertools.product(sorted('ТИМАШЕВСК')[::-1], repeat=5):
    x = ''.join(x)
    k += 1
    if x[2] in 'ТМШВСК' and x[0] in 'ИАЕ' and x[1] in 'ИАЕ' and x[3] in 'ИАЕ' and x[4] in 'ИЕА':
        print(k, x)