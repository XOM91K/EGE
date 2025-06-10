import itertools

k = 0
for x in itertools.product('БНПЭ', repeat=4):
    x = ''.join(x)
    k += 1
    if not(x[0] == 'П' or x[-1] == 'П' or 'ЭЭ' in x):
        if k % 2 == 0:
            print(k,x)
