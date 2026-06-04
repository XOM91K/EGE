import functools
@functools.lru_cache(None)
def F(n):
    if n >= 20:
        return F(n - 4) + 4620
    if n < 20:
        return 8 * (G(n - 12) - 21)
@functools.lru_cache(None)
def G(n):
    if n >= 384242:
        return n / 4 + 18
    if n < 384242:
        return 12 + G(n + 41)
for n in range(385000, 0, -1):
    G(n)
for n in range(0, 385000):
    F(n)
print(F(913))