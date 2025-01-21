import functools
@functools.lru_cache(None)
def F(n):
    if n <= 2:
        return 5
    if n > 2:
        return F(n - 2) + n
    
print(F(23023))