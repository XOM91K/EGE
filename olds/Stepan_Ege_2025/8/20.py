import itertools
k = 0
for x in itertools.product('АВНРЬЯ', repeat = 5):
    x = ''.join(x)
    k += 1
    if x[0] != 'А' and x.count('Н') <= 1 and 'АА' not in x:
        print(k, x)
        break