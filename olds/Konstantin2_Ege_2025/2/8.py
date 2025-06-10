import itertools
def f(x, y, z, w):
    return (w or x or y) <= ((y or z) and x or y and (w or z))
for i in itertools.product([0, 1], repeat=5):
    table = [(0, 0, 0, i[0]),
             (i[1], 1, 1, i[2]),
             (i[3], 1, i[4], 1)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)
