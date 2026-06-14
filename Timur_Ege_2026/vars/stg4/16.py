import functools
@functools.lru_cache(None)
def F(n):
    if n > 29999:
        return n + F(n -5)
    if n < 30000:
        return n + G(n - 2)
@functools.lru_cache(None)
def G(n):
    if n < 30000:
        return 10 + n + G(n + 3)
    if n > 29999:
        return n ** 2
for n in range(80_000, 0, -1):
    G(n)
for n in range(0, 80_000):
    F(n)
print(F(75000))