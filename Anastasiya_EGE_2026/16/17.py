import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(500)
def F(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n + 3) * F(n - 3)
for x in range(1, 247600):
    F(x)
print(((F(247563) // 519) - 477 * F(247560)) // F(247557))