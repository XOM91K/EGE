import functools
@functools.lru_cache(None)
def V(n):
    if n > 100:
        return V(n - 3) + 28965
    if n <= 100:
        return 5*(M(n-4)-25)
@functools.lru_cache(None)
def M(n):
    if n >= 555384:
        return 12 * n + 70
    if n < 555384:
        return M(n+8)-55
for x in range(560000, 1, -1):
    M(x)
for x in range(1, 560000):
    V(x)
print(V(9865)**2)