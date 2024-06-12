import functools
import sys
sys.setrecursionlimit(100000)
def F(n):
    if n >= 4938:
        return n + 6
    if n < 4938:
        return n * F(n + 5)


print(F(4928) - F(4935))