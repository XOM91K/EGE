import sys, functools
sys.setrecursionlimit(1000000)
@functools.lru_cache(None)
def F(n):
    if n < 3:
        return n * 4
    if n >= 3 and n % 2 != 0:
        return n * 2
    if n >= 3 and n % 2 == 0:
        return 5 * F(n - 2) + n
ct = 0
for n in range(1, 10000):
    fn = F(n)
    if len(str(fn)) == 3 and fn % 2 == 0:
        print(n)
        ct += 1
print(ct)