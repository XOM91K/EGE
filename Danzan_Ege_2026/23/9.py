import functools
@functools.lru_cache(None)
def f(x, y, ct):
    if x == 24 or x == 32:
        ct += 1
    if x > y:
        return 0
    if x == y and ct == 1:
        return 1
    if x == y and ct != 1:
        return 0
    if x < y:
        return f(x + 1, y, ct) + f(x + 2, y, ct) + f(x + 4, y, ct) + f(x + 8, y, ct)
print(f(16, 48, 0))