import itertools
def f(x, y, z, w):
    return (z <= w) and y and (not x)
for i in itertools.product([0, 1], repeat=5):
    t = [(0, 1, i[0], 0),
         (i[1], 0, i[2], i[3]),
         (0, 1, 1, i[4])]
    if len(set(t)) == 3:
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in t] == [1, 1, 0]:
                print(j)