import sys, functools

sys.setrecursionlimit(100000)

@functools.lru_cache(None)
def F(n):
    if n < 100:
        return n
    if n > 99 and n % 2 == 0:
        return (1 / 2) * F(n - 1)
    if n > 99 and n % 2 != 0:
        return 2 * F(n - 1)
for x in range(1, 17000):
    F(x)

print(1000 * F(16384) / F(7777))
