import itertools
def F(x, y, z, w, u):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))
for i in itertools.product([0, 1], repeat=8):
    table = [(0, i[0], 0, 0, 0),
             (0, i[1], i[2], 0, 0),
             (i[3], 0, 0, 0, i[4]),
             (0, 0, i[5], i[6], i[7])]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzwu'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0, 0]:
                print(j)