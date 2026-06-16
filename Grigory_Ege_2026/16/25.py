import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(5000)
def F(n):
    if n < 6:
        return 2
    if n >= 6:
        return (n % 4 + 2) * F(n - 2)
for n in range(1, 2027):
    F(n)
print((F(2026) - 3 * F(2024)) / F(2022))