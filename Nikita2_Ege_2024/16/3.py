import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 2
    if n > 1:
        return F(n - 1) + n + 1
for x in range(23031):
    F(x)
print(F(23030))