import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n >= 20:
        return F(n - 5) + 3219
    if n < 20:
        return 8 * (G(n - 9) - 34)
@functools.lru_cache(None)
def G(n):
    if n >= 250000:
        return n / 24 + 32
    if n < 250000:
        return G(n + 9) - 3
for x in range(250000, 1, -1):
    G(x)
for x in range(926):
    F(x)
print(F(925))