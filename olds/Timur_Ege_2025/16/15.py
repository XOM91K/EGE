import functools
@functools.lru_cache(None)
def F(n):
    if n < 3:
        return n * 4
    if n >= 3 and n % 2 != 0:
        return n * 2
    if n >= 3 and n % 2 == 0:
        return 5 * F(n - 2) + n
ct = 0
for n in range(1, 2000):
    if len(str(F(n))) == 3 and F(n) % 2 == 0:
        ct += 1
print(ct)