import itertools
def f(x,y,z,w,):
    return ((x and y) or (y and z)) == ((x<= w) and (w <= z))
for i in itertools.product([0,1], repeat=2):
    table = [(0, 1, 1, 1), (0, 1, 0, i[0]), (0, 1, 0, i[1])]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)