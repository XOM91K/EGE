import functools
@functools.lru_cache(None)
def f(n):
    if n == 1:
        return 2
    elif n > 1 and f(n - 1) < 7555444:
        return f(n - 1) + 6
    else:
        return f(n - 1) - 7555444
mx = 0
for x in range(1, 7000_000*2):
    mx = max(mx, f(x))
print(mx)