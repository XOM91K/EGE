# import sys, functools
# sys.setrecursionlimit(100000)
# @functools.lru_cache(None)
# def F(n):
#     if n > 2024:
#         return 2
#     if n == 2024:
#         return 1
#     if n < 2024:
#         return n*(n+1) + F(n+1) - F(n+2)
# for x in range(1, 3000):
#     F(x)
# print(F(100) - F(10) + F(2020))

import sys
sys.setrecursionlimit(100000)
import functools
@functools.lru_cache(None)
def F(n):
    if n > 2024:
        return 2
    if n == 2024:
        return 1
    if n < 2024:
        return n*(n+1) + F(n+1) - F(n+2)
# два варианта либо от (3000, 1, -1)
# либо от (1, 3000)
for x in range(3000, 1, -1):
    print(F(x), x)
print(F(100) - F(10) + F(2020))