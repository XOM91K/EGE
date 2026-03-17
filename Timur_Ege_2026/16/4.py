import functools
@functools.lru_cache(None)
def F(n):
    if n > 19999:
        return n + F(n -6)
    if n < 20000:
        return n + G(n - 3)
@functools.lru_cache(None)
def G(n):
    if n < 20000:
        return 20 + n + G(n + 4)
    if n > 19999:
        return n ** 2
for n in range(66000, 0, -1):
    G(n)
for n in range(0, 66000):
    F(n)
print(F(65000))