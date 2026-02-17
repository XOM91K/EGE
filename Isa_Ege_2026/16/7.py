import sys, functools
sys.setrecursionlimit(109000)
@functools.lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) * (n // 2) + 1
for x in range(1, 10000):
    F(x)
print(sum([int(d) for d in str(F(10000))[-18:]]))
