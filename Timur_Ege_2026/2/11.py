import itertools
def F(x, y ,z, w):
    return ((not z) and y and x and (not w)) or ((not z) and y and (not x) and (not w)) or (z and y and x and (not w))
for i in itertools.product([0, 1], repeat=7):
    table = [(i[0], 1, i[1], i[2]),
             (i[3], 0, 1, i[4]),
             (0, i[5], 0, i[6]),]
    if len(set(table)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)