import sys,functools
sys.setrecursionlimit(10**7)
@functools.lru_cache(5000)
def F(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n+3)*F(n-3)
for x in range(1,320000):
    F(x)
print((F(318765) - 318762 * F(318762)) / F(318759))