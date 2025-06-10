import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n > 0:
        return 3 * n + F(n - 1)
for n in range(0, 10000):
    if F(n) > 17_505_321:
        print(n)