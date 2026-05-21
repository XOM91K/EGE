import sys, functools
sys.setrecursionlimit(20_000_000)
@functools.lru_cache(None)
def f(x, y, s):
    if x > y:
        return 0
    if x == y and s.count('B') <= 3:
        return 1
    if x == y and s.count('B') > 3:
        return 0
    if x < y:
        return f(x + 3, y, s + 'A') + f(x + 4, y, s + 'B') + f(x ** 2, y, s + 'C')
print(f(4, 61, ''))