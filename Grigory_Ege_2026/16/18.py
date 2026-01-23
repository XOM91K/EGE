import sys,functools
sys.setrecursionlimit(10**9)
@functools.lru_cache(None)
def F(n):
    if n>=128:
        return F(n-5)+1092
    if n < 128 :
        return 5*G(n-7)+29
@functools.lru_cache(None)
def G(n):
    if n > 303728:
        return n-15
    if n<=303728:
        return (G(n+8)/2)-109
for x in range(304000, 1, -1):
    G(x)
for x in range(1,2100):
    F(x)
print(F(2049))