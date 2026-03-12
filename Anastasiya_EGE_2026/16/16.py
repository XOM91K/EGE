import sys,functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def g(n):
    if n<111700:
        return 8*n-4
    if n>=111700:
        return (g(n-17)+344)
@functools.lru_cache(None)
def f(n):
    if n<65000:
        return (f(9+n)+13020)
    if n>=65000:
        return (4*(g(n-4)-12))
for x in range(1, 120000):
    g(x)
for x in range(70000, 1, -1):
    f(x)
print(sum(map(int, str(f(4975)))) * 2)