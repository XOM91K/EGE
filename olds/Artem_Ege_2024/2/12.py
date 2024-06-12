import itertools
def F(x, y, z, w):
    return (not(x <= z) or (y == w) or y)
for i in itertools.product([0, 1], repeat=7):
    table = [(1, 0, i[0], i[1]),
             (i[2], 1, 0, i[3]),
             (0, i[4], i[5], i[6])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)