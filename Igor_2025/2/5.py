import itertools
def F(x, y, z, w):
    return (x == (y <= z)) and (y == (not(z <= w)))
for i in itertools.product([0, 1], repeat=4):
    table = [(0, 0, i[0], 0),
             (i[1], 0, i[2], 0),
             (1, 0, 1, i[3])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 1, 0]:
                print(j)