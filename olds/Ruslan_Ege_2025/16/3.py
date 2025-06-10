from sys import*
from functools import *
setrecursionlimit(10000000)
@lru_cache(None)

def f(n):
    if n > 2024:
        return 2
    if n == 2024:
        return 1
    if n < 2024:
        return n * (n+1) + f(n + 1) - f(n + 2)
for x in range(2024, 0, -1):
    f(x)
print(f(100)-f(10)+ f(2020))