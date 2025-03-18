import functools
#@functools.lru_cache(None)
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return G(n) + F(n - 1)
    if n > 2 and n % 2 != 0:
        return F(n - 2) - 2 * G(n + 1)
@functools.lru_cache(None)
def G(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return F(n - 3) + F(n - 2)
    if n > 2 and n % 2 != 0:
        return F(n + 1) - G(n - 1)
# for x in range(1, 10000):
#     G(x)
#     F(x)
print(G(120))