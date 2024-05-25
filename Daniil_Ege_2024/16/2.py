import sys
sys.setrecursionlimit(1000000)
def F(n):
    if n <= 3:
        return 2025
    if n > 3:
        return 3 * (n - 1) * F(n - 2)
print(F(2027) / F(2023))