import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(5000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2*n+f(n-1)
for n in range(1, 60_000):
    f(n)
print(sum(map(int, str(f(57693)))) ** 2)