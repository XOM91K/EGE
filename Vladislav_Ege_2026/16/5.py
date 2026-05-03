import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n >= 21:
        return F(n - 8) + 1095
    else:
        return 10 * (G(n - 7) - 36)
@functools.lru_cache(None)
def G(n):
    if n >= 22560:
        return n / 23 + 33
    else:
        return G(n + 11) - 4
for n in range(22600, 1, -1):
    G(n)
for n in range(1, 22600):
    F(n)
print(F(548))
