import itertools
def F(x, y, z, w):
    return (z == w) and (x <= y) or (not w)
for i in itertools.product([0, 1], repeat=11):
    table = [(i[0], i[1], 0, 0),
             (i[2], 0, 0, 0),
             (i[3], 0, 0, i[4]),
             (i[5], i[6], i[7], 0),
             (i[8], i[9], 0, i[10])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0, 0, 0]:
                print(j)