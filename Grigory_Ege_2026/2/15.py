import itertools
s = []
def f(x,y,z,w):
    return (w == z) and (x<=y) and ((not w) or x)
for i in itertools.product([0,1],repeat=4):
    table = [(0,0,1,i[0]),
             (i[1],1,1,0),
             (0,i[2],i[3],0)]
    if len(table) == len(set(table)):
        for j in itertools.permutations('xyzw',r=4):
            if [f(**dict(zip(j,r))) for r in table] == [0,0,0]:
                s.append(j)
print(len(set(s)))