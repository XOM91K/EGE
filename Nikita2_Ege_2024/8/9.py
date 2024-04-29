import itertools
k = 0
ct = 0
for x in itertools.product('БЕЧЮ', repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] != 'Ю' and 'ЕЕ' not in x:
        print(k, x)
        ct += 1
print(ct)