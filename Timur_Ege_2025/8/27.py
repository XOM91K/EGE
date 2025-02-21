import itertools
k = 0
for x in itertools.product(sorted('НОРМАЛЬЕ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[0:4] == 'НОРМ':
        print(k, x)
    if x == 'НЕНОРМ':
        print(k, x)
#137588
#154817

#[1, 5]
