import functools, sys
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def G(n):
    if n < 25:
        return n
    if n >= 25:
        return (n - 5) * G(n - 6)
for x in range(1, 100000):
    G(x)
print((G(60000) - 315 * G(59994)) / G(59988))