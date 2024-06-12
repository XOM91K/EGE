import itertools
def f(x, y, z, w):
    return w and ((not x) or y) and (((not y) and z) or (y and (not z)))
for i in itertools.product([0, 1], repeat=3):
    table = [(0, 0, i[0], i[1]),
             (i[2], 0, 0, 1),
             (1, 0, 0, 1)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)