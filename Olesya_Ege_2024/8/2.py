from itertools import product
c = 0
ct = 0
for x in product('БЕЧЮ', repeat=5):
    x = ''.join(x)
    c += 1
    if c % 2 == 0 and x[0] not in 'Ю' and 'ЕЕ' not in x:
        ct += 1
        print(c, x)
print(ct)