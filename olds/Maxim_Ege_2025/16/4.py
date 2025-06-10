import sys, functools
sys.setrecursionlimit(1000000)

@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n % 2 > 0:
        return F(n - 1) + n * 2 - 1
    if n % 2 == 0:
        return F(n / 2) * 4
for a in range(0,10000):
    for b in range(0, 10000):
        if F(a) - F(b) == 1045:
            print(abs(a - b))