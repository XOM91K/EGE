import functools
@functools.lru_cache(None)
def F(n):
    if n % 2 == 0:
        return F(n // 2) + 3
    elif n % 2 != 0 and n % 3 == 0:
        return F(n // 3) + 2
    else:
        return 0
for n in range(1, 10 ** 10):
    if F(n) == 70:
        print(n)
        break