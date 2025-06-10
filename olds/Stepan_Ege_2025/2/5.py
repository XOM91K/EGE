import itertools
def F(x, y, z, w):
    return (y <= x) and (not z) and w
for i in itertools.product([0, 1], repeat=6):
    table = [(1, 0, i[0], i[1]), (1, 1, i[2], i[3]), (i[4], 1, 1, i[5])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)