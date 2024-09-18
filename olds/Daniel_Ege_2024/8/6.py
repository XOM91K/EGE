from itertools import product
k = 0
for x in product('АГДИЛНРЯ', repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] != 'Я' and x.count('Д') == 3:
        print(k, x)