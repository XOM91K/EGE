import functools
@functools.lru_cache(None)
def F(n):
    if n < 10:
        return n
    if n > 9:
        return 3 * n + G(n - 2)
@functools.lru_cache(None)
def G(n):
    if n < 10:
        return n
    if n > 9:
        return n - 2 + F(n - 1)
for x in range(2204):
    G(x)
    F(x)
print(F(2204) - G(2200))