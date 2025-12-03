import sys, functools
sys.setrecursionlimit(200000)
@functools.lru_cache(None)
def f(n):
    if n==1 or n==2: return 1
    if n>2: return 3*f(n-2)+f(n-1)
for x in range(150000):
    f(x)
print(f(15000)//f(14996))