# 4825
# import sys
# import functools
#
# sys.setrecursionlimit(1000000)
#
#
# @functools.lru_cache(None)
def g(s, p, z):
    if p == 3 and s >= 43:
        return 1
    elif p == 3 and s < 43:
        return 0
    elif p < 3 and s >= 43:
        return 0
    if p % 2 == 0:
        if z == 1:
            return g(s + 2, p + 1, 2) or g(s * 2, p + 1, 3)
        elif z == 2:
            return g(s + 1, p + 1, 1) or g(s * 2, p + 1, 3)
        elif z == 3:
            return g(s + 1, p + 1, 1) or g(s + 2, p + 1, 2)
        elif z == 0:
            return g(s + 1, p + 1, 1) or g(s + 2, p + 1, 2) or g(s * 2, p + 1, 3)
    else:
        if z == 1:
            return g(s + 2, p + 1, 2) and g(s * 2, p + 1, 3)
        elif z == 2:
            return g(s + 1, p + 1, 1) and g(s * 2, p + 1, 3)
        elif z == 3:
            return g(s + 1, p + 1, 1) and g(s + 2, p + 1, 2)
        elif z == 0:
            return g(s + 1, p + 1, 1) and g(s + 2, p + 1, 2) and g(s * 2, p + 1, 3)


for x in range(1, 43):
    if g(x, 0, 0):
        print(x)