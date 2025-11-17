import sys
import functools

sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def F(n):
    if n > 2024:
        return 2
    if n == 2024:
        return 1
    if n < 2024:
        return n*(n+1) + F(n+1) - F(n+2)
for x in range(5000, 1, -1):
    F(x)
print(F(100)-F(10)+F(2020))