import sys
import functools
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def f(n):
    if n > 2024:
        return 2
    elif n == 2024:
        return 1
    else:
        return n * (n + 1) + f(n + 1) - f(n + 2)
for i in range(3000, 1, -1):
    f(i)
print(f(100) - f(10) + f(2020))