import functools
@functools.lru_cache(None)
def F(n):
    if n < 10:
        return n - 1
    if n >= 10 and n % 2 == 0:
        return 3 * n - 1 + F(n - 3)
    if n >= 10 and n % 2 != 0:
        return 5 * n + 2 + F(n - 4)
for x in range(1, 10000):
    F(x)
print(F(4445) - F(4444))