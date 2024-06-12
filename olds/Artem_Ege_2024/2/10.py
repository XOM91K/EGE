import itertools
def F(x, y, z, w):
    return (x or (not y)) and (not(x == z)) and w
for i in itertools.product([0, 1], repeat=4):
    table = [(i[0], 0, 0, 1),
             (0, 0, 1, 1),
             (0, i[1], i[2], i[3])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)