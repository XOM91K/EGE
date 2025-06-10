import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n <= 1:
        return 1
    else:
        return F(n - 1) + F(n - 2)
for x in range(1, 100500):
    F(x)
print(str(F(50000))[-5:])
print(str(F(100000))[-5:])