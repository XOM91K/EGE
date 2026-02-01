import sys, functools

sys.setrecursionlimit(100_000)


@functools.lru_cache(None)
def f(n):
    if n < 31054:
        return f(n + 4) + 3020
    if n >= 31054:
        return 3 * (g(n - 2) - 15)


def g(n):
    if n >= 28:
        return g(n - 5) - 15
    if n < 28:
        return 3 * n - 4


for x in range(1, 20):
    f(x)
print(f(15))
