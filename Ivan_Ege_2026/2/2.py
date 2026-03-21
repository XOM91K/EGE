import itertools

def f(x, y, z, w):
    return (not(not(x <= (not w)) and z)) and (not(w <= z)) and (x <= (not z))
a = set()
for i in itertools.product([1, 0], repeat=5):
    table = [(1, 0, i[0], 0),
             (1, 0, i[1], i[2]),
             (i[3], 1, i[4], 1)]
    if len(set(table)) == 3:
        for j in itertools.permutations('xyzw'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 0, 0]:
                a.add(j)
print(len(a))