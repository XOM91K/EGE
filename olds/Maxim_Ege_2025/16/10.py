import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n <= 5:
        return 1000
    if n > 5:
        return n + 3 + F(n-2)
for x in range(0, 54000):
    F(x)
a = F(53078) + F(53076) + F(53074)
print(3*F(53080)-a)