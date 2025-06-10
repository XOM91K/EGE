import itertools
def F(x, y, z, w):
    return (x <= (y <= z)) and (y <= (z == (not w)))
for i in itertools.product([0, 1], repeat=6):
    table = [(0, 0, i[0], 0),
             (0, 0, i[1], i[2]),
             (i[3], 0, i[4], i[5])]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)