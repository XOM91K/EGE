import itertools
k = 0
for x in itertools.product(sorted('тбдцэекнч'), repeat=6):
    x = ''.join(x)
    k += 1
    if k % 2 == 0 and x[0] != 'н' and x[-1] != 'н' and x.count('е') >= 3:
        print(k, x)