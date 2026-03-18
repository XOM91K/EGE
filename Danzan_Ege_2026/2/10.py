import itertools
def f(x,y,z,w):
    return (not w) or ((z <= x) <= y)
for i in itertools.product([0, 1], repeat=7):
    table = [(i[0], 0, i[1], i[2]),
             (0, 1, i[3], 0),
             (i[4], i[5], i[6], 1)]
    if len(set(table)) == 3:
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)