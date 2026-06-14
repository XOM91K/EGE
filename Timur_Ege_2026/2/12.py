import itertools
def F(x,y,z,w):
    return (w==z)and (x<=y) and ((not w) or x)
for i in itertools.product([0,1], repeat=4):
    table=[(0,0,1,i[0]),
           (i[1],1,1,0),
           (0,i[2],i[3],0)]
    if len(set(table))==3:
        for j in itertools.permutations('xyzw'):
            if[F(**dict(zip(j,r)))for r in table]==[0,0,0]:
                print(j)