import itertools
k = 0
ct = 0
for x in itertools.product('ВЕЛНРХ', repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[:2] == 'ЕН':
        ct += 1
print(ct)