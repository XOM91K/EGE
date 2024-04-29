import functools
mx = 0
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 2
    elif n > 1 and F(n - 1) < 7555444:
        return F(n - 1) + 6
    else:
        return F(n - 1) - 7555444
for x in range(1, 7555444 * 2):
    mx = max(mx, F(x))
print(mx)
#7555448