import functools
@functools.lru_cache(None)
def F(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return 3 * F(n - 2) + F(n - 1)
l = [0, 1, 1]
for x in range(3, 20_000_030):
    l.append(3 * l[x - 2] + l[x - 1])
print()