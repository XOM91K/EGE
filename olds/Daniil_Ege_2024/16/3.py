import sys
sys.setrecursionlimit(25000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n + F(n - 1)
print(F(2023) - F(2019))