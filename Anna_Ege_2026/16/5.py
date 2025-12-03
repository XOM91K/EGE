import sys, functools
sys.setrecursionlimit(100000000)
@functools.lru_cache(None)
def f(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return 3 * f(n-2) + f(n-1)
for x in range(1000, 10000):
    print(f(x + 4) / f(x))
#print(f(20000024)/f(20000020))