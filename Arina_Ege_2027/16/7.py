# import sys, functools
# sys.setrecursionlimit(100000)
# @functools.lru_cache(5000)
# def f(n):
#     if n < 100:
#         return n
#     if n > 99 and n % 2 == 0:
#         return (0.5)*f(n-1)
#     if n > 99 and n % 2 != 0:
#         return 2*f(n-1)
#
#
# for n in range(17000):
#     f(n)
#
# print(1000 * (f(16384)/f(7777)))
import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(5000)
def f(n):
    if n < 100:
        return n
    if n > 99 and n % 2 == 0:
        return (1/2)*f(n-1)
    if n > 99 and n % 2 != 0:
        return 2*f(n-1)
for n in range(17000):
    f(n)
print(1000 * (f(16384)/f(7777)))