import sys
sys.setrecursionlimit(100000)
def F(n):
    if n <= 3:
        return 1
    if n > 3:
        return (n + 3) * F(n - 2)
print(F(2028) / F(2024))