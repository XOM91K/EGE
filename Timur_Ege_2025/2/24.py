import itertools
def F(x,y,z,w):
    return (((w <= z) == (x <= (not y))) and (x or z))
for i in itertools.product([0,1], repeat = 2):
    table = [(1,0,0,1),
             (1,1,1,0),
             (0,i[0],0,i[1])]
    if len(set(table)) == len(table):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in table] == [1,0,1]:
                print(j)