import itertools
def F1(x, y, z, w):
    return (x <= y) or ((not w) == z)
def F2(x, y, z, w):
    return (x <= y) == (w and (not z))
for i in itertools.product([0, 1], repeat=6):
    table = [(i[0], i[1], i[2], 0),
             (i[3], i[4], 0, 0),
             (i[5], 0, 0, 0)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F1(**dict(zip(j, r))) for r in table] == [F2(**dict(zip(j, r))) for r in table]:
                print(j)