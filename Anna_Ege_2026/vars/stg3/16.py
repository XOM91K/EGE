import functools
@functools.lru_cache(None)
def F(n):
    if n >= 20:
        return F(n - 4) + 4620
    else:
        return 8 * (G(n - 12) - 21)
@functools.lru_cache(None)
def G(n):
    if n >= 384242:
        return n / 4 + 18
    else:
        return 12 + G(n + 41)
for x in range(400_000, 1, -1):
    G(x)
for x in range(1, 5000):
    F(x)
print(F(913))