import sys
sys.setrecursionlimit(3000)
def F(n):
    if n <= 2:
        return n
    if n > 2:
        return n + F(n - 2)
print(F(2023) + F(2020))