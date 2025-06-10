import sys, functools
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def F(n):
    if n < 5:
        return 4**4
    if n > 4:
        return 4 * F(n - 1) + 4
for x in range(1, 4049):
    F(x)
print(F(4048)/F(4036))