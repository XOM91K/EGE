import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def f(x, y, ctB):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 3, y, ctB) + f(x + 4, y, ctB + 1) + f(x ** 2, y, ctB)
for i in range(5, 256 + 100):
    f(4, i, 0)
print(f(4, 32, 0))