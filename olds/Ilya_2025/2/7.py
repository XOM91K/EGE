import itertools
def F(x, y, z, w):
    return (w == (z <= x)) and y
for i in itertools.product([0, 1], repeat=5):
    table = [(i[0], 0, i[1], 0),
             (1, i[2], 1, 1),
             (i[3], i[4], 0, 0)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 0, 1]:
                print(j)