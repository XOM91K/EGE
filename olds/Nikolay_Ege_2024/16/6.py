import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n >= 10000:
        return 1
    if n < 10000 and n % 2 == 0:
        return F(n + 3) + 7
    if n < 10000 and n % 2 != 0:
        return F(n + 1) - 3
for x in range(10000, 50, -1):
    F(x)
print(F(50) - F(57))