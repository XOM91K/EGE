import itertools
k = 0
ct = 0
for x in itertools.product('ЬРПЛЕА', repeat=5):
    x = ''.join(x)
    k += 1
    print(k, x)
    if x[-1] == 'Ь':
        ct += 1
    if k == 387:
        break
print(ct)