import sys, functools
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)
for x in range(1, 4000):
    F(x)

print((F(2024)//4 + F(2023))/F(2022))