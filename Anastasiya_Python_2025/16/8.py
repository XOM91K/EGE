import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(n):
    if n>2024:
        return 2
    if n == 2024:
        return 1
    if n<2024:
        return n*(n+1) + f(n+1) - f(n+2)
for i in range(10000, 1, -1):
    f(i)
print(f(100)-f(10)+f(2020))