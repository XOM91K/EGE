import itertools
def F(x, y, z, w):
    return w <= ((z <= y) and x)
for i in itertools.product([0, 1], repeat=4):
    t = [(0, i[0], 1, 0),
         (i[1], 1, 1, 0),
         (0, i[2], 0, i[3])]
    if len(set(t)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in t] == [0, 1, 0]:
                print(j)
