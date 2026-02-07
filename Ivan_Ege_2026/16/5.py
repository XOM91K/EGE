import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def G(n):
    if n > 303_728:
        return n - 15
    else:
        return G(n + 8) / 2 - 109
@functools.lru_cache(None)
def F(n):
    if n >= 128:
        return F(n - 5) + 1092
    else:
        return 5 * G(n - 7) + 29
for n in range(303_800, 0, -1):
    G(n)
for n in range(120, 2100):
    F(n)
print(F(2049))