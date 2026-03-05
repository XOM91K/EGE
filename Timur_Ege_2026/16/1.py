import functools
@functools.lru_cache(None)
def F(n):
    if n < 31054:
        return F(n + 4) + 3020
    if n >= 31054:
        return 3 * (G(n - 2) - 15)
@functools.lru_cache(None)
def G(n):
    if n >= 28:
        return G(n - 5) - 15
    if n < 28:
        return 3 * n - 4
for d in range(0, 40000):
    G(d)
for d in range(40000, 0, -1):
    F(d)

print(F(15))