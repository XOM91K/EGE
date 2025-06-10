import functools, sys
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n < 10:
        return n
    if n >= 10:
        return G(F(n - 1) % 10) + F(G(n % 10) - 1) - F(n - 3)
@functools.lru_cache(None)
def G(n):
    if n < 10:
        return -n
    if n >= 10:
        return F(G(n - 1) % 10) + G(F(n - 1) - 1) + G(n - 2)
for x in range(1, 1112):
    F(x)
    G(x)
print(F(1111) + G(1111))