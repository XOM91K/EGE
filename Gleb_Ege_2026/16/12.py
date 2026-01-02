import sys, functools
sys.setrecursionlimit(100_000)
@functools.lru_cache(None)
def f(n):
    return g(n - 2)
@functools.lru_cache(None)
def g(n):
    if n < 100:
        return n
    if n >= 100:
        return f(n - 3) + 1
for x in range(1, 10000):
    g(x)
print(f(5000))