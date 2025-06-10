import functools
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) * (n // 2) + 1
for x in range(1, 15000):
    F(x)
print(sum(map(int, str(F(10000))[-18:])))