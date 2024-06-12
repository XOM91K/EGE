import functools
@functools.lru_cache(None)
def g(x, y, z):
    if '11' in z:
        return 0
    if x == y:
        return 1
    if x > y or x == 28:
        return 0
    if x < y:
        return g(x + 1, y, z + '1') + g(x + 3, y, '') + g(x * 2, y, '')
print(g(4, 10, '') * g(10, 93, ''))