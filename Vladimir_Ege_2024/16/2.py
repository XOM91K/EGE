import sys, functools
sys.setrecursionlimit(10000)
@functools.lru_cache(None)
def F(n):
    if n >= 2025:
        print('1:', n)
        return n
    if n < 2025:
        print('2:', n)
        return F(n + 1) - F(n + 2) + 7
    print(n)
for x in range(2026, 1):
    F(x)
    print('.')

print(F(15) - F(24))