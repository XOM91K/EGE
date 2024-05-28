import functools
@functools.lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 3 == 0:
        return f(n - 1) + n / 3
    else:
        return f(n - 1) + f(n - 2)
print(f(54) - f(52) - f(50))