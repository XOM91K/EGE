import functools
@functools.lru_cache(None)
def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * F(n - 4)
for i in range(1, 13766):
    #1. от 1 до 13766
    #2. от 13766 до 1  -1
    F(i)
print((F(13766) - 9 * F(13762)) / F(13758))