import itertools
def F(x,y,z,w):
    return ((not(w == y)) and (z <= w) and (not x))
for i in itertools.product([0,1], repeat= 6):
    table = [(i[0], i[1],i[2],1),(1,i[3],1,i[4]),(0,i[5],1,0)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r)))for r in table] == [1,1,1]:
                print(j)