import itertools
def F(x, y, z, w):
    return ((x <= y) or (z <= w)) and (not(x <= w))
for i in itertools.product([0, 1], repeat=5):
    table = [(1, 0, 1, i[0]), (1, i[1], i[2], 1), (i[3], i[4], 1, 0)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 1, 1]:
                print(j)