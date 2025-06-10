import functools
@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 1
    if n > 0:
        return 2 * F(1 - n) + 3 * F(n - 1) + 2
    if n < 0:
        return -F(-n)
for x in range(1,15000):
    F(x)
print(sum(map(int,str(F(14750)))))