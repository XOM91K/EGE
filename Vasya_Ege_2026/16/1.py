import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(1000)
def F(n):
    if n < 17:
        return 6
    if n >= 17:
        return (n + 5) * F(n - 9)
for n in range(1, 235000):
    F(n)
print((F(234561) // 436 + F(234552) // 218) // F(234534))