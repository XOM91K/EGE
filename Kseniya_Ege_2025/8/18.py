import itertools
n = 0
for x in itertools.product('ДИКМО', repeat=5):
    x = ''.join(x)
    n += 1
    if x.count('М') == 2:
        if 'ММ' not in x:
            print(n, x)