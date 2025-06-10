import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 3:
        return 1
    if n > 2 and sum(map(int, str(n))) % 2 == 0:
        return F(n-1) - F(n-2)
    if n > 2 and sum(map(int, str(n))) % 2 != 0:
        return F(n-1) + F(n//2)
print(F(100))