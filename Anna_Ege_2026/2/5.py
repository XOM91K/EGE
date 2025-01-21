import itertools
def F(x, y, z, w, u):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))
