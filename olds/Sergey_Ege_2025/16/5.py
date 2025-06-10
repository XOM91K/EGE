import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(n):
    if n == 1:
        return 2
    if n > 1:
        return f(n - 1) + n + 1
for x in range(1, 23023):
    f(x)
print(f(23023))