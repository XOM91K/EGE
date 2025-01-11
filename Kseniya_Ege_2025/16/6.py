import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) * F(n // 2) + 1
for x in range(1, 10001):
    F(x)
print(F(10000))