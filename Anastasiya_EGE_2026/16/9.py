import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(n):
    if n<5:
        return 4**4
    if n>4:
        return 4*f(n-1)+4
for i in range(1, 10000):
    f(i)
print(f(4048)/f(4036))