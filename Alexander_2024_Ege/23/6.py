import functools
@functools.lru_cache(None)
def g(x, y, z):
    if x == y and z == 10:
        return 1
    if x != y and z == 10:
        return 0
    if z < 10:
        return g(x + 4, y, z + 1) + g(x + 7, y, z + 1) + g(x // 2, y, z + 1)
print(g(1, 1, 0))