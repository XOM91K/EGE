import functools
@functools.lru_cache(None)
def f(n):
    print(n)
    if n < 6:
        return n
    if n >= 6:
        return 3 * n * f(n - 3)
for x in range(1, 20000):
    f(x)
print((f(12571) - 9 * f(12568)) / f(12565))