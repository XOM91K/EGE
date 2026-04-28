import sys, functools
sys.setrecursionlimit(300000)
@functools.lru_cache(None)
def f(n):
    if n<17:
        return 6
    if n>=17:
        return (n+5)*f(n-9)
for x in range(1, 300000):
    f(x)
print((f(234561) // 436 + f(234552) // 218) // f(234534))