import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)
for x in range(1, 50_000):
    F(x)
print((F(47872) - 290 * F(47865)) / F(47858))