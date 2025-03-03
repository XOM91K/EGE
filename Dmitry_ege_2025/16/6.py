import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n + F(n-1)
for x in range(1, 58000):
    F(x)
print(sum(map(int, str(F(57693)))) ** 2)