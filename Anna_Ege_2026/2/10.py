import itertools
ct = set()
def f(x, y, w, z):
    return (w==z) and (x<= y) and ((not w) or x)
for i in itertools.product([0, 1], repeat = 4):
    l = [(0, 0, 1, i[0]),
         (i[1], 1, 1, 0),
         (0, i[2], i[3], 0)]
    if len(set(l)) == len(l):
        for j in itertools.permutations('xywz'):
            if [f(**dict(zip(j, r)))for r in l] == [0, 0 ,0]:
                ct.add(j)
print(len(ct))