import sys,functools
sys.setrecursionlimit(100000000)
@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 0
    else:
        return F(n - 1) + n
ct = 0
print(1542613234-765432010 + 1)
for x in range(1, 10001):
     if F(x) % 3 != 0:
         ct += 1
print(ct)