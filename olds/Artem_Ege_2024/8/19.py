import itertools
k = 0
for x in itertools.product('АПРСУ', repeat=5):
    x = ''.join(x)
    k += 1
    if x.count('У') <= 1 and 'АА' not in x:
        print(k, x)