import itertools
def f(x, y, z):
    return (not z) and x or x and y
table = [(0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
         ]
for j in itertools.permutations('xyz'):
    if [f(**dict(zip(j, r))) for r in table] == [0, 1, 0, 1, 0, 0, 0, 1]:
        print(j)