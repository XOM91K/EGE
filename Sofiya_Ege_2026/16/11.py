import sys, functools
sys.setrecursionlimit(1_000_000)
@functools.lru_cache(None)
def f(n):
    if n==1: return 1
    if n>1: return f(n-1)*(n//2)+1
for x in range(1, 11000):
    f(x)
print(sum(map(int, str(f(10000))[-18:])))