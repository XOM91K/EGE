import itertools
def f(x, y, z, w):
    return (x <= y) and (y <= z) and (z <= w)
for i in itertools.product([0, 1], repeat=6):
    table = [(i[0], i[1], 1, 0), (i[2], 0, i[3], 1), (1, i[4], 0, i[5])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)