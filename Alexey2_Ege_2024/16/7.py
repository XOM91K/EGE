import sys
sys.setrecursionlimit(1000000)
def F(n):
    if n < 3:
        return 3
    if n >= 3:
        return 2 * n + 5 + F(n - 2)
print(F(3027) - F(3023))