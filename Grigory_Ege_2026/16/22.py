import sys, functools

sys.setrecursionlimit(10 ** 7)


@functools.lru_cache(None)
def F(n):
    if n >= 57_000:
        return F(n - 2) + 3552 + F(n - 3)
    if n < 57_000:
        return 222 + G(n - 2) + G(n - 1)


@functools.lru_cache(None)
def G(n):
    if n >= 9999:
        return G(n - 5) + G(n - 3) + 157
    if n < 9999:
        return 15 * (2 * n + 4)


for x in range(1, 59000):
    G(x)
for x in range(1, 59000):
    F(x)
print(F(2540))
print(1 * 5 * 2 * 6 * 5 * 2)