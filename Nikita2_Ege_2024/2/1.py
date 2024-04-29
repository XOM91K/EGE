print('x y z w')
from itertools import product
for x, y, z, w in product([0, 1], repeat=4):
    if ((z and y) or ((x <= z) == (y <= w))) == 0:
        print(x, y, z, w)
