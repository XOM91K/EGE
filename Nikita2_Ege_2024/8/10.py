import itertools
k = 0
ct = 0
for x in itertools.product('ЕИКРСУЯ', repeat=6):
    k += 1
    x = ''.join(x)
    if k % 2 == 0 and x[0] != 'К' and (x.count('Е') + x.count('У') + x.count('Я') + x.count('И')) <= 2:
        ct += 1
print(ct)