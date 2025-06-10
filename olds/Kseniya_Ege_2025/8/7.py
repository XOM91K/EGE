import itertools
n = 0
for x in itertools.product('БДЕКНТЦЧЭ', repeat=6):
    x = ''.join(x)
    n += 1
    if n % 2 == 0 and x[0] != 'Н' and x[-1] != 'Н' and x.count('Е') >= 3:
        print(n, x)