import sys, functools
sys.setrecursionlimit(1000_000)
@functools.lru_cache(None)
def f(n):
    if n>=128: return f(n-5)+1092
    if n<128: return 5*g(n-7)+29
@functools.lru_cache(None)
def g(n):
    if n>303728: return n-15
    if n<=303728: return g(n+8)/2-109
for n in range(304000, 1, -1):
    g(n)
for n in range(1, 2050):
    f(n)
print(f(2049))