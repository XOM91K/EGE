import functools, sys
sys.setrecursionlimit(100000)
@functools.lru_cache(None)

def F(n):
    if n == 0:
        return 1
    if n > 0:
        return 2 * F(1 - n) + 3 * F(n - 1) + 2
    if n < 0:
        return -F(-n)
# LAST HOPE
for i in range(1, 15000):
    F(i)
print(sum(map(int, str(F(14750)))))