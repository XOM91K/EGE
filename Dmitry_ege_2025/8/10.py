import itertools
t = 0
for x in itertools.product(sorted('ТБДЦЭЕКНЧ'), repeat=5):
    x = ''.join(x)
    t += 1
    if t % 2 == 0:
        if x[0] != 'Н' and x[-1] != 'Н' and x.count('Е') >= 3:
            print(t, x)
    #if x % 2 and x[0] != 'Н' and x[-1] != 'Н' and x.count('Е') > 2:
        #print(x)
# s = 'АВГДЖЕЗЯ'
# print(s, ''.join(sorted(s)))