import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(5000)
def f(n):
    if n < 17:
        return 6
    if n >= 17:
        return (n+5)*f(n-9)
for n in range(1, 235_000):
    f(n)
print((f(234561)//436+f(234552)//218)//f(234534))