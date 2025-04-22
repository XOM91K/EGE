import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * F(n - 7)
for n in range(50000):
    F(n)
print((F(47872) - 290 * F(47865)) / F(47858))