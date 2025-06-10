import sys
sys.setrecursionlimit(100000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n + F(n - 1)
print(F(2025) - F(2022))