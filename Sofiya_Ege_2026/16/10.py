import sys, functools
sys.setrecursionlimit(1000_000)
@functools.lru_cache(None)
def g(n):
    if n>=301208: return 10*n+50
    if n<301208: return g(n+7)-21
@functools.lru_cache(None)
def f(n):
    if n>40: return f(n-4)+3020
    if n<=40: return 3*(g(n-2)-15)
for i in range(302000, 1, -1):
    g(i)
for i in range(1, 6000):
    f(i)
print(f(5078))