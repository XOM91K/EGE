import itertools
def F(a, b, c, d):
    return ((a <= b) == c) or d
for i in itertools.product([0, 1], repeat=4):
    table = [(1, 0, 1, i[0]),
             (1, 0, i[1], 1),
             (i[2], i[3], 1, 0)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('abcd'):
            if [F(**dict(zip(j, r))) for r in table] == [0, 0, 0]:
                print(j)