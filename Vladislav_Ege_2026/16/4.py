import sys,functools
sys.setrecursionlimit(10000000)
@functools.lru_cache(None)
def F(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return 3 * F(n - 2) + F(n - 1)
for x in range(1, 21_000_000):
    F(x)
print(F(20000024) / F(20000020))