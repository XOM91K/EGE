import sys
import functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(n):
    if n <= 2:
        return 5
    if n > 2:
        return f(n - 2) + n
for x in range(1, 23023):
    f(x)
print(f(23023))