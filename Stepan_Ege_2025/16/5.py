import functools
@functools.lru_cache(None)
def F(n):
    if n < 6:
        return n
    if n >= 6:
        return 3 * n * F(n - 3)
#for x in range(13000, 1, -1):
for x in range(1, 13000):
    F(x)
print((F(12571) - 9 * F(12568)) / F(12565))