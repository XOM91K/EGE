import sys
import functools
sys.setrecursionlimit(1000000000)
@functools.lru_cache(None)
def F(x, y):  # x - от какого числа идем , y в какое число идем
    if x == y:
        return 1
    if x > y or x ==100:
        return 0
    if x < y:
        return F(x + x % 10, y) + F(x + x % 68, y) + F(x ** 2, y)

for x in range(69, 681):
    F(68, x)
print(F(2,68) * F(68,680))