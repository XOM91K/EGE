import sys, functools
sys.setrecursionlimit(10**6)
@functools.lru_cache(None)
def f(n):
    if n ==0:
        return 0
    if n >0:
        return 3*n + f(n-1)
for n in range(1, 1000000):
    if f(n) > 17_505_321:
        print(n)
        break