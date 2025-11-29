import sys
import functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n + F(n-1)
for x in range(1,1000000):
    F(x)
print(F(57693))