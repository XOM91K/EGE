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
for x in range(0, 30000):
    F(x)
#d = sum(map(int, str(F(57693)))) ** 2
print(sum(map(int, str(F(14750)))))