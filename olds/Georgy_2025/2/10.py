import itertools
def F(x, y, z, w):
    return ((x <= y) or (z == x)) and (w <= z)
for i in itertools.product([1, 0], repeat=0):
    table = [(0, 0, 1, 1),
             (0, 0, 1, 0),
             (0, 1, 1, 1)]
    if len(set(table)) == len(table):
       for j in itertools.permutations('xyzw'):
           if [F(**dict(zip(j, r))) for r in table] == [1, 0, 0]:
               print(j)