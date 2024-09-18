import itertools
def f(x, y, z, w):
    return(x==(z<=y)) and (not w)
for i in itertools.product([0,1],repeat=5):
    table = [(i[0], i[1], 1, i[2]), (i[3], 1, 0, 1), (0, 1, 0, i[5])]
    if len(table) ==len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 0]:
                print(j)