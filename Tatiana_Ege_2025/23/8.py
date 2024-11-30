import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n > 2024:
        return 2
    if n == 2024:
        return 1
    if n < 2024:
        return n*(n+1) + F(n+1) - F(n+2)
for x in range(2025, 1, -1):
    print(x, F(x))
print(F(100)-F(10)+F(2020))