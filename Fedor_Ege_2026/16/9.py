import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def G(n):
    if n >= 28:
        return G(n - 5) - 15
    else:
        return 3 * n - 4
@functools.lru_cache(None)
def F(n):
    if n < 31054:
        return F(n + 4) + 3020
    if n >= 31054:
        return 3 * (G(n - 2) - 15)

for x in range(1, 32000):
    G(x)
for x in range(32000, 1, -1):
    F(x)
print(F(15))