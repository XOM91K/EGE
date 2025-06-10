import itertools
k = 0
for x in itertools.product('БДЕКНТЧЦЭ', repeat = 6):
    x = ''.join(x)
    k += 1
    if x[0] != 'Н' and x[-1] != 'Н' and x.count('Е')>=3 and k % 2 == 0:
        print(k, x)