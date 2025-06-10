import itertools
k = 0
for x in itertools.product('БВЕКЛОУФ', repeat=5):
    x = ''.join(x)
    k += 1
    if x[0] == 'Ф' and x[-1] == 'Л':
        print(k, x)