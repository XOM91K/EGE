import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def F(n):
    if n < 6:
        return n
    if n >= 6:
        return 3 * n * F(n - 3)
for i in range(12700):
    F(i)
print((F(12571) - 9 * F(12568)) / F(12565))


#1083
from functools import lru_cache
# @lru_cache(maxsize=None)
# def f(n):
#     if n == 0:
#         return 1
#     if n > 0:
#         return 2 * f(1 - n) + 3 * f(n - 1) + 2
#     if n < 0:
#         return -f(-n)
# for i in range(15000):
#     f(i)
# h = 0
# for i in str(f(14750)):
#     h += int(i)
# print(h