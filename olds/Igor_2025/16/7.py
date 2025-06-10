import sys
import functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * F(n - 4)
for x in range(1, 14000):
    F(x)
print((F(13766)-9*F(13762))/F(13758))
l = []
for n in range(0, 13766 + 1):
    if n < 5:
        l.append(n)
    else:
        l.append(2 * n * l[n - 4])
print((l[13766]-9*l[13762])/l[13758])