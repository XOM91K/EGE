import sys, functools
sys.setrecursionlimit(10 ** 7)
@functools.lru_cache(None)
def F(n):
    if n > 40:
        return F(n - 4) + 3020
    if n <= 40:
        return 3 * (G(n - 2) - 15)
@functools.lru_cache(None)
def G(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return G(n + 7) - 21
for n in range(310000, 1, -1):
    G(n)
for n in range(1, 5100):
    F(n)
print(F(5078))
