import sys, functools
sys.setrecursionlimit(235000)
sys.set_int_max_str_digits(100000)
@functools.lru_cache(235000)
def F(n):
    if n < 17:
        return 6
    if n >= 17:
        return (n + 5) * F(n - 9)
for x in range(1, 235000):
    F(x)
print((F(234561)//436 + F(234552)//218)/F(234534))