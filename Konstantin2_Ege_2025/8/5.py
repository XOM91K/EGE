import itertools
k = 0
for x in itertools.product(sorted('ТБДЦЭЕКНЧ'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] != 'Н' and x[-1] != 'Н':
        if x.count('Е') >= 3:
            print(k, x)
            break