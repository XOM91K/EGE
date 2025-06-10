import functools
@functools.lru_cache(None)
def f(x,y):
    if x > y or x == 35:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
print(f(7, 13) * f(13, 15) *f(15, 51))