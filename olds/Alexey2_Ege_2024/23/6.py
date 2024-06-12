import functools
@functools.lru_cache(None)
def f(x, y, z):
    if x > y or (x == y and z[-3:] != 'BAB'):
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y, z + 'A') + f(x * 2, y, z + 'B') + f(x + 5, y, z + 'C')
print(f(5, 62, ''))