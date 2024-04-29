import functools, sys
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and sum(map(int, str(n))) % 2 == 0:
        return f(n - 1) - f(n - 2)
    if n > 2 and sum(map(int, str(n))) % 2 != 0:
        return f(n - 1) + f(n // 2)
print(f(100))
