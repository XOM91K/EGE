import functools
@functools.lru_cache(None)
def F(n):
    return G(n - 2)
@functools.lru_cache(None)
def G(n):
    if n < 100:
        return n
    if n >= 100:
        return F(n - 3) + 1
for x in range(5000):
    G(x)
    F(x)
print(F(5000))