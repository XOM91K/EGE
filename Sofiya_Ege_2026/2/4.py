import itertools
def F(x, y, z, w):
    return w or (y <= z) and x
for i in itertools.product([0, 1], repeat=6):
    table = [(i[0], i[1], 0, 0),
             (1, 1, i[2], i[3]),
             (1, i[4], i[5], 1)]
    if len(set(table)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 0, 0]:
                print(j)