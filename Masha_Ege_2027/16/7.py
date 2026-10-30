import sys, functools
sys.setrecursionlimit(20000)
sys.set_int_max_str_digits(100000)
@functools.lru_cache(10000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) * (n // 2) + 1
for x in range(1, 11000):
    F(x)
s = str(F(10000))[-18:]
print(sum(map(int, s)))