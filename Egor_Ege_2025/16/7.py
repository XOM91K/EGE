import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n >= 3210:
        return 1
    if n <= 3210:
        return F(n + 3) + 7

@functools.lru_cache(None)
def G(n):
    if n < 10:
        return n
    if n >= 10:
        return G(n - 3) + 5
print(F(15) - G(3000))