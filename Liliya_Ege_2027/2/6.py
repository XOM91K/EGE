import itertools
def f(x, y, z, w):
    return w and ((y <= x) <= z)
for i in itertools.product([0, 1], repeat=5):
    t = [(i[0], i[1], 0, 1),
         (0, i[2], i[3], 0),
         (0, 1, i[4], 1)]
    if len(set(t)) == 3:
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in t] == [1, 1, 0]:
                print(j)