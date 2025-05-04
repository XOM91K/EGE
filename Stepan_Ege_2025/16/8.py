import sys, functools
sys.setrecursionlimit(20000)
@functools.lru_cache(None)
def f(n):
    if n < 100:
        return n
    if n > 99 and n % 2 == 0:
        return (1/2) * f(n - 1)
    if n > 99 and n % 2 != 0:
        return 2 * f(n - 1)
for x in range(1, 17000):
    f(x)
print(1000 * f(16384)/f(7777))