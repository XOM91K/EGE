import functools
@functools.lru_cache(None)
def F(n):
    if n <= 2:
        return 5
    if n > 2:
        return F(n - 2) + n
for x in range(1, 25000):
    F(x)
print(F(23023))