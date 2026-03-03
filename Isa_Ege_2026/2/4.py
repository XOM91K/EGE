import itertools
def F1(x, y, z, w):
    return (w == x) and (y <= z)
def F2(x, y, z, w):
    return (w <= x) <= (y == z)
for i in itertools.product([0, 1], repeat=5):
    t = [(1, i[0], 1, 1),
         (i[1], 1, 0, 0),
         (i[2], 0, 0, i[3])]
    if len(set(t)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F1(**dict(zip(j, r))) for r in t] == [1, 1, 0]:
                if [F2(**dict(zip(j, r))) for r in t] == [0, i[4], 0]:
                    print(j)