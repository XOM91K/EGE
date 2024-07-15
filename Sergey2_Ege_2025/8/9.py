import itertools
k = 0
ct = 0
for x in itertools.product(sorted('ЧРМЮЗНАДЯ'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 2 != 0 and x[0] == 'А' and x.count('Ю') == 2:
        ct += 1
print(ct)