import itertools
k = 0
ct = 0
for x in itertools.product('ВЕЛНРХ', repeat=5):
    k += 1
    x = ''.join(x)
    if k % 2 != 0:
        if x[0] == 'Е' and x[1] == 'Н':
            ct += 1
            print(k, x)
print(ct)