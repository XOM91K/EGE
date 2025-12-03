import functools
@functools.lru_cache(None)
def F(n):
    if n >= 2022:
        return n
    if n < 2022:
        return F(n + 5) + 7
for x in range(2022):
    F(x)
print(F(45) - F(49))