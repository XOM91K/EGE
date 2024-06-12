import sys
sys.setrecursionlimit(10000)
def F(n):
    if n <= 400:
        return 1
    if n > 400:
        return F(n - 2) * (n - 325)
