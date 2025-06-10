import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 7:
        return 7
    if n >= 7 and n%3 != 0:
        return 5 - F(n-1)
    if n >= 7 and n%3 == 0:
        return 3 + F(n-1)
for x in range(1, 4000):
    F(x)
print(F(3015))