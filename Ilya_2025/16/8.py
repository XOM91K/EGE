import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    print(n)
    if n < 6:
        return n
    if n >= 6:
        return 3 * n * F(n - 3)
for i in range(1, 15000):
    F(i)
print((F(12571) - 9 * F(12568)) / F(12565))