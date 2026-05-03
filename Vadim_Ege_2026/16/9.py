import sys, functools
sys.setrecursionlimit(100000000)
@functools.lru_cache(None)
def F(n):
    if n < 17:
        return 6
    if n >= 17:
        return (n + 5) * F(n - 9)
for x in range(1, 235_000):
    F(x)
print((F(234561) // 436 + F(234552) // 218) // F(234534))
