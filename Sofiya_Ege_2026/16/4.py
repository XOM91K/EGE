import sys, functools
sys.setrecursionlimit(10000000)
@functools.lru_cache(None)
def F(n):
    if n <= 23:
        return n + 6
    if n > 23:
        return n + 6 + F(n - 2)
for x in range(1, 7000):
    F(x)
print(F(6857) - F(6845))