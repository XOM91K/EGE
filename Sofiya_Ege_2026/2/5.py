import itertools
def f(x, y, z, w):
    return (not w) and ((y or z) <= (y and (not x)))
for i in itertools.product([0,1], repeat=8):
    t=[(i[0], i[1], i[2], 1),
       (i[3], i[4], 1, i[5]),
       (i[6], 1, 1, i[7])]
    if len(set(t))==3:
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r)))for r in t]==[1, 1, 1]:
                print(j)