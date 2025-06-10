import functools, sys
sys.setrecursionlimit(50000)
@functools.lru_cache(None)
def F(n):
    if n < 6:
        return n
    if n >= 6:
        return (3 * n - 2) * F(n - 5)
for n in range(1, 60000):
    F(n)
print((F(20568) - 51702 * F(20563)) / F(20553))