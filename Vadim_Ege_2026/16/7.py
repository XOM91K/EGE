import sys, functools
sys.setrecursionlimit(10**6)
@functools.lru_cache(None)
def f(x):
    if x <3:
        return 1
    if sum(map(int,str(x)))%2 == 0 and x>2:
        return f(x-1)-f(x-2)
    if sum(map(int,str(x)))%2 != 0 and x>2:
        return f(x-1)+f(x//2)
print(f(100))