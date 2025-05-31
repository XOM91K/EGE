import functools
@functools.lru_cache(None)
def F(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 2 == 0:
        return F(n + 1) + n ** 2- 3 * (n - 1)
    if n < 10000 and n % 2 != 0:
        return F(n + 2) + 5 * n - (n - 1)
# for x in range(1, 12000):
#         F(x)
for x in range(12000, 1, -1):
    F(x)
print(F(90) - F(99))