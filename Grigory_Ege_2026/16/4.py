import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n <= 2:
        return 5
    if n > 2:
        return F(n - 2) + n
for n in range(1, 24000):
    F(n)
print(F(23023))