import sys,functools
sys.setrecursionlimit(10*9)
@functools.lru_cache(5000)
def f(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n + 3) * f(n -3)
for n in range(1, 320000):
    f(n)
print((f(318765) - 318762 * f(318762)) / f(318759))