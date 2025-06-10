import sys
sys.setrecursionlimit(100000)
def F(n):
    if n < 10:
        return n
    if n >= 10:
        return 3 * n + F(n - 3)
print((F(6250) + 2 * F(6244)) / F(6238))