import functools, sys
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 10:
        return n
    if n > 9:
        return 3*n + G(n - 2)
def G(n):
    if n < 10:
        return n
    if n > 9:
        return n - 2 + F(n - 1)
print(F(2204) - G(2200))