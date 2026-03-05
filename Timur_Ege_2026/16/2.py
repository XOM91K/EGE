import functools
@functools.lru_cache(None)
def F(n):
    if n >= 128:
        return F(n - 5) + 1092
    if n < 128:
        return 5 * G(n - 7) + 29
@functools.lru_cache(None)
def G(n):
    if n > 303728:
        return n - 15
    if n <= 303728:
        return G(n + 8) / 2 - 109
for n in range(310000, 0, -1):
    G(n)
for n in range(0, 310000):
    F(n)
print(F(2049))