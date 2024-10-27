import itertools
def F(x, y, z, w):
    return (x and (not y)) or (y == z) or (not w)
for i in itertools.product([0, 1], repeat=4):
    table = [(1, i[0], 0, 0),
             (i[1], 0, i[2], 0),
             (1, 0, 1, i[3])]
    if len(set(table)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)