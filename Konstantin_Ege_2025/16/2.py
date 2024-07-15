import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)
print((2 * F(2024) + F(2023)) / F(2022))