import itertools
def f(x, y, z, w):
    return w <= (y != (z <= x))
for i in itertools.product([0, 1], repeat=5):
    table = [(i[0], 1, 1, 1), (0, i[1], i[2], 0), (i[3], i[4], 0, 0)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 0, 0]:
                print(j)