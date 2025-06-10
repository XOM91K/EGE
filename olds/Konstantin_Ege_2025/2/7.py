import itertools
def f1(x,y,z,w,):
    return (w or (not y)) <= (z == x)
def f2(x,y,z,w,):
    return (w or (not y)) == (x <= z)
for i in itertools.product([0,1], repeat=6):
    table = [(i[0], 1, i[1], 1), (i[2], 0, 0, 0), (0, 0, 0, i[3])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f1(**dict(zip(j, r))) for r in table] == [0, i[4], 0]:
                if [f2(**dict(zip(j, r))) for r in table] == [i[5], 0, 0]:
                    print(j)