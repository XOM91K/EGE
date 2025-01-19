import functools
@functools.lru_cache(None)
def F(n):
    if n <= 2:
        return n
    if n > 2:
        return n + F(n - 2)
# if n < [какого-то числа] => for x in range(1, 3000)
# if n > [какого-то числа] => for x in range(3000, 1, -1)
for x in range(1, 3000):
    F(x)
print(F(2023) + F(2020))