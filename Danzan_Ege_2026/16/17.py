import sys, functools
sys.setrecursionlimit(1000000000)
@functools.lru_cache(5000)
def F(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n + 3) * F(n - 3)
for x in range(1, 319000):
    F(x)
print((F(318765) - 318762 * F(318762)) / F(318759))