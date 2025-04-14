import itertools
t = 0
for x in itertools.product(sorted('ДГИАШЭ'), repeat=5):
    x = ''.join(x)
    if x[0] != 'И' and x[0] != 'А' and x[0] != 'Э' and x[-1] != 'Д' and x[-1] != 'Г' and x[-1] != 'Ш':
        t += 1
        print(t, x)