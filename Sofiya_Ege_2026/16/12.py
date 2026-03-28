import sys, functools
sys.setrecursionlimit(1_000_000)
@functools.lru_cache(None)
def v(n):
    if n>100: return v(n-3)+28965
    if n<=100: return 5*(m(n-4)-25)
@functools.lru_cache(None)
def m(n):
    if n>=555384: return 12*n+70
    if n<555384: return m(n+8)-55
for n in range(600_000, 1, -1):
    m(n)
for n in range(1, 10_000):
    v(n)
print(v(9865) ** 2)