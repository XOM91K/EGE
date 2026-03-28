import functools
@functools.lru_cache(None)
def R(n):
    if n > 50:
        return R(n - 4) + 13020
    if n <= 50:
        return 4 * (H(n - 3) - 18)
@functools.lru_cache(None)
def H(n):
    if n >= 401333:
        return 10 * n + 50
    if n < 401333:
        return H(n + 7) - 45
for x in range(401333, 1, -1):
    H(x)
for x in range(401333):
    R(x)
print(R(6666) ** 2)