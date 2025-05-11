import sys , functools
sys.setrecursionlimit(1000000000)
@functools.lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1)*f(n//2)+1
for x in range(10010):
    f(x)
v = str(f(10000))[-18:]
p = sum(int(d) for d in v)
print(p)