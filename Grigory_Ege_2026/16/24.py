import sys,functools
sys.setrecursionlimit(10**7)
@functools.lru_cache(100000)
def F(n):
    return 3 * (G(n-4)+5)
@functools.lru_cache(100000)
def G(n):
    if n < 8 :
        return 3*n
    if n >= 8:
        return G(n-3)+2
for n in range(1, 13000):
    G(n)
    F(n)
print(F(12345))