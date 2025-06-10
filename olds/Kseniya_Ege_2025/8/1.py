import itertools
n = 0
for x in itertools.product('ГЖИМФЧЯ', repeat=6):
    x = ''.join(x)
    n = n + 1
    if x[0] == 'Ж' and x[1] == 'Я':
        print(n, x)