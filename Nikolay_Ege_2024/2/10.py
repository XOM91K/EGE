from itertools import *
def f(x,y,w,z):
    return (x and(not(y))) or (x and z) or ((not(x))and(not(y)))
for i in product([0,1],repeat=7):
    table=[(i[0],i[1],1,i[2]),
           (1,i[3],1,i[4]),
           (1,1,1,i[5]),
           (1,i[6],1,1)]
    if len(table)==len(set(table)):
        for j in permutations('xywz'):
            if [f(**dict(zip(j,r)))for r in table]==[0,0,0,0]:
                print(j)
