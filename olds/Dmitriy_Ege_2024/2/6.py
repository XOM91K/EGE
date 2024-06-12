import itertools
def f(a, b, c, d):
    return (a <= b) and (b <= c) and (c <= d)
for i in itertools.product([0, 1], repeat=2):
    table = [(0, i[0], 1, 0), (0, i[1], 1, 0), (0, 1, 1, 1)]
    if len(set(table)) == len(table):
        for j in itertools.permutations('abcd'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)