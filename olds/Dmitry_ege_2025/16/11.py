import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 4) * F(n - 6)
for x in range(1, 35000):
    F(x)
print((F(33448) - 230 * F(33442)) / F(33436))