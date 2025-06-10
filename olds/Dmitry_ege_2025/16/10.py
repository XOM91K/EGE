import sys
sys.setrecursionlimit(100000)
def F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + F(n-2)
print(F(2126) - F(2122))