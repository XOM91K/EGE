print('x y z w')
import itertools
for x, y, z, w in itertools.product([0, 1], repeat=4):
    if ((x == (w or y)) or ((w <= z) and (y <= w))) == 0:
        print(x, y, z, w)