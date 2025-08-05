import itertools
k = 0
for x in itertools.product('ГЖИМФЧЯ', repeat=6):
    x = ''.join(x)
    k += 1
    if x[:2] == 'ЖЯ':
        print(k, x)