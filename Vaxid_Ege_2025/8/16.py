import itertools
k = 0
for x in itertools.product(sorted('НОРМАЛЬЕ'), repeat = 6):
    x = ''.join(x)
    k = k + 1
    if x[:4] == 'НОРМ':
        print(k, x)
    if x == 'НЕНОРМ':
        print(k, x)
#154817

#137588

# от 1 до 5
# 5 - 1 = 4 + 1