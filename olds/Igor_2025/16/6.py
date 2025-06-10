import sys
sys.setrecursionlimit(100000)
def F(n):
    if n < 3:
        return n
    if n >= 3:
        return (n - 1) * F(n - 2)
print((F(2024) - F(2022)) / F(2020))