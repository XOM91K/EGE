import sys, functools
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def F(n):
    if n < 3:
        return 2
    if n % 2 == 0 and n > 2:
        return 2 * F(n - 2) - F(n - 1) + 2
    if n % 2 != 0 and n > 2:
        return 2 * F(n - 1) + F(n - 2) - 2
for x in range(1, 171):
    print(x, F(x))
