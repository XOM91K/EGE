import itertools
def f(x, y, z, w):
    return not(x <= y) or ((not w) <= (not z)) or w
for i in itertools.product([0, 1], repeat=6):
    table = [(i[0], i[1], 1, i[2]),
             (1, 1, i[3], i[4]),
             (i[5], 1, 1, 0)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)