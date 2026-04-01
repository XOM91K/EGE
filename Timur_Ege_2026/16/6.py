import functools
@functools.lru_cache(None)
def G(n):
    if n < 25:
        return n  # 10
    if n >= 25: # 10   5 * G(4)
        return (n - 5) * G(n - 6)
for n in range(0, 100000):
    G(n)
print((G(60000) - 315 * G(59994)) / G(59988))
