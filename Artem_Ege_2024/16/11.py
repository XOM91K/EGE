import functools
@functools.lru_cache(None)
def F(n):
    if n < 3:
        return n
    if n > 2:
        return (2 * n - 1) * (F(n - 1) + F(n - 2))
print(F(69) % (10 ** 9 + 7))