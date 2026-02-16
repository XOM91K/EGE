import itertools
ct=0
s = set()
def f(x, y, w, z):
    return ((((not x) and (not z)) or z) or (y and (not(y or w))))
for i in itertools.product([0,1],repeat=5):
    l=[(1,i[0],1,i[1]),
       (1,0,i[2],i[3]),
       (i[4],0,0,0)]
    if len(set(l))==len(l):
        for j in itertools.permutations('xywz'):
            if [f(**dict(zip(j,r))) for r in l]==[0,1,0]:
                ct+=1
                s.add(j)
print(len(s))