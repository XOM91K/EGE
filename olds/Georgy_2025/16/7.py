import sys, functools
sys.setrecursionlimit(99999)
@functools.lru_cache(None)
def F(n):
    print(n)
    if n == 1:
        return 1
    return (n + 1) * F(n - 1)


for x in range(1, 2400):
    F(x)
print(((F(2025) // 2026) + F(2024)) / F(2023))