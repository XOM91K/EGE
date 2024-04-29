import functools
@functools.lru_cache(None)
def F(n):
    if n < 3:
        return n
    if n > 2 and n % 2 != 0:
        return F(n - 1) + F(n - 2) + 1
    if n > 2 and n % 2 == 0:
        return sum([F(i) for i in range(1, n)])
print(F(38))