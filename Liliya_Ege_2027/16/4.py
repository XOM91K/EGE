import sys, functools
sys.setrecursionlimit(1_000_000)
@functools.lru_cache(5000)
def F(n):
    if n >= 128:
        return F(n - 5) + 1092
    if n < 128:
        return 5 * G(n - 7) + 29
@functools.lru_cache(5000)
def G(n):
    if n > 303728:
        return n - 15
    if n <= 303728:
        return G(n + 8) / 2 - 109
for x in range(305000, 1, -1):
    G(x)
for x in range(1, 3000):
    F(x)
print(F(2049))