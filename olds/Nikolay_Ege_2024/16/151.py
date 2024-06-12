import functools, sys

sys.setrecursionlimit(100000)


@functools.lru_cache(None)
def f(n):
    if n > 10000:
        return n
    if f(n + 1) % 2 == 0 and n > 10:
        return f(n + 1) + 5
    if f(n + 1) % 2 != 0 and n > 10:
        return f(n + 1) - 8


for x in range(10100, 20, -1):
    f(x)
print(f(140) - f(150))
