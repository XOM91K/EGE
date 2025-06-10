import itertools
def F(x, y, z, w):
    return (((not y) <= (not w)) <= (not z)) <= x
for i in itertools.product([0,1],repeat=5):
    table = [(i[0], 1, i[1], 1),
             (0, 1, i[2], 0),
             (i[3], i[4], 1, 0)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0,1, 0]:
                print(j)