import functools, sys
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n > 10000:
        return n
    if n > 10 and F(n + 1) % 2 == 0:
        return F(n + 1) + 5
    if n > 10 and F(n + 1) % 2 != 0:
        return F(n + 1) - 8
for x in range(10000, 130, -1):
    F(x)
print(F(140) - F(150))