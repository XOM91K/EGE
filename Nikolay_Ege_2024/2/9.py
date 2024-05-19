from itertools import *


def f(x, y, w, z):
    return ((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))


for i in product([0, 1], repeat=4):
    table = [(1, 0, 0, 0),
    (i[0], 1, 0, i[1]),
    (1, 0, i[2], i[3])]
    if len(table) == len(set(table)):
        for j in permutations('xywz'):
            if [f(**dict(zip(j, r))) for r in table] == [1, 1, 1]:
                print(j)