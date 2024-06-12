import itertools
def f(x, y, z, w):
    return (x and y) or ((z == y) and w)
for i in itertools.product([0, 1], repeat=7):
    table = [(i[0], i[1], 1, 1),
             (i[2], 0, 0, i[3]),
             (i[4], 0, i[5], 0),
             (i[6], 0, 0, 0)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [0, 0, 1, 1]:
                print(j)