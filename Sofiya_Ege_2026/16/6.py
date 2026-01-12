import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def g(n):
    if n<25: return n
    if n>=25: return (n-5)*g(n-6)
for x in range(1, 60_000):
    g(x)
print((g(60_000)-315*g(59994))/g(59988))