import functools, sys
sys.setrecursionlimit(1000000000)
@functools.lru_cache(None)
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return 3*f(n-2) + f(n-1)
for i in range(1, 10000 + 1):
    print(f(i + 4)/f(i))
# print(f(20000024)/f(20000020))