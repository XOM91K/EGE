import itertools
def f(x, y, z ,w):
    return w and ((z or y) == (z and x))
for i in itertools.product([0, 1], repeat=5):
    table = [(0, i[0], 0, i[1]), (i[2], i[3], 1, 0), (0, 1, i[4], 0)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 0]:
                print(j)