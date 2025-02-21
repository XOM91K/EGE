import functools
@functools.lru_cache(None)
def F(n):
    if n < 10:
        return n
    if n >= 10:
        return F(n % 10) + F(n // 10)
for x in range(10323661230, 11251251000 + 100):
    #if F(x) == 159:
        print(x, F(x))
#9223372036854775808
#9999999999999999999