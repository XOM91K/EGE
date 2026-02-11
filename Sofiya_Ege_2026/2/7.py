import itertools
s = set()
def f(x, y, z, w):
    return (((not x) and (not z))or z)or(y and (not(y or w)))
for i in itertools.product([0,1], repeat=5):
    t=[(1, i[0], 1, i[1]),
       (1, 0, i[2], i[3]),
       (i[4], 0, 0, 0)]
    if len(set(t))==3:
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r)))for r in t]==[0, 1, 0]:
                s.add(j)
print(len(s))