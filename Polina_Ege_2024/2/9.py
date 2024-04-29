import itertools
def f(a, b, c, d):
    return ((a and b) <= c) and ((b and c) <= d)
for i in itertools.product([0, 1], repeat=6):
    table = [(i[0], 1, 1, 1),
             (i[1], 1, i[2], 1),
             (1, 1, 1, i[3]),
             (i[4], 1, 1, i[5])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('abcd'):
            if [f(**dict(zip(j, r))) for r in table] == [0, 0, 0, 0]:
                print(j)