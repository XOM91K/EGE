import itertools
def F(x, y, z, w):
    return (y <= (not(x <= z))) or w
for i in itertools.product([0, 1], repeat=7):
    table = [(i[0], 0, i[1], i[2]),
             (0, 1, i[3], i[4]),
             (1, i[5], i[6], 0)]
    if len(set(table)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)