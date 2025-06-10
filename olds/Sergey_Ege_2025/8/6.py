import itertools
k = 0
ct = 0
for x in itertools.product('ЬРПЛЕА', repeat=5):
    x = ''.join(x)
    k += 1
    if x[-1] == 'Ь' and k <= 387:
        ct += 1
print(ct)