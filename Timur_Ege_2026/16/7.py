import functools
@functools.lru_cache(100)
def F(n):
    if n < 10:
        return 3
    if n >= 10:
        return (n + 4) * F(n - 5)
for x in range(1, 257500):
    F(x)
print((F(257487) // 683 + 67 * F(257477)) // F(257472))
