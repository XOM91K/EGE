import itertools
k = 0
for x in itertools.product(sorted('НОРМАЛЬЕ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[:4] == 'НОРМ':
        print(k, x)
    if x == 'НЕНОРМ':
        print(k, x)
print(154817 - 137588 + 1)