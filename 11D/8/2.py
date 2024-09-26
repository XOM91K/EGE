import itertools
k = 0
for x in itertools.product(sorted('НОРМАЛЬЕ'), repeat=6):
    k += 1
    x = ''.join(x)
    if x == 'НЕНОРМ':
        print(k)
    if 'НОРМ' == x[:4]:
        print(k)
        break
        # 137588
        # 154817
print(154817 - 137588 - 1)