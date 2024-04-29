import sys, functools
sys.setrecursionlimit(100000)
@functools.lru_cache(None)
def f(x, y):

    if x == y:
        return 1
    if x > y or x == 100:
        return 0
    if x < y:
        return f(x + int(str(x)[-1]), y) + f(x + (x % 68), y) + f(x ** 2, y)
# for x in range(1, 681):
#     for y in range(1, 681):
#         f(x, y)
print( f(68, 680))