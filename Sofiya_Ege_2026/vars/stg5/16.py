import functools, sys
sys.setrecursionlimit(1000000)
@functools.lru_cache(444)
def F(n):
    if n >= 14:
        return n * F(n - 1)
    if n < 14:
        return 8 * G(n - 3)
@functools.lru_cache(444)
def G(n):
    if n < 31:
        return 4
    if n >= 31:
        return n / 2 * G(n - 2)
for n in range(1, 642000):
    G(n)
for n in range(1, 321000):
    F(n)
print(F(320726) / G(641450))