import itertools
def F(x, y, z, w):
    return ((not x) <= y) and ((not y) == z) and w
for i in itertools.product([0, 1], repeat=8):
    table = [(0, i[0], 0, i[1]),
             (0, i[2], i[3], i[4]),
             (i[5], 0, i[6], i[7])]
    if len(set(table)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)