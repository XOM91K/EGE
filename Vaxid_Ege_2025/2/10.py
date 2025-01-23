import itertools
def F(x, y, z, w):
    return (z == (not y)) and ((not x) or y) and w
for i in itertools.product([0, 1], repeat=6):
    table = [(1, i[0], i[1], 0),
             (0, 0, i[2], 1),
             (i[3], i[4], i[5], 1)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)