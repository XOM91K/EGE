import itertools
def F(x, y, z, w):
    return (x <= (z <= w) and (z <= (y == (not w))))
for i in itertools.product([0, 1], repeat=6):
    table = [(i[0], 0, 0, 0),
             (i[1], i[2], 0, 0),
             (i[3], i[4], 0, i[5])]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)