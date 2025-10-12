import sys, functools
sys.setrecursionlimit(10 ** 6)
@functools.lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)
for x in range(0, 50000):
    F(x)
print((F(47872) - 290 * F(47865)) / F(47858))