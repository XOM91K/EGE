import itertools
k = 0
for x in itertools.product('БДЕКНТЦЧЭ', repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 == 0:
        if x[0] != 'Н' and x[-1] != 'Н':
            if x.count('Е') >= 3:
                print(k)