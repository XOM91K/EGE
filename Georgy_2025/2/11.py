import itertools
def F(x,y,z,w):
    return x and (z <= w) and (not(y))
for i in itertools.product([0,1], repeat = 7):
    table = [(i[0],i[1],1,i[2]),
             (i[3],1,0,i[4]),
             (1,0,i[5],i[6])]
    if len(table) == len(set(table)):
        for j in itertools.permutations("xyzw"):
            if [F(**dict(zip(j,r))) for r in table] == [1,1,1]:
                print(j)