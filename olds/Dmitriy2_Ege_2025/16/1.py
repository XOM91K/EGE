import functools
@functools.lru_cache(None)
def F(n):
    if n <= 2:
        return n
    if n > 2:
        return n + F(n - 2)
for x in range(2025):
    F(x)
print(F(2023) + F(2020))