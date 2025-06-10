import functools
@functools.lru_cache(None)
def G(n):
    if n < 25:
        return n
    if n >= 25:
        return (n - 5) * G(n - 6)
for i in range(60001):
    G(i)
print((G(60000) - 315 * G(59994)) / G(59988))