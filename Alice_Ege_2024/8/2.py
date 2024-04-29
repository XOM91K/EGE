import itertools
k = 0
ct = 0
for x in itertools.product('БЖОУФЦЮ', repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[:2] == 'ЖО':
        ct += 1
        print(k, x)
print(ct)