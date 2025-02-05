import sys, functools
sys.setrecursionlimit(100_000)
@functools.lru_cache(None)
def F(n):
    if n==1:
        return 1
    if n>1:
        return 2*n+F(n-1)
for x in range(60000):
    F(x)
a = F(57693)
print(a )
print((sum(map(int,list(str(a)))))**2)