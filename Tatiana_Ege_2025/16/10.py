import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n + F(n - 1)
for i in range(60000):
    F(i)
print(sum(map(int, str(F(57693)))) ** 2)