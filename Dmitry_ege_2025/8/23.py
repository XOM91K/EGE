import itertools
ct = 0
k = 0
for x in itertools.product (sorted('НОРМАЛЬЕ'), repeat=6):
    x = ''.join(x)
    k += 1
    if x[:4] == 'НОРМ':
        print(k, x)
    if x == 'НЕНОРМ':
        print(k, x)
#137588
#154817
# от 1 до 5 = 3
# 5 - 1 = 4 - 1 = 3
# 154817 - 137588 - 1 = 0