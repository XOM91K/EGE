ct = 0
import sys, functools
sys.setrecursionlimit(10000000)
@functools.lru_cache(None)
def F(n):
    if n < 3:
        return n * 4
    if n >= 3 and n % 2 != 0:
        return n * 2
    if n >= 3 and n % 2 == 0:
        return (5 * F(n - 2)) + n
for n in range(1, 10000):
    f = F(n)
    if len(str(f)) == 3 and f % 2 == 0:
        ct += 1
print(ct)