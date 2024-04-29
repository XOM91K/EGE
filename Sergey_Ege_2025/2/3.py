import itertools
def f(x, y, z, w):
    return (x <= (z == w)) or (not(y <= w))
for i in itertools.product([0,1], repeat=7):
    table = [(i[0], 1, i[1], i[2]), (0, i[3], 0, i[4]), (i[5], 0, 0, i[6])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)
