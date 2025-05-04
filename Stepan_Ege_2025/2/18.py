import itertools
d = []
def f(x, y, z, w):
    return not((not(x <= w)) and z) and (not(w <= z)) and (x <= (not z))
for i in itertools.product([0, 1], repeat = 5):
    table = [(1, 0, i[0], 0),
             (1, 0, i[1], i[2]),
             (i[3], 1, i[4], 1)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 0, 0]:
                d.append(j)
print(len(set(d)))