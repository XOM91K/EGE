import itertools
k = 0
for x in itertools.product('ЕКМОСЧ', repeat=4):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] == 'Ч' and x[3] == 'О':
        print(k, x)