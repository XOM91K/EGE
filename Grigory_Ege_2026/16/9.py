import sys, functools
sys.setrecursionlimit(10000000)
@functools.lru_cache(None)
def F(n):
    if n < 5 :
        return n
    if n >= 5 :
        return  2 * n * F(n - 4)
for x in range(1, 13800):
    F(x)
print((F(13766)-9*F(13762))/F(13758))