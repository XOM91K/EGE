import functools
@functools.lru_cache(None)
def F(n):
     if n == 1 or n == 2:
         return 1
     if n > 2:
         return 3 * F(n - 2) + F(n - 1)
print(F(670) / F(666))