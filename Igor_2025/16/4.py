import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n <= 2:
        return 5
    if n > 2:
        return F(n - 2) + n
for x in range(2, 23024):
    F(x)
print(F(23023))