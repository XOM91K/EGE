import sys
sys.setrecursionlimit(10000)
def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n - 1)
print(F(2024) - F(2021))