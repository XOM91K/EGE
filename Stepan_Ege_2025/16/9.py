import functools
@functools.lru_cache(None)
def F(n):
    if n > 10000:
        return 2025
    if n <= 10000 and n % 2 != 0:
        return F(3 * n + 1) + n + 1
    if n <= 10000 and n % 2 == 0:
        return F(n + 3) + 2 * n + 3
for x in range(10000, 1, -1):
    F(x)
print(2 * F(25) - F(238))
