import itertools
def F(x, y, z, w):
    return (((not((not x) or y)) and (not w)) or (not(z and (not(y and w)))))
for i in itertools.product([0, 1], repeat=7):
    table = [(0, i[0], i[1], 0),
             (i[2], 1, i[3], i[4]),
             (1, 0, i[5], i[6])]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)