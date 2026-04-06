import itertools
def F(x, y, z , w):
    return y and (((not w) or z) == x)
for i in itertools.product([0, 1], repeat=5):
    t = [(i[0], i[1], 0, 0),
         (i[2], 1, 1, 1),
         (0, i[3], i[4], 0)]
    if len(set(t)) == 3:
        for j in itertools.permutations('xyzw'):
            if [F(**dict(zip(j, r))) for r in t] == [1, 0, 1]: # jr Neymar
                print(j)
