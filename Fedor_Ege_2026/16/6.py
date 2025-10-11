import sys, functools
sys.setrecursionlimit(5000)
@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 2*n - 1
    if n % 2 == 0:
        return 4*F(n/2)
d = []
for a in range(1, 1500):
    for b in range(1, 1500):
        if F(a) - F(b) == 1045:
            d.append(abs(a - b))
print(max(d))