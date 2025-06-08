import functools
@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n > 0:
        return 3 * n + F(n - 1)
for n in range(1, 10000):
    if F(n) > 17_505_321:
        print(n)
        break
