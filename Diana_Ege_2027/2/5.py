import itertools
def f1(x, y, z, w):
    return (x == y) and (w <= z)
def f2(x, y, z, w):
    return (x <= y) <= (w == z)
for i in itertools.product([0, 1], repeat=5):
    t = [(1, i[0], 1, 1),
         (0, 1, 0, i[1]),
         (i[2], 0, 0, i[3])]
    if len(set(t)) == 3:
        for j in itertools.permutations('xyzw'):
            if [f1(**dict(zip(j, r))) for r in t] == [1, 1, 0]:
                if [f2(**dict(zip(j, r))) for r in t] == [0, i[4], 0]:
                    print(j)