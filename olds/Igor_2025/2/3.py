import itertools
def F1(x, y, z, w):
    return (x == y) and (w <= z)
def F2(x, y, z, w):
    return (x <= y) <= (w == z)
for i in itertools.product([0, 1], repeat=5):
    table = [(1, i[0], 1, 1),
             (0, 1, 0, i[1]),
             (i[2], 0, 0, i[3])]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F1(**dict(zip(j, r))) for r in table] == [1, 1, 0]:
                if [F2(**dict(zip(j, r))) for r in table] == [0, i[4], 0]:
                    print(j)