import itertools
def f(x, y, z, w):
    return (x <= y) and z and (not w)
for i in itertools.product([0, 1], repeat=4):
    table = [(0, 1, i[0], 1),
             (i[1], 1, i[2], i[3]),
             (0, 1, 1, 1)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)

