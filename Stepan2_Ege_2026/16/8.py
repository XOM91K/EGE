import functools
@functools.lru_cache(None)
def F(n):
    if n > 10000:
        return n + 4
    if n <= 10000:
        return 3 * n + 5 + F(n + 3)
for x in range(10000, 1, -1):
    F(x)
print(F(707) - F(716))