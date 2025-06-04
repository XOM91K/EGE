import sys
sys.setrecursionlimit(10000)
def F(n):
    if n == 1:
        return 1
    else:
        return (n + 1) * F(n-1)
print(((F(2025) // 2026) + F(2024)) / F(2023))