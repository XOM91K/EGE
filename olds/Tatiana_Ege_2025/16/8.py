import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 3) * F(n - 5)
for i in range(45000):
    F(i)
print((F(44652) - 350 * F(44647)) / F(44642))