import sys, functools
sys.setrecursionlimit(10 ** 6)
@functools.lru_cache(None)
def F(n):
    return 2 * (G(n - 3) + 8)
@functools.lru_cache(None)
def G(n):
    if n < 10:
        return 2 * n
    else:
        return G(n - 2) + 1
for x in range(1, 16000):
    F(x)
print(F(15548))