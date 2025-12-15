import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)
@functools.lru_cache(None)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n + 9) - 4
for x in range(270_000,1 , -1):
    G(x)
for x in range(1, 700):
    F(x)
print(F(673))