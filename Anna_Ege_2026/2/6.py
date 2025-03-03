import itertools
def F(x, y, z, w):
    return x <= ((z <= y) <= w)
for i in itertools.product([0, 1], repeat=5):
    table = [(i[0], 1, 0, 0),
             (1, i[1], 0, i[2]),
             (0, i[3], i[4], 0)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 0, 0]:
                print(j)
print(dict(zip(('z', 'w', 'x', 'y'), (0, 1, 0, 0))))