import sys, functools
sys.setrecursionlimit(10 ** 6)
@functools.lru_cache(5000)
def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)
@functools.lru_cache(5000)
def G(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return G(n + 9) - 4
for x in range(249000, 1, -1):
    G(x)
for x in range(1, 1000):
    F(x)
print(F(673))